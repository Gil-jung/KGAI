from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional, Dict
from pydantic import BaseModel
import traceback
from database.neo4j_db import neo4j_db
from database.mongo_db import mongo_db

app = FastAPI(
    title="AI Knowledge Graph API",
    description="AI 지식 그래프를 위한 API",
    version="1.0.0",
)

class NodeCreate(BaseModel):
    name: str
    category: str
    properties: Optional[Dict[str, str]] = {}
    markdown_content: str

class NodeUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    properties: Optional[Dict[str, str]] = None
    markdown_content: Optional[str] = None

class NodeResponse(BaseModel):
    id: int
    name: str
    category: str
    properties: Dict[str, str]

class EdgeCreate(BaseModel):
    source_id: int
    target_id: int
    relationship_type: str

class EdgeResponse(BaseModel):
    id: int
    source_id: int
    target_id: int
    relationship_type: str

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
        update_data = {k: v for k, v in node.dict().items() if v is not None and k != 'markdown_content'}
        neo4j_result = neo4j_db.update_node(node_id, update_data)

        # MongoDB 마크다운 문서 업데이트
        if node.markdown_content is not None:
            mongo_db.update_document(node_id, node.markdown_content)

        return NodeResponse(
            id=node_id,
            name=neo4j_result['name'],
            category=neo4j_result['category'],
            properties=neo4j_result['properties']
        )
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
    """
    노드를 검색합니다.

    - **query**: 검색할 키워드
    - **category**: 검색할 노드의 카테고리 (선택사항)
    - **limit**: 반환할 최대 결과 수 (기본값: 10)
    """
    try:
        results = neo4j_db.search_nodes(query, category, limit)
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)