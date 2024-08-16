from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "your_password"  # Neo4j 설치 시 설정한 비밀번호로 변경

driver = GraphDatabase.driver(uri, auth=(user, password))

def add_ai_concept(tx, name, description):
    tx.run("MERGE (a:AIConcept {name: $name}) "
           "ON CREATE SET a.description = $description",
           name=name, description=description)

def add_relation(tx, name1, name2, relation):
    tx.run("MATCH (a:AIConcept {name: $name1}), (b:AIConcept {name: $name2}) "
           "MERGE (a)-[r:" + relation + "]->(b)",
           name1=name1, name2=name2)

def init_database():
    with driver.session() as session:
        # AI 개념 노드 추가
        session.write_transaction(add_ai_concept, "머신러닝", "데이터로부터 학습하여 예측 또는 결정을 수행하는 AI의 한 분야")
        session.write_transaction(add_ai_concept, "딥러닝", "여러 층의 인공 신경망을 사용하는 머신러닝의 한 방법")
        session.write_transaction(add_ai_concept, "자연어처리", "컴퓨터가 인간의 언어를 이해하고 처리하는 AI 기술")
        session.write_transaction(add_ai_concept, "컴퓨터 비전", "컴퓨터가 디지털 이미지나 비디오를 이해하는 AI 기술")

        # 관계 추가
        session.write_transaction(add_relation, "머신러닝", "딥러닝", "INCLUDES")
        session.write_transaction(add_relation, "딥러닝", "자연어처리", "APPLIED_TO")
        session.write_transaction(add_relation, "딥러닝", "컴퓨터 비전", "APPLIED_TO")

    print("Database initialized with sample AI concepts and relations.")

if __name__ == "__main__":
    init_database()
    driver.close()