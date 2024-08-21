from knowledge_graph_manager import KnowledgeGraphManager
import json

manager = KnowledgeGraphManager()

# 노드 생성
nodes = [
    {
        "name": "머신러닝",
        "category": "인공지능 기술",
        "properties": {
            "정의": "컴퓨터가 명시적인 프로그래밍 없이 데이터를 분석하고 패턴을 인식하여 작업을 수행하는 인공지능의 한 분야",
            "주요_개념": ["데이터", "모델", "학습", "특징", "라벨"],
            "종류": ["지도학습", "비지도학습", "강화학습"],
            "활용_분야": ["이미지 및 음성 인식", "자연어 처리", "추천 시스템", "자율주행 자동차", "금융"],
            "과정": ["데이터 수집", "데이터 전처리", "모델 선택", "모델 학습", "모델 평가", "모델 개선", "배포 및 사용"],
            "한계_및_도전과제": ["데이터 의존성", "해석 가능성", "과적합"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00001_machine_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "지도학습",
        "category": "머신러닝 방법론",
        "properties": {
            "정의": "라벨이 있는 데이터를 사용해 학습하는 방법",
            "특징": ["입력 데이터와 정답(라벨)이 주어짐", "새로운 입력 데이터에 대한 결과를 예측"],
            "예시": ["스팸 메일 분류기", "이미지 분류"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00002_supervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "비지도학습",
        "category": "머신러닝 방법론",
        "properties": {
            "정의": "라벨이 없는 데이터를 사용해 학습하는 방법",
            "특징": ["데이터 간의 패턴이나 그룹을 스스로 찾아냄"],
            "예시": ["고객 세분화", "이상 탐지"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00003_unsupervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "강화학습",
        "category": "머신러닝 방법론",
        "properties": {
            "정의": "에이전트가 환경과 상호작용하며 보상을 극대화하는 방향으로 학습하는 방법",
            "특징": ["에이전트가 행동을 취하고 보상을 받음", "다음 행동을 결정하기 위해 보상을 사용"],
            "예시": ["게임 AI", "로봇 제어"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00004_reinforcement_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "분류",
        "category": "지도학습 작업",
        "properties": {
            "정의": "입력 데이터를 미리 정의된 범주 중 하나로 할당하는 작업",
            "예시": ["이메일 스팸 필터", "이미지 분류", "감정 분석"],
            "알고리즘": ["로지스틱 회귀", "결정 트리", "랜덤 포레스트", "서포트 벡터 머신", "신경망"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00005_classification.md", "r", encoding="utf-8").read()
    },
    {
        "name": "회귀",
        "category": "지도학습 작업",
        "properties": {
            "정의": "입력 변수와 출력 변수 사이의 관계를 모델링하는 통계적 방법",
            "주요_알고리즘": ["선형 회귀", "릿지 회귀", "라쏘 회귀", "엘라스틱넷", "결정 트리 회귀", "랜덤 포레스트 회귀", "서포트 벡터 회귀"],
            "응용_분야": ["주식 가격 예측", "부동산 가격 예측", "판매량 예측", "기후 변화 모델링", "인구 증가 예측"],
            "평가_지표": ["평균 제곱 오차 (MSE)", "평균 절대 오차 (MAE)", "결정 계수 (R-squared)", "조정된 결정 계수", "평균 제곱근 오차 (RMSE)"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00006_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "과적합과 일반화",
        "category": "머신러닝 개념",
        "properties": {
            "과적합_정의": "모델이 훈련 데이터에 너무 잘 맞춰져 새로운 데이터에 대한 예측 성능이 떨어지는 현상",
            "일반화_정의": "모델이 새로운, 보지 못한 데이터에 대해서도 잘 작동하는 능력",
            "과적합_원인": ["모델의 복잡성이 데이터의 복잡성을 초과", "훈련 데이터의 부족", "노이즈에 대한 과도한 학습"],
            "방지_기법": ["교차 검증", "정규화", "앙상블 방법", "데이터 증강", "조기 종료"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00007_overfitting_and_generalization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "공짜 점심 없음 이론",
        "category": "머신러닝 개념",
        "properties": {
            "정의": "모든 문제에 대해 평균적으로 가장 좋은 성능을 내는 단일 알고리즘은 존재하지 않는다는 이론",
            "의미": "특정 문제에 대해 좋은 성능을 내는 알고리즘이 다른 문제에서는 좋지 않은 성능을 낼 수 있음",
            "시사점": ["문제에 따른 적절한 알고리즘 선택의 중요성", "도메인 지식과 경험의 가치", "하이퍼파라미터 튜닝의 필요성"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00008_no_free_lunch_theorem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "군집화",
        "category": "비지도학습 작업",
        "properties": {
            "정의": "데이터를 유사한 특성을 가진 그룹으로 나누는 작업",
            "주요_알고리즘": ["K-평균", "계층적 군집화", "DBSCAN", "가우시안 혼합 모델"],
            "응용_분야": ["고객 세분화", "이미지 압축", "이상 탐지", "문서 분류"],
            "평가_지표": ["실루엣 계수", "칼린스키-하라바즈 지수", "데이비스-볼딘 지수"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00009_clustering.md", "r", encoding="utf-8").read()
    },
    {
        "name": "잠재된 변형 인자 발견하기",
        "category": "비지도학습 작업",
        "properties": {
            "정의": "데이터의 기저에 있는 중요한 특성이나 패턴을 찾아내는 과정",
            "주요_기법": ["주성분 분석 (PCA)", "독립 성분 분석 (ICA)", "t-SNE", "오토인코더"],
            "응용_분야": ["차원 축소", "특성 추출", "데이터 시각화", "노이즈 제거"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00010_discovering_latent_factors_of_variation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "자기 지도학습",
        "category": "비지도학습 작업",
        "properties": {
            "정의": "레이블이 없는 데이터에서 자동으로 지도 신호를 생성하여 학습하는 방법",
            "특징": ["대규모 레이블 없는 데이터 활용", "사전 학습과 미세 조정 단계로 구성"],
            "응용_분야": ["자연어 처리", "컴퓨터 비전", "음성 인식"],
            "주요_기법": ["마스크 언어 모델링", "다음 단어 예측", "이미지 회전 예측", "컨텍스트 예측"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00011_self_supervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "비지도학습 평가",
        "category": "머신러닝 프로세스",
        "properties": {
            "어려움": "정답 레이블이 없어 직접적인 성능 측정이 어려움",
            "평가_방법": ["내부 평가 지표", "외부 평가 지표", "인간 평가", "다운스트림 작업 성능"],
            "주요_지표": ["실루엣 계수", "칼린스키-하라바즈 지수", "데이비스-볼딘 지수", "상호 정보량"],
            "고려사항": ["데이터의 특성", "작업의 목적", "도메인 지식"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00012_evaluation_unsupervised_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "데이터",
        "category": "머신러닝 요소",
        "properties": {
            "정의": "머신러닝 모델을 훈련하고 평가하는 데 사용되는 정보의 집합",
            "유형": ["구조화된 데이터", "비구조화된 데이터", "반구조화된 데이터"],
            "품질_요소": ["정확성", "완전성", "일관성", "시의성", "관련성"],
            "처리_단계": ["수집", "정제", "변환", "축소", "통합"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00013_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이미지 데이터셋",
        "category": "데이터 예시",
        "properties": {
            "정의": "컴퓨터 비전 작업에 사용되는 이미지 모음",
            "주요_데이터셋": ["ImageNet", "COCO", "CIFAR-10/100", "MNIST"],
            "특징": ["레이블링된 이미지", "다양한 카테고리", "대규모 데이터"],
            "응용_분야": ["이미지 분류", "객체 탐지", "이미지 분할", "얼굴 인식"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00014_image_dataset.md", "r", encoding="utf-8").read()
    },
    {
        "name": "텍스트 데이터셋",
        "category": "데이터 예시",
        "properties": {
            "정의": "자연어 처리 작업에 사용되는 텍스트 문서 모음",
            "주요_데이터셋": ["Wikipedia 덤프", "Common Crawl", "IMDb 리뷰", "Penn Treebank"],
            "특징": ["대규모 코퍼스", "다국어 데이터", "도메인 특화 데이터"],
            "응용_분야": ["텍스트 분류", "감정 분석", "기계 번역", "질의응답"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00015_text_dataset.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산적인 입력 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {
            "정의": "범주형 또는 이산적 데이터를 머신러닝 알고리즘에 적합한 형태로 변환하는 과정",
            "주요_기법": ["원-핫 인코딩", "레이블 인코딩", "빈도 인코딩", "타겟 인코딩"],
            "고려사항": ["차원의 저주", "희소성", "순서 정보 보존"],
            "응용_분야": ["범주형 변수 처리", "텍스트 데이터 토큰화", "시계열 데이터 이산화"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00016_preprocessing_discrete_input_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "텍스트 데이터 전처리",
        "category": "데이터 처리 기법",
        "properties": {
            "정의": "자연어 처리 작업을 위해 원시 텍스트 데이터를 정제하고 구조화하는 과정",
            "주요_단계": ["토큰화", "정규화", "불용어 제거", "어간 추출/표제어 추출"],
            "고급_기법": ["품사 태깅", "개체명 인식", "구문 분석"],
            "도구": ["NLTK", "spaCy", "Gensim", "TextBlob"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00017_preprocessing_text_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "결측 데이터 다루기",
        "category": "데이터 처리 기법",
        "properties": {
            "정의": "데이터셋에서 누락된 값을 처리하는 방법",
            "처리_방법": ["제거", "대체", "예측"],
            "대체_기법": ["평균/중앙값/최빈값 대체", "회귀 대체", "다중 대체"],
            "고려사항": ["결측 메커니즘", "결측 비율", "변수 간 상관관계"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00018_handling_missing_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "머신러닝과 다른 분야와의 관계",
        "category": "머신러닝 응용",
        "properties": {
            "관련_분야": ["통계학", "컴퓨터 과학", "인공지능", "데이터 과학"],
            "응용_영역": ["의료", "금융", "마케팅", "자율주행", "로보틱스"],
            "융합_사례": ["생물정보학", "계산 사회과학", "디지털 인문학"],
            "윤리적_고려사항": ["편향성", "해석 가능성", "프라이버시"]
        },
        "markdown_content": open("Documents/PML1/01_introduction/00019_the_relationship_between_ml_and_other_fields.md", "r", encoding="utf-8").read()
    }
]

created_nodes = []
for node in nodes:
    try:
        result = manager.add_node(**node)
        if result:
            created_nodes.append(result)
            print(f"노드 생성 성공: {result['name']}")
        else:
            print(f"노드 생성 실패: {node['name']}")
    except Exception as e:
        print(f"노드 '{node['name']}' 생성 중 오류 발생: {str(e)}")

# 엣지 생성
edges = [
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[1]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[2]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[3]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[1]['id'], "target_id": created_nodes[4]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[1]['id'], "target_id": created_nodes[5]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[8]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[9]['id'], "relationship_type": "포함"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[10]['id'], "relationship_type": "관련"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[6]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[7]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[12]['id'], "relationship_type": "사용"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[13]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[14]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[15]['id'], "relationship_type": "전처리_기법"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[16]['id'], "relationship_type": "전처리_기법"},
    {"source_id": created_nodes[12]['id'], "target_id": created_nodes[17]['id'], "relationship_type": "전처리_기법"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[18]['id'], "relationship_type": "관련"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[11]['id'], "relationship_type": "평가_방법"}
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