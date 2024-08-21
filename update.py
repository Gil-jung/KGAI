from knowledge_graph_manager import KnowledgeGraphManager
import json

manager = KnowledgeGraphManager()

# 노드 생성
nodes = [
    {
        "name": "머신러닝",
        "category": "인공지능 기술",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00001_machine_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "지도학습",
        "category": "머신러닝 방법론",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00002_supervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "비지도학습",
        "category": "머신러닝 방법론",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00003_unsupervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "강화학습",
        "category": "머신러닝 방법론",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00004_reinforcement_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "분류",
        "category": "지도학습 작업",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00005_classification.md", "r", encoding="utf-8").read()
    },
    {
        "name": "회귀",
        "category": "지도학습 작업",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00006_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "과적합과 일반화",
        "category": "머신러닝 개념",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00007_overfitting_and_generalization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "공짜 점심 없음 이론",
        "category": "머신러닝 개념",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00008_no_free_lunch_theorem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "군집화",
        "category": "비지도학습 작업",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00009_clustering.md", "r", encoding="utf-8").read()
    },
    {
        "name": "잠재된 변형 인자 발견하기",
        "category": "비지도학습 작업",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00010_discovering_latent_factors_of_variation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "자기 지도학습",
        "category": "비지도학습 작업",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00011_self_supervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "비지도학습 평가",
        "category": "머신러닝 프로세스",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00012_evaluation_unsupervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "데이터",
        "category": "머신러닝 요소",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00013_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이미지 데이터셋",
        "category": "데이터 예시",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00014_image_dataset.md", "r", encoding="utf-8").read()
    },
    {
        "name": "텍스트 데이터셋",
        "category": "데이터 예시",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00015_text_dataset.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산적인 입력 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00016_preprocessing_discrete_input_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "텍스트 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00017_preprocessing_text_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "결측 데이터 다루기",
        "category": "데이터 처리 기법",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00018_handling_missing_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "머신러닝과 다른 분야와의 관계",
        "category": "머신러닝 응용",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/01_introduction/00019_the_relationship_between_ml_and_other_fields.md", "r", encoding="utf-8").read()
    }
]

created_nodes = []
for node in nodes:
    result = manager.add_node(**node)
    if result:
        created_nodes.append(result)
        print(f"노드 생성 성공: {result['name']}")
    else:
        print(f"노드 생성 실패: {node['name']}")

# 엣지 생성
edges = [
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[1]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[2]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[3]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[1]['id'], "target_id": created_nodes[4]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[1]['id'], "target_id": created_nodes[5]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[6]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[7]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[8]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[9]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[10]['id'], "target_id": created_nodes[9]['id'], "relationship_type": "기반"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[11]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[12]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[13]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[14]['id'], "relationship_type": "관련"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[15]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[16]['id'], "relationship_type": "적용"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[17]['id'], "relationship_type": "적용"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[18]['id'], "relationship_type": "사용"}
]

created_edges = []
for edge in edges:
    result = manager.add_edge(**edge)
    if result:
        created_edges.append(result)
        print(f"엣지 생성 성공: {result['relationship_type']}")
    else:
        print(f"엣지 생성 실패: {edge['relationship_type']}")

graph_data = {
    "nodes": created_nodes,
    "edges": created_edges
}

with open("knowledge_graph.json", "w", encoding="utf-8") as f:
    json.dump(graph_data, f, ensure_ascii=False, indent=2)

print("지식그래프가 knowledge_graph.json 파일로 저장되었습니다.")