from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
from pydantic import BaseModel
import traceback
from database.neo4j_db import neo4j_db
from database.mongo_db import mongo_db
import logging
from urllib.parse import unquote

app = FastAPI(
    title="AI Knowledge Graph API",
    description="AI 지식 그래프를 위한 API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React 앱의 URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class NodeCreate(BaseModel):
    name: str
    category: str
    properties: Optional[Dict[str, Any]] = {}
    markdown_content: str

class NodeUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    properties: Optional[Dict[str, Any]] = None
    markdown_content: Optional[str] = None

class NodeResponse(BaseModel):
    id: int
    name: str
    category: str
    properties: Dict[str, Any]

class EdgeCreate(BaseModel):
    source_id: int
    target_id: int
    relationship_type: str

class EdgeResponse(BaseModel):
    id: int
    source_id: int
    target_id: int
    relationship_type: str

class EdgeUpdate(BaseModel):
    relationship_type: str

class NodeData(BaseModel):
    id: int
    name: str
    category: str
    properties: dict

class EdgeData(BaseModel):
    id: int
    source: int
    target: int
    relationship_type: str

class GraphData(BaseModel):
    nodes: List[NodeData]
    edges: List[EdgeData]

class MarkdownResponse(BaseModel):
    content: str

@app.post("/nodes", response_model=NodeResponse, tags=["nodes"])
async def create_node(node: NodeCreate):
    """
    새로운 노드를 생성합니다.

    - **name**: 노드의 이름
    - **category**: 노드의 카테고리
    - **properties**: 노드의 추가 속성 (선택사항)
    - **markdown_content**: 노드와 관련된 마크다운 내용
    """
    try:
        # Neo4j에 노드 추가
        neo4j_result = neo4j_db.create_node(node.name, node.category, node.properties)
        node_id = neo4j_result['id']

        # MongoDB에 마크다운 문서 추가
        mongo_db.create_document(node_id, node.markdown_content)

        return NodeResponse(
            id=node_id,
            name=neo4j_result['name'],
            category=neo4j_result['category'],
            properties=neo4j_result['properties']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/nodes/{node_id}", response_model=NodeResponse, tags=["nodes"])
async def update_node(node_id: int, node: NodeUpdate):
    """
    지정된 ID의 노드를 업데이트합니다.

    - **node_id**: 업데이트할 노드의 ID
    - **name**: 새로운 노드 이름 (선택사항)
    - **category**: 새로운 노드 카테고리 (선택사항)
    - **properties**: 업데이트할 노드 속성 (선택사항)
    - **markdown_content**: 새로운 마크다운 내용 (선택사항)
    """
    try:
        # Neo4j 노드 업데이트
        update_data = {k: v for k, v in node.dict(exclude_unset=True).items() if v is not None and k != 'markdown_content'}
        neo4j_result = neo4j_db.update_node(node_id, **update_data)

        # MongoDB 마크다운 문서 업데이트
        if node.markdown_content is not None:
            mongo_db.update_document(node_id, node.markdown_content)

        if neo4j_result:
            return NodeResponse(
                id=node_id,
                name=neo4j_result['name'],
                category=neo4j_result['category'],
                properties=neo4j_result['properties']
            )
        else:
            raise HTTPException(status_code=404, detail="Node not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nodes/{node_id}", response_model=NodeResponse, tags=["nodes"])
async def get_node(node_id: int):
    """
    지정된 ID의 노드를 조회합니다.

    - **node_id**: 조회할 노드의 ID
    """
    try:
        # Neo4j에서 노드 정보 가져오기
        neo4j_result = neo4j_db.get_node(node_id)
        if not neo4j_result:
            raise HTTPException(status_code=404, detail="Node not found")

        # MongoDB에서 마크다운 문서 가져오기
        mongo_result = mongo_db.get_document(node_id)

        return NodeResponse(
            id=node_id,
            name=neo4j_result['name'],
            category=neo4j_result['category'],
            properties=neo4j_result['properties']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search", response_model=List[NodeResponse], tags=["search"])
async def search_nodes(
    query: str = Query(..., description="검색어"),
    category: Optional[str] = Query(None, description="노드 카테고리 필터"),
    limit: int = Query(10, description="결과 제한 수")
):
    try:
        decoded_query = unquote(query)
        results = neo4j_db.search_nodes(query=decoded_query, category=category, limit=limit)
        return [NodeResponse(id=result['id'], name=result['name'], category=result['category'], properties=result['properties']) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/edges", response_model=EdgeResponse, tags=["edges"])
async def create_edge(edge: EdgeCreate):
    """
    두 노드 사이에 새로운 엣지를 생성합니다.

    - **source_id**: 시작 노드의 ID
    - **target_id**: 도착 노드의 ID
    - **relationship_type**: 관계의 유형
    """
    try:
        result = neo4j_db.create_relationship(edge.source_id, edge.target_id, edge.relationship_type)
        return EdgeResponse(
            id=result['id'],
            source_id=result['source_id'],
            target_id=result['target_id'],
            relationship_type=result['type']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nodes/{node_id}/edges", response_model=List[EdgeResponse], tags=["edges"])
async def get_node_edges(node_id: int):
    """
    지정된 노드와 연결된 모든 엣지를 조회합니다.

    - **node_id**: 엣지를 조회할 노드의 ID
    """
    try:
        results = neo4j_db.get_node_relationships(node_id)
        return [EdgeResponse(
            id=result['id'],
            source_id=result['source_id'],
            target_id=result['target_id'],
            relationship_type=result['type']
        ) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/edges/{edge_id}", response_model=EdgeResponse, tags=["edges"])
async def update_edge(edge_id: int, edge_update: EdgeUpdate):
    try:
        result = neo4j_db.update_relationship(edge_id, edge_update.relationship_type)
        if result:
            return EdgeResponse(**result)
        else:
            raise HTTPException(status_code=404, detail=f"Edge {edge_id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/edges/{edge_id}", tags=["edges"])
async def delete_edge(edge_id: int):
    """
    지정된 ID의 엣지를 삭제합니다.

    - **edge_id**: 삭제할 엣지의 ID
    """
    try:
        result = neo4j_db.delete_relationship(edge_id)
        if result:
            return {"message": "Edge deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Edge not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/nodes/{node_id}", tags=["nodes"])
async def delete_node(node_id: int = Path(..., description="삭제할 노드의 ID")):
    try:
        # Neo4j에서 노드 삭제
        neo4j_success = neo4j_db.delete_node(node_id)
        
        # MongoDB에서 문서 삭제
        mongo_success = mongo_db.delete_document(node_id)
        
        if neo4j_success and mongo_success:
            return {"message": f"Node {node_id} successfully deleted from Neo4j and MongoDB"}
        elif neo4j_success:
            return {"message": f"Node {node_id} deleted from Neo4j, but not found in MongoDB"}
        elif mongo_success:
            return {"message": f"Node {node_id} deleted from MongoDB, but not found in Neo4j"}
        else:
            raise HTTPException(status_code=404, detail=f"Node {node_id} not found in Neo4j and MongoDB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nodes/{node_id}/with_connections", response_model=GraphData, tags=["nodes"])
async def get_node_with_all_connections(node_id: int):
    try:
        result = neo4j_db.get_node_with_all_connections(node_id)
        return GraphData(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/nodes/{node_id}/markdown", response_model=MarkdownResponse, tags=["nodes"])
async def get_node_markdown(node_id: int):
    try:
        markdown_content = mongo_db.get_markdown(node_id)
        if markdown_content is None:
            raise HTTPException(status_code=404, detail="Markdown content not found")
        return MarkdownResponse(content=markdown_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)