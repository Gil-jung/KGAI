from neo4j import GraphDatabase
import os

class Neo4jDatabase:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, name, category, properties=None):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_node, name, category, properties)
            return result

    @staticmethod
    def _create_node(tx, name, category, properties):
        query = (
            f"CREATE (n:{category} {{name: $name, category: $category}}) "
            "SET n += $properties "
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties"
        )
        result = tx.run(query, name=name, category=category, properties=properties or {})
        return result.single()

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

    def update_node(self, node_id, properties):
        with self.driver.session() as session:
            result = session.write_transaction(self._update_node, node_id, properties)
            return result

    @staticmethod
    def _update_node(tx, node_id, properties):
        query = (
            "MATCH (n) WHERE id(n) = $node_id "
            "SET n += $properties "
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties"
        )
        result = tx.run(query, node_id=node_id, properties=properties)
        return result.single()

    def create_relationship(self, source_id, target_id, relationship_type):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_relationship, source_id, target_id, relationship_type)
            return result

    @staticmethod
    def _create_relationship(tx, source_id, target_id, relationship_type):
        query = (
            "MATCH (a), (b) WHERE id(a) = $source_id AND id(b) = $target_id "
            "CREATE (a)-[r:$relationship_type]->(b) "
            "RETURN id(r) as id, type(r) as type, id(a) as source_id, id(b) as target_id"
        )
        result = tx.run(query, source_id=source_id, target_id=target_id, relationship_type=relationship_type)
        return result.single()

    def search_nodes(self, query, category=None, limit=10):
        with self.driver.session() as session:
            result = session.read_transaction(self._search_nodes, query, category, limit)
            return result

    @staticmethod
    def _search_nodes(tx, query, category, limit):
        category_filter = f"WHERE n:{category} " if category else ""
        cypher_query = (
            f"MATCH (n) {category_filter}"
            "WHERE n.name CONTAINS $query "
            "RETURN id(n) as id, n.name as name, n.category as category, properties(n) as properties "
            "LIMIT $limit"
        )
        result = tx.run(cypher_query, query=query, limit=limit)
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

neo4j_db = Neo4jDatabase()