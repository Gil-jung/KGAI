from fastapi.testclient import TestClient
from main import app
from database.neo4j_db import neo4j_db
from database.mongo_db import mongo_db

client = TestClient(app)

def test_create_node():
    response = client.post(
        "/nodes",
        json={"name": "Test Node", "category": "Test", "properties": {"key": "value"}, "markdown_content": "# Test Content"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Node"
    assert data["category"] == "Test"
    assert data["properties"]["key"] == "value"

def test_get_node():
    create_response = client.post(
        "/nodes",
        json={"name": "Get Test Node", "category": "Test", "properties": {}, "markdown_content": "# Get Test Content"}
    )
    node_id = create_response.json()["id"]

    response = client.get(f"/nodes/{node_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Get Test Node"
    assert data["category"] == "Test"

def test_update_node():
    create_response = client.post(
        "/nodes",
        json={"name": "Update Test Node", "category": "Test", "properties": {}, "markdown_content": "# Update Test Content"}
    )
    node_id = create_response.json()["id"]

    update_response = client.put(
        f"/nodes/{node_id}",
        json={"name": "Updated Node", "properties": {"new_key": "new_value"}}
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Updated Node"
    assert data["properties"]["new_key"] == "new_value"

def test_search_nodes():
    client.post(
        "/nodes",
        json={"name": "Search Test Node", "category": "SearchTest", "properties": {}, "markdown_content": "# Search Test Content"}
    )

    response = client.get("/search?query=Search Test&category=SearchTest")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["name"] == "Search Test Node"

def test_create_edge():
    node1 = client.post(
        "/nodes",
        json={"name": "Edge Test Node 1", "category": "Test", "properties": {}, "markdown_content": "# Edge Test Content 1"}
    ).json()
    node2 = client.post(
        "/nodes",
        json={"name": "Edge Test Node 2", "category": "Test", "properties": {}, "markdown_content": "# Edge Test Content 2"}
    ).json()

    response = client.post(
        "/edges",
        json={"source_id": node1["id"], "target_id": node2["id"], "relationship_type": "TEST_RELATION"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["source_id"] == node1["id"]
    assert data["target_id"] == node2["id"]
    assert data["relationship_type"] == "TEST_RELATION"

def teardown_module(module):
    neo4j_db.driver.close()
    mongo_db.client.close()