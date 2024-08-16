from fastapi import FastAPI, HTTPException
from neo4j import GraphDatabase
from elasticsearch import Elasticsearch
import markdown
import os

app = FastAPI()

# Neo4j 연결 설정
neo4j_uri = "bolt://localhost:7687"
neo4j_user = "neo4j"
neo4j_password = "YpE6gYc-bGNHiU5CZQbNeoeCcp2FV09JeCgvX-jwUOU"
graph = GraphDatabase.driver(neo4j_uri, auth=(neo4j_user, neo4j_password))

# Elasticsearch 연결 설정 (수정된 부분)
es = Elasticsearch("http://localhost:9200")

# 마크다운 문서 디렉토리 설정
MARKDOWN_DIR = "markdown_docs"

@app.get("/api/graph")
def get_graph():
    with graph.session() as session:
        result = session.run("MATCH (n)-[r]->(m) RETURN n, r, m")
        nodes = []
        edges = []
        for record in result:
            nodes.extend([record["n"], record["m"]])
            edges.append(record["r"])
        return {"nodes": [dict(node) for node in set(nodes)],
                "edges": [dict(edge) for edge in edges]}

@app.get("/api/node/{node_id}")
def get_node(node_id: str):
    with graph.session() as session:
        result = session.run("MATCH (n) WHERE id(n) = $id RETURN n", id=node_id)
        node = result.single()
        if node:
            return dict(node["n"])
        raise HTTPException(status_code=404, detail="Node not found")

@app.get("/api/document/{node_id}")
def get_document(node_id: str):
    file_path = os.path.join(MARKDOWN_DIR, f"{node_id}.md")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            html = markdown.markdown(content)
            return {"content": html}
    raise HTTPException(status_code=404, detail="Document not found")

@app.get("/api/search")
def search(query: str):
    result = es.search(index="knowledge_graph", body={"query": {"match": {"content": query}}})
    return result["hits"]["hits"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)