from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
import traceback
from database.neo4j_db import neo4j_db
from database.mongo_db import mongo_db

app = FastAPI()

class SearchResult(BaseModel):
    node_id: int
    label: str
    properties: dict

class NodeData(BaseModel):
    label: str
    properties: dict
    content: str
    related: List[str]
    markdown_content: str

@app.get("/")
async def root():
    return {"message": "AI Knowledge Graph API"}

@app.post("/nodes")
async def create_node(label: str, properties: dict):
    node = neo4j_db.create_node(label, properties)
    return {"node_id": node["node_id"], "properties": dict(node["n"])}

@app.get("/nodes/{node_id}")
async def get_node(node_id: int):
    node = neo4j_db.get_node(node_id)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return {"node_id": node_id, "properties": dict(node["n"])}

@app.put("/nodes/{node_id}")
async def update_node(node_id: int, properties: dict):
    node = neo4j_db.update_node(node_id, properties)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return {"node_id": node_id, "properties": dict(node["n"])}

@app.delete("/nodes/{node_id}")
async def delete_node(node_id: int):
    result = neo4j_db.delete_node(node_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Node not found")
    return {"message": "Node deleted successfully"}

@app.post("/documents")
async def create_document(node_id: int, content: str):
    doc_id = mongo_db.create_document(node_id, content)
    return {"document_id": doc_id, "node_id": node_id}

@app.get("/documents/{node_id}")
async def get_document(node_id: int):
    document = mongo_db.get_document(node_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.put("/documents/{node_id}")
async def update_document(node_id: int, content: str):
    result = mongo_db.update_document(node_id, content)
    if result == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document updated successfully"}

@app.delete("/documents/{node_id}")
async def delete_document(node_id: int):
    result = mongo_db.delete_document(node_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted successfully"}

@app.get("/search", response_model=List[SearchResult])
async def search_nodes(
    query: str = Query(..., description="검색어"),
    labels: Optional[List[str]] = Query(None, description="노드 라벨 필터"),
    limit: int = Query(10, description="결과 제한 수")
):
    results = neo4j_db.search_nodes(query, labels, limit)
    return [SearchResult(node_id=result["id"], label=result["label"], properties=result["properties"]) for result in results]

@app.post("/expand-node/{node_id}")
async def expand_node(node_id: int):
    expanded_nodes = neo4j_db.expand_node(node_id)
    return {"expanded_nodes": expanded_nodes}

@app.post("/add_data")
async def add_data(nodes: List[NodeData]):
    try:
        for node in nodes:
            # Neo4j에 노드 추가
            node_id = neo4j_db.create_node(node.label, node.properties)
            
            # MongoDB에 문서 추가
            mongo_db.create_document(str(node_id), {
                "content": node.content,
                "markdown_content": node.markdown_content
            })
            
            # 관련 노드 연결
            for related_label in node.related:
                related_id = neo4j_db.get_node_by_label(related_label)
                if related_id:
                    neo4j_db.create_relationship(node_id, related_id, "RELATED_TO")
                else:
                    # 관련 노드가 없으면 새로 생성
                    new_related_id = neo4j_db.create_node(related_label, {})
                    neo4j_db.create_relationship(node_id, new_related_id, "RELATED_TO")
        
        return {"message": f"{len(nodes)} nodes added successfully"}
    except Exception as e:
        error_msg = f"Error adding data: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)  # 서버 콘솔에 오류 출력
        raise HTTPException(status_code=500, detail=error_msg)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)