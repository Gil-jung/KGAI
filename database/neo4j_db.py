from neo4j import GraphDatabase
import os
import logging
from urllib.parse import unquote
from typing import List, Optional, Dict, Any

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Neo4jDatabase:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            logger.info("Successfully connected to Neo4j database")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j database: {str(e)}")
            raise

    def close(self):
        self.driver.close()

    def create_node(self, name, category, properties=None):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_node, name, category, properties)
            logger.debug(f"Created node: {result}")
            return result

    @staticmethod
    def _create_node(tx, name, category, properties):
        # 카테고리에서 공백을 제거하고 CamelCase로 변환
        safe_category = ''.join(word.capitalize() for word in category.split())
        
        query = (
            f"CREATE (n:{safe_category} {{name: $name, category: $category}})"
            "SET n += $properties "
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties"
        )
        result = tx.run(query, name=name, category=category, properties=properties)
        return result.single().data()

    def get_node(self, node_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_node, node_id)
            return result

    @staticmethod
    def _get_node(tx, node_id):
        query = (
            "MATCH (n) WHERE id(n) = $node_id "
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties"
        )
        result = tx.run(query, node_id=node_id)
        return result.single()

    def update_node(self, node_id, name: Optional[str] = None, category: Optional[str] = None, properties: Optional[Dict[str, Any]] = None):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._update_node, node_id, name, category, properties
            )
            return result

    @staticmethod
    def _update_node(tx, node_id: int, name: Optional[str], category: Optional[str], properties: Optional[Dict[str, Any]]):
        query_parts = []
        params = {"node_id": node_id}

        if name is not None:
            query_parts.append("SET n.name = $name")
            params["name"] = name
        if category is not None:
            safe_category = ''.join(word.capitalize() for word in category.split())
            query_parts.append(f"REMOVE n:{safe_category} SET n:{safe_category}, n.category = $category")
            params["category"] = category
        if properties is not None:
            query_parts.append("SET n += $properties")
            params["properties"] = properties

        if not query_parts:
            return None

        query = (
            "MATCH (n) WHERE id(n) = $node_id "
            + " ".join(query_parts)
            + " RETURN n"
        )
        result = tx.run(query, **params)
        return result.single()

    def create_relationship(self, source_id, target_id, relationship_type):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._create_relationship, source_id, target_id, relationship_type
            )
            return result

    @staticmethod
    def _create_relationship(tx, source_id, target_id, relationship_type):
        # 관계 유형에서 특수 문자 제거 및 공백을 언더스코어로 대체
        safe_relationship_type = ''.join(c if c.isalnum() else '_' for c in relationship_type)
        
        query = (
            f"MATCH (a), (b) "
            f"WHERE id(a) = $source_id AND id(b) = $target_id "
            f"CREATE (a)-[r:{safe_relationship_type}]->(b) "
            f"RETURN id(r) as id, type(r) as type, id(a) as source_id, id(b) as target_id"
        )
        result = tx.run(query, source_id=source_id, target_id=target_id)
        return result.single().data()

    def search_nodes(self, query: str, category: Optional[str] = None, limit: int = 10):
        with self.driver.session() as session:
            result = session.read_transaction(self._search_nodes, query=query, category=category, limit=limit)
            logger.debug(f"Search query: {query}, Category: {category}, Limit: {limit}")
            logger.debug(f"Search result: {result}")
            return result

    @staticmethod
    def _search_nodes(tx, query: str, category: Optional[str] = None, limit: int = 10):
        safe_category = ''.join(word.capitalize() for word in category.split()) if category else None
        category_filter = f"AND n:{safe_category} " if safe_category else ""
        cypher_query = (
            "MATCH (n) "
            "WHERE toLower(n.name) CONTAINS toLower($search_query) " + category_filter +
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties "
            "LIMIT $limit"
        )
        result = tx.run(cypher_query, search_query=query, limit=limit)
        return [record.data() for record in result]

    def get_node_relationships(self, node_id):
        with self.driver.session() as session:
            return session.read_transaction(self._get_node_relationships, node_id)

    @staticmethod
    def _get_node_relationships(tx, node_id):
        query = (
            "MATCH (n)-[r]-(m) WHERE id(n) = $node_id "
            "RETURN id(r) as id, type(r) as type, id(startNode(r)) as source_id, id(endNode(r)) as target_id"
        )
        result = tx.run(query, node_id=node_id)
        return [record.data() for record in result]

    def delete_relationship(self, relationship_id):
        with self.driver.session() as session:
            return session.write_transaction(self._delete_relationship, relationship_id)

    @staticmethod
    def _delete_relationship(tx, relationship_id):
        query = (
            "MATCH ()-[r]-() WHERE id(r) = $relationship_id "
            "DELETE r"
        )
        result = tx.run(query, relationship_id=relationship_id)
        return result.consume().counters.relationships_deleted > 0

    def delete_node(self, node_id: int):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_node, node_id)
            return result

    @staticmethod
    def _delete_node(tx, node_id: int):
        query = (
            "MATCH (n) "
            "WHERE id(n) = $node_id "
            "DETACH DELETE n "
            "RETURN count(n) as deleted_count"
        )
        result = tx.run(query, node_id=node_id)
        return result.single()["deleted_count"] > 0

    def test_connection(self):
        with self.driver.session() as session:
            result = session.run("RETURN 1 AS num")
            return result.single()["num"] == 1

    def update_relationship(self, relationship_id, new_type):
        with self.driver.session() as session:
            return session.write_transaction(self._update_relationship, relationship_id, new_type)

    @staticmethod
    def _update_relationship(tx, relationship_id, new_type):
        safe_new_type = ''.join(c if c.isalnum() else '_' for c in new_type)
        query = (
            f"MATCH ()-[r]-() WHERE id(r) = $relationship_id "
            f"SET r:{safe_new_type} "
            f"RETURN id(r) as id, type(r) as type, id(startNode(r)) as source_id, id(endNode(r)) as target_id"
        )
        result = tx.run(query, relationship_id=relationship_id)
        return result.single().data() if result.single() else None

    def get_node_with_all_connections(self, node_id: int) -> Dict[str, List[Dict[str, Any]]]:
        with self.driver.session() as session:
            result = session.read_transaction(self._get_node_with_all_connections, node_id)
            return result

    @staticmethod
    def _get_node_with_all_connections(tx, node_id: int):
        query = """
        MATCH (n)
        WHERE id(n) = $node_id
        CALL apoc.path.subgraphAll(n, {
            relationshipFilter: ">",
            maxLevel: 10
        })
        YIELD nodes, relationships
        WITH n AS main_node, nodes, relationships
        RETURN main_node,
               [node IN nodes WHERE id(node) <> id(main_node) | {
                   id: id(node),
                   name: node.name,
                   category: labels(node)[0],
                   properties: properties(node)
               }] AS related_nodes,
               [rel IN relationships | {
                   id: id(rel),
                   source: id(startNode(rel)),
                   target: id(endNode(rel)),
                   relationship_type: type(rel)
               }] AS edges
        """
        result = tx.run(query, node_id=node_id)
        record = result.single()
        
        if not record:
            return {"nodes": [], "edges": []}

        main_node = record["main_node"]
        main_node_data = {
            "id": node_id,
            "name": main_node["name"],
            "category": list(main_node.labels)[0],
            "properties": dict(main_node)
        }

        nodes = [main_node_data] + record["related_nodes"]
        edges = record["edges"]

        return {"nodes": nodes, "edges": edges}

neo4j_db = Neo4jDatabase()
if neo4j_db.test_connection():
    logger.info("Neo4j connection test successful")
else:
    logger.error("Neo4j connection test failed")