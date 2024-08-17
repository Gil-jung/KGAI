import os, re
from dotenv import load_dotenv
from neo4j import GraphDatabase
import openai
from typing import List, Optional

load_dotenv()

def escape_label(label):
    if re.search(r'[^a-zA-Z0-9]', label):
        return f"`{label}`"
    return label

class Neo4jDatabase:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # def create_node(self, label, properties):
    #     with self.driver.session() as session:
    #         result = session.write_transaction(self._create_node, label, properties)
    #         return result

    def get_node(self, node_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_node, node_id)
            return result

    def update_node(self, node_id, properties):
        with self.driver.session() as session:
            result = session.write_transaction(self._update_node, node_id, properties)
            return result

    def delete_node(self, node_id):
        with self.driver.session() as session:
            result = session.write_transaction(self._delete_node, node_id)
            return result

    def search_nodes(self, query: str, labels: Optional[List[str]] = None, limit: int = 10):
        with self.driver.session() as session:
            return session.read_transaction(self._search_nodes, query, labels, limit)

    def expand_node(self, node_id: int):
        with self.driver.session() as session:
            return session.write_transaction(self._expand_node, node_id)

    def create_node(self, label, properties):
        with self.driver.session() as session:
            escaped_label = escape_label(label)
            result = session.write_transaction(
                lambda tx: tx.run(
                    f"CREATE (n:{escaped_label} $props) RETURN id(n) as node_id",
                    props=properties
                ).single()
            )
            return result["node_id"]

    def get_node_by_label(self, label):
        with self.driver.session() as session:
            escaped_label = escape_label(label)
            result = session.read_transaction(
                lambda tx: tx.run(
                    f"MATCH (n:{escaped_label}) RETURN id(n) as node_id"
                ).single()
            )
            return result["node_id"] if result else None

    def create_relationship(self, source_id, target_id, relationship_type):
        with self.driver.session() as session:
            escaped_relationship = escape_label(relationship_type)
            session.write_transaction(
                lambda tx: tx.run(
                    f"MATCH (a), (b) WHERE id(a) = $source_id AND id(b) = $target_id "
                    f"CREATE (a)-[r:{escaped_relationship}]->(b)",
                    source_id=source_id, target_id=target_id
                )
            )


    @staticmethod
    def _create_node(tx, label, properties):
        query = (
            f"CREATE (n:{label} $properties) "
            "RETURN id(n) as node_id, n"
        )
        result = tx.run(query, properties=properties)
        return result.single()

    @staticmethod
    def _get_node(tx, node_id):
        query = (
            "MATCH (n) "
            "WHERE id(n) = $node_id "
            "RETURN n"
        )
        result = tx.run(query, node_id=node_id)
        return result.single()

    @staticmethod
    def _update_node(tx, node_id, properties):
        query = (
            "MATCH (n) "
            "WHERE id(n) = $node_id "
            "SET n += $properties "
            "RETURN n"
        )
        result = tx.run(query, node_id=node_id, properties=properties)
        return result.single()

    @staticmethod
    def _delete_node(tx, node_id):
        query = (
            "MATCH (n) "
            "WHERE id(n) = $node_id "
            "DELETE n"
        )
        result = tx.run(query, node_id=node_id)
        return result.consume().counters.nodes_deleted

    @staticmethod
    def _search_nodes(tx, query: str, labels: Optional[List[str]], limit: int):
        label_filter = ""
        if labels:
            label_filter = f"WHERE n:{' OR n:'.join(labels)} "

        cypher_query = (
            f"MATCH (n) {label_filter}"
            "WHERE any(prop in keys(n) WHERE toString(n[prop]) CONTAINS $query) "
            "RETURN id(n) as id, labels(n) as label, properties(n) as properties "
            "LIMIT $limit"
        )
        result = tx.run(cypher_query, query=query, limit=limit)
        return [record.data() for record in result]

    @staticmethod
    def _expand_node(tx, node_id: int):
        # 여기서는 OpenAI API를 사용하여 노드를 확장하는 예시를 보여줍니다.
        # 실제 구현에서는 적절한 AI 모델이나 외부 API를 사용해야 합니다.
        openai.api_key = "your-openai-api-key"

        # 노드 정보 가져오기
        node_info = tx.run("MATCH (n) WHERE id(n) = $node_id RETURN properties(n) as props", node_id=node_id).single()["props"]

        # AI 모델을 사용하여 관련 개념 생성
        prompt = f"Generate 3 related concepts for: {node_info}"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        related_concepts = response.choices[0].text.strip().split("\n")

        # 새로운 노드 생성 및 관계 설정
        new_nodes = []
        for concept in related_concepts:
            result = tx.run(
                "CREATE (n:Concept {name: $name}) "
                "WITH n "
                "MATCH (m) WHERE id(m) = $node_id "
                "CREATE (m)-[:RELATED_TO]->(n) "
                "RETURN id(n) as id, labels(n) as label, properties(n) as properties",
                name=concept, node_id=node_id
            )
            new_nodes.append(result.single().data())

        return new_nodes

# Neo4j Aura 데이터베이스 인스턴스 생성
neo4j_db = Neo4jDatabase()


if __name__ == "__main__":
    try:
        with neo4j_db.driver.session() as session:
            result = session.run("RETURN 1 AS num")
            print(result.single()["num"])
        print("Neo4j Aura DB 연결 성공!")
    except Exception as e:
        print(f"Neo4j Aura DB 연결 실패: {e}")