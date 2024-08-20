from knowledge_graph_manager import KnowledgeGraphManager
import json

manager = KnowledgeGraphManager()

# 노드 생성
nodes = [
    {
        "name": "머신러닝",
        "category": "인공지능 기술",
        "properties": {
            "정의": "데이터로부터 학습하여 성능을 향상시키는 알고리즘",
            "주요_분야": "지도학습, 비지도학습, 강화학습"
        },
        "markdown_content": open("Documents/00001_machine_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "지도학습",
        "category": "머신러닝 방법론",
        "properties": {
            "특징": "레이블이 있는 데이터 사용",
            "예시": "분류, 회귀"
        },
        "markdown_content": open("Documents/00002_supervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "비지도학습",
        "category": "머신러닝 방법론",
        "properties": {
            "특징": "레이블이 없는 데이터 사용",
            "예시": "클러스터링, 차원 축소"
        },
        "markdown_content": open("Documents/00003_unsupervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "강화학습",
        "category": "머신러닝 방법론",
        "properties": {
            "특징": "환경과 상호작용하며 학습",
            "주요_개념": "에이전트, 환경, 보상"
        },
        "markdown_content": open("Documents/00004_reinforcement_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "분류",
        "category": "머신러닝 작업",
        "properties": {
            "정의": "데이터를 미리 정의된 범주로 구분",
            "예시": "이메일 스팸 분류, 이미지 인식"
        },
        "markdown_content": open("Documents/00005_classification.md", "r", encoding="utf-8").read()
    },
    {
        "name": "회귀",
        "category": "머신러닝 작업",
        "properties": {
            "정의": "연속적인 출력값 예측",
            "예시": "주택 가격 예측, 판매량 예측"
        },
        "markdown_content": open("Documents/00006_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "클러스터링",
        "category": "머신러닝 작업",
        "properties": {
            "정의": "유사한 데이터를 그룹화",
            "알고리즘_예시": "K-means, DBSCAN"
        },
        "markdown_content": open("Documents/00007_clustering.md", "r", encoding="utf-8").read()
    },
    {
        "name": "차원 축소",
        "category": "데이터 처리 기법",
        "properties": {
            "목적": "데이터의 복잡성 감소",
            "기법_예시": "PCA, t-SNE"
        },
        "markdown_content": open("Documents/00008_dimensionality_reduction.md", "r", encoding="utf-8").read()
    },
    {
        "name": "앙상블 학습",
        "category": "머신러닝 기법",
        "properties": {
            "정의": "여러 모델을 결합하여 성능 향상",
            "방법_예시": "배깅, 부스팅, 스태킹"
        },
        "markdown_content": open("Documents/00009_ensemble_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "신경망",
        "category": "머신러닝 모델",
        "properties": {
            "구조": "입력층, 은닉층, 출력층",
            "학습_방법": "역전파 알고리즘"
        },
        "markdown_content": open("Documents/00010_neural_networks.md", "r", encoding="utf-8").read()
    },
    {
        "name": "딥러닝",
        "category": "인공지능 기술",
        "properties": {
            "특징": "다층 신경망 사용",
            "응용_분야": "컴퓨터 비전, 자연어 처리"
        },
        "markdown_content": open("Documents/00011_deep_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "모델 평가",
        "category": "머신러닝 프로세스",
        "properties": {
            "목적": "모델의 성능과 일반화 능력 측정",
            "기법": "교차 검증, 홀드아웃 검증"
        },
        "markdown_content": open("Documents/00012_model_evaluation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "데이터",
        "category": "머신러닝 요소",
        "properties": {
            "유형": "구조화 데이터, 비구조화 데이터",
            "품질_요소": "정확성, 완전성, 일관성"
        },
        "markdown_content": open("Documents/00013_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "특성 공학",
        "category": "데이터 처리 기법",
        "properties": {
            "정의": "원시 데이터로부터 유용한 특성 추출",
            "기법": "정규화, 원-핫 인코딩, 비닝"
        },
        "markdown_content": open("Documents/00014_feature_engineering.md", "r", encoding="utf-8").read()
    },
    {
        "name": "과적합과 과소적합",
        "category": "머신러닝 개념",
        "properties": {
            "과적합": "훈련 데이터에 지나치게 최적화",
            "과소적합": "모델이 데이터의 패턴을 충분히 학습하지 못함"
        },
        "markdown_content": open("Documents/00015_overfitting_underfitting.md", "r", encoding="utf-8").read()
    },
    {
        "name": "하이퍼파라미터 튜닝",
        "category": "머신러닝 프로세스",
        "properties": {
            "목적": "모델의 성능 최적화",
            "방법": "그리드 서치, 랜덤 서치, 베이지안 최적화"
        },
        "markdown_content": open("Documents/00016_hyperparameter_tuning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "텍스트 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {
            "단계": "토큰화, 정제, 정규화",
            "기법": "불용어 제거, 어간 추출, 품사 태깅"
        },
        "markdown_content": open("Documents/00017_preprocessing_text_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이미지 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {
            "기법": "크기 조정, 정규화, 데이터 증강",
            "목적": "모델 입력에 적합한 형태로 변환"
        },
        "markdown_content": open("Documents/00018_preprocessing_image_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "시계열 데이터 분석",
        "category": "데이터 분석 기법",
        "properties": {
            "특징": "시간에 따른 데이터 패턴 분석",
            "기법": "이동 평균, 지수 평활법, ARIMA"
        },
        "markdown_content": open("Documents/00019_time_series_analysis.md", "r", encoding="utf-8").read()
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