from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "여러 확률 변수의 결합 분포",
        "category": "확률론 개념",
        "properties": {
            "정의": "두 개 이상의 확률 변수에 대한 동시 확률 분포",
            "특징": ["다변량 확률 분포", "주변화를 통한 개별 분포 도출 가능"],
            "응용": ["다변량 데이터 분석", "복잡한 시스템 모델링"],
            "관련_개념": ["조건부 확률", "독립성", "공분산"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00059_joint_distributions_for_multiple_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "공분산",
        "category": "통계학 개념",
        "properties": {
            "정의": "두 확률 변수 간의 선형 관계를 측정하는 통계량",
            "수식": "Cov(X,Y) = E[(X - E[X])(Y - E[Y])]",
            "특징": ["대칭성", "스케일 의존성"],
            "응용": ["포트폴리오 이론", "주성분 분석"],
            "관련_개념": ["상관계수", "분산"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00060_covariance.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상관",
        "category": "통계학 개념",
        "properties": {
            "정의": "두 변수 간의 선형 관계의 강도와 방향을 나타내는 측도",
            "범위": "[-1, 1]",
            "해석": ["1은 완벽한 양의 선형 관계", "0은 선형 관계 없음", "-1은 완벽한 음의 선형 관계"],
            "종류": ["피어슨 상관계수", "스피어만 순위 상관계수"],
            "한계": ["비선형 관계 포착 불가", "인과관계 설명 불가"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00061_correlation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "무상관은 독립을 뜻하지 않는다",
        "category": "통계학 개념",
        "properties": {
            "주요_내용": "상관관계가 0이라고 해서 두 변수가 반드시 독립인 것은 아님",
            "예시": "Y = X^2 (X가 표준 정규 분포를 따를 때)",
            "함의": ["비선형 관계 존재 가능", "상관계수의 한계"],
            "중요성": "데이터 분석 시 다양한 관계 고려 필요"
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00062_uncorrelated_does_not_imply_causation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상관성은 인과성을 뜻하지 않는다",
        "category": "통계학 개념",
        "properties": {
            "주요_내용": "두 변수 간 상관관계가 있다고 해서 반드시 인과관계가 있는 것은 아님",
            "예시": ["얼음크림 판매량과 익사 사고 건수", "닭의 수와 자동차 생산량"],
            "오류_원인": ["제3의 변수 존재", "우연한 일치", "역인과관계"],
            "해결_방법": ["실험 설계", "인과 추론 기법", "도메인 지식 활용"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00063_correlation_does_not_imply_causation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "심슨의 역설",
        "category": "통계학 개념",
        "properties": {
            "정의": "부분 집단에서의 경향성이 전체 집단에서 사라지거나 역전되는 현상",
            "원인": ["집단 간 이질성", "숨겨진 변수의 영향"],
            "예시": ["버클리 대학 입학 성비 문제", "신장결석 치료 효과 연구"],
            "해결방법": ["층화 분석", "인과 모델링"],
            "중요성": "데이터 해석 시 주의 필요"
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00064_simpson_paradox.md", "r", encoding="utf-8").read()
    },
    {
        "name": "다변량 가우스(정규) 분포",
        "category": "확률론 개념",
        "properties": {
            "정의": "여러 변수에 대한 가우스 분포의 일반화",
            "매개변수": ["평균 벡터", "공분산 행렬"],
            "특징": ["타원형 등고선", "선형 변환 불변성"],
            "응용": ["다변량 데이터 모델링", "주성분 분석"],
            "한계": ["비선형 관계 표현 어려움"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00065_the_multivariate_gaussian_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "마할라노비스 거리",
        "category": "통계학 개념",
        "properties": {
            "정의": "다변량 공간에서 점과 분포 간의 거리를 측정하는 방법",
            "수식": "√((x-μ)^T Σ^(-1) (x-μ))",
            "특징": ["스케일 불변성", "상관관계 고려"],
            "응용": ["이상치 탐지", "분류 알고리즘"],
            "관련_개념": ["유클리드 거리", "공분산 행렬"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00066_mahalanobis_distance.md", "r", encoding="utf-8").read()
    },
    {
        "name": "다변량 정규 분포(MVN)의 주변 및 조건부 분포",
        "category": "확률론 개념",
        "properties": {
            "주변 분포": "부분 집합 변수의 분포",
            "조건부 분포": "일부 변수가 주어졌을 때 나머지 변수의 분포",
            "특징": ["주변 분포도 정규 분포", "조건부 분포도 정규 분포"],
            "응용": ["베이지안 추론", "결측치 처리"],
            "계산 방법": ["행렬 분할", "슈어 보수"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00067_marginals_and_conditionals_of_an_mvn.md", "r", encoding="utf-8").read()
    },
    {
        "name": "선형 가우스 체계",
        "category": "확률론 및 통계학 개념",
        "properties": {
            "정의": "입력과 출력이 선형 관계이고 노이즈가 가우시안인 시스템",
            "구성 요소": ["입력 변수", "출력 변수", "가우시안 노이즈"],
            "특징": ["조건부 분포가 가우시안", "베이지안 추론 용이"],
            "응용": ["선형 회귀", "칼만 필터"],
            "한계": ["비선형 관계 모델링 어려움"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00068_linear_gaussian_systems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스를 위한 베이즈 규칙",
        "category": "확률론 및 통계학 개념",
        "properties": {
            "정의": "가우시안 분포를 따르는 확률 변수에 대한 베이즈 정리의 적용",
            "특징": ["사후 분포도 가우시안", "공액 사전 분포"],
            "응용": ["칼만 필터", "가우시안 프로세스 회귀"],
            "관련_개념": ["베이즈 정리", "가우시안 분포", "최대 사후 확률 추정"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00069_bayes_rule_for_gaussians.md", "r", encoding="utf-8").read()
    },
    {
        "name": "지수족",
        "category": "확률론 개념",
        "properties": {
            "정의": "특정 형태의 확률 밀도 함수를 가진 분포들의 집합",
            "특징": ["충분 통계량 존재", "최대 엔트로피 성질"],
            "예시": ["정규 분포", "베르누이 분포", "감마 분포"],
            "응용": ["일반화 선형 모델", "변분 추론"],
            "장점": ["수학적 편의성", "자연 매개변수의 존재"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00070_the_exponential_family.md", "r", encoding="utf-8").read()
    },
    {
        "name": "로그 분할 함수는 누율 생성 함수다",
        "category": "확률론 및 통계학 개념",
        "properties": {
            "정의": "지수족 분포의 로그 분할 함수와 누율 생성 함수의 관계",
            "의미": "로그 분할 함수의 미분으로 모든 누율을 얻을 수 있음",
            "응용": ["모수 추정", "분포의 특성 분석"],
            "관련_개념": ["지수족", "누율", "충분 통계량"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00071_log_partition_function_is_cumulant_generating_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "지수족의 최대 엔트로피 미분",
        "category": "확률론 및 통계학 개념",
        "properties": {
            "정의": "지수족 분포가 최대 엔트로피 원리를 만족함을 보이는 과정",
            "주요_내용": ["라그랑주 승수법 사용", "KL 발산 최소화"],
            "의의": "지수족 분포의 이론적 근거 제공",
            "응용": ["통계적 모델링", "정보 이론"],
            "관련_개념": ["최대 엔트로피 원리", "지수족", "쿨백-라이블러 발산"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00072_maximum_entropy_derivation_of_the_exponential_family.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스 혼합 모델",
        "category": "확률론 및 머신러닝 모델",
        "properties": {
            "정의": "여러 가우스 분포의 가중 합으로 복잡한 분포를 모델링하는 방법",
            "구성요소": ["가우스 분포", "혼합 가중치"],
            "학습 방법": "EM 알고리즘",
            "응용": ["클러스터링", "밀도 추정", "이상치 탐지"],
            "장단점": ["유연한 모델링", "해석 가능성", "로컬 최적해 문제", "성분 수 결정의 어려움"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00073_gaussian_mixture_models.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베르누이 혼합 모델",
        "category": "확률론 및 머신러닝 모델",
        "properties": {
            "정의": "여러 베르누이 분포의 가중 합으로 이진 데이터를 모델링하는 방법",
            "구성요소": ["베르누이 분포", "혼합 가중치"],
            "학습 방법": "EM 알고리즘",
            "응용": ["문서 분류", "이미지 분할", "유전자 발현 분석"],
            "특징": ["이진 데이터에 특화", "희소성 처리 가능"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00074_bernoulli_mixture_models.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률적 그래프 모델",
        "category": "확률론 및 머신러닝 모델",
        "properties": {
            "정의": "확률 변수 간의 의존성을 그래프로 표현한 모델",
            "종류": ["베이지안 네트워크", "마르코프 랜덤 필드", "조건부 랜덤 필드"],
            "장점": ["복잡한 의존성 표현", "효율적인 추론", "도메인 지식 통합"],
            "응용": ["자연어 처리", "컴퓨터 비전", "생물정보학"],
            "주요 작업": ["구조 학습", "매개변수 학습", "확률적 추론"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00075_probabilistic_graphical_models.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률적 그래프 모델 추론",
        "category": "확률론 및 머신러닝 기법",
        "properties": {
            "정의": "확률적 그래프 모델에서 원하는 확률을 계산하는 과정",
            "방법": ["정확한 추론", "근사 추론"],
            "알고리즘": ["변수 소거법", "신뢰 전파", "MCMC", "변분 추론"],
            "과제": ["주변화", "MAP 추정", "조건부 확률 계산"],
            "응용": ["의사결정 지원", "이상 탐지", "예측 모델링"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00076_pgm_inference.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률적 그래프 모델 학습",
        "category": "확률론 및 머신러닝 기법",
        "properties": {
            "정의": "데이터로부터 확률적 그래프 모델의 구조와 매개변수를 학습하는 과정",
            "구성요소": ["구조 학습", "매개변수 학습"],
            "방법": ["최대 우도 추정", "베이지안 학습", "EM 알고리즘"],
            "과제": ["과적합 방지", "결측 데이터 처리", "계산 복잡성 관리"],
            "응용": ["인과관계 발견", "시계열 예측", "추천 시스템"]
        },
        "markdown_content": open("Documents/PML1/03_probability_multivariate_models/00077_pgm_learning.md", "r", encoding="utf-8").read()
    }
]

# created_nodes = []
# for node in nodes:
#     try:
#         result = manager.add_node(**node)
#         if result:
#             created_nodes.append(result)
#             print(f"노드 생성 성공: {result['name']}")
#         else:
#             print(f"노드 생성 실패: {node['name']}")
#     except Exception as e:
#         print(f"노드 '{node['name']}' 생성 중 오류 발생: {str(e)}")

# for idx in range(19, 58):
#     node = manager.get_node(idx)
#     created_nodes.append(node)
# print(created_nodes)

# 엣지 생성
edges = [
    {"source_name": "확률 변수", "target_name": "여러 확률 변수의 결합 분포", "relationship_type": "확장_개념"},
    {"source_name": "여러 확률 변수의 결합 분포", "target_name": "공분산", "relationship_type": "관련_개념"},
    {"source_name": "공분산", "target_name": "상관", "relationship_type": "관련_개념"},
    {"source_name": "상관", "target_name": "무상관은 독립을 뜻하지 않는다", "relationship_type": "주의_사항"},
    {"source_name": "상관", "target_name": "상관성은 인과성을 뜻하지 않는다", "relationship_type": "주의_사항"},
    {"source_name": "상관", "target_name": "심슨의 역설", "relationship_type": "관련_현상"},
    {"source_name": "여러 확률 변수의 결합 분포", "target_name": "다변량 가우스(정규) 분포", "relationship_type": "특수_경우"},
    {"source_name": "다변량 가우스(정규) 분포", "target_name": "마할라노비스 거리", "relationship_type": "관련_개념"},
    {"source_name": "다변량 가우스(정규) 분포", "target_name": "다변량 정규 분포(MVN)의 주변 및 조건부 분포", "relationship_type": "특성"},
    {"source_name": "다변량 가우스(정규) 분포", "target_name": "선형 가우스 체계", "relationship_type": "응용"},
    {"source_name": "베이즈 규칙", "target_name": "가우스를 위한 베이즈 규칙", "relationship_type": "특수_경우"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "다변량 가우스(정규) 분포", "relationship_type": "확장"},
    {"source_name": "확률 변수", "target_name": "지수족", "relationship_type": "분포_집합"},
    {"source_name": "지수족", "target_name": "로그 분할 함수는 누율 생성 함수다", "relationship_type": "특성"},
    {"source_name": "머신러닝", "target_name": "여러 확률 변수의 결합 분포", "relationship_type": "기반_이론"},
    {"source_name": "머신러닝", "target_name": "공분산", "relationship_type": "사용_개념"},
    {"source_name": "머신러닝", "target_name": "상관", "relationship_type": "사용_개념"},
    {"source_name": "데이터", "target_name": "상관성은 인과성을 뜻하지 않는다", "relationship_type": "분석_주의사항"},
    {"source_name": "머신러닝", "target_name": "가우스를 위한 베이즈 규칙", "relationship_type": "사용_기법"},
    {"source_name": "머신러닝", "target_name": "지수족", "relationship_type": "사용_모델"},
    {"source_name": "지수족", "target_name": "지수족의 최대 엔트로피 미분", "relationship_type": "이론적_근거"},
    {"source_name": "다변량 가우스(정규) 분포", "target_name": "가우스 혼합 모델", "relationship_type": "기반_모델"},
    {"source_name": "베르누이 분포", "target_name": "베르누이 혼합 모델", "relationship_type": "기반_모델"},
    {"source_name": "확률 변수", "target_name": "확률적 그래프 모델", "relationship_type": "모델링_대상"},
    {"source_name": "확률적 그래프 모델", "target_name": "확률적 그래프 모델 추론", "relationship_type": "관련_작업"},
    {"source_name": "확률적 그래프 모델", "target_name": "확률적 그래프 모델 학습", "relationship_type": "관련_작업"}
]

# created_edges = []
# for edge in edges:
#     source_id = manager.search_nodes(edge['source_name'])[0]['id']
#     target_id = manager.search_nodes(edge['target_name'])[0]['id']
#     result = manager.add_edge(source_id, target_id, edge['relationship_type'])
#     if result:
#         created_edges.append(result)
#         print(f"엣지 생성 성공: {edge['source_name'], edge['target_name'], edge['relationship_type']}")
#     else:
#         print(f"엣지 생성 실패: {edge['source_name'], edge['target_name'], edge['relationship_type']}")

# 기존 파일 읽기
# if os.path.exists("knowledge_graph.json"):
#     with open("knowledge_graph.json", "r", encoding="utf-8") as f:
#         existing_data = json.load(f)
# else:
#     existing_data = {"nodes": [], "edges": []}

# 새로운 노드와 엣지 추가
# existing_data["nodes"].extend(created_nodes)
# existing_data["edges"].extend(created_edges)

# # 중복 제거 (옵션)
# # existing_data["nodes"] = list({node["id"]: node for node in existing_data["nodes"]}.values())
# # existing_data["edges"] = list({(edge["source_id"], edge["target_id"]): edge for edge in existing_data["edges"]}.values())

# 파일에 저장
# with open("knowledge_graph.json", "w", encoding="utf-8") as f:
#     json.dump(existing_data, f, ensure_ascii=False, indent=2)

# print("지식그래프가 knowledge_graph.json 파일에 추가되었습니다.")



def update_knowledge_graph(nodes, edges):
    # 기존 knowledge_graph.json 파일 읽기
    if os.path.exists("knowledge_graph.json"):
        with open("knowledge_graph.json", "r", encoding="utf-8") as f:
            knowledge_graph = json.load(f)
    else:
        knowledge_graph = {"nodes": [], "edges": []}

    # 노드 ID 매핑 생성
    node_id_mapping = {node["name"]: node["id"] for node in knowledge_graph["nodes"]}
    max_node_id = max(node_id_mapping.values()) if node_id_mapping else 0

    # 새로운 노드 변환 및 추가
    for node in nodes:
        if node["name"] not in node_id_mapping:
            max_node_id += 1
            new_node = {
                "id": max_node_id,
                "name": node["name"],
                "category": node["category"],
                "properties": node["properties"]
            }
            knowledge_graph["nodes"].append(new_node)
            node_id_mapping[node["name"]] = max_node_id

    # 새로운 엣지 변환 및 추가
    existing_edges = {(edge["source_id"], edge["target_id"], edge["relationship_type"]) for edge in knowledge_graph["edges"]}
    for edge in edges:
        source_id = node_id_mapping.get(edge["source_name"])
        target_id = node_id_mapping.get(edge["target_name"])
        if source_id and target_id:
            edge_tuple = (source_id, target_id, edge["relationship_type"])
            if edge_tuple not in existing_edges:
                new_edge = {
                    "source": source_id,
                    "target": target_id,
                    "type": edge["relationship_type"]
                }
                knowledge_graph["edges"].append(new_edge)
                existing_edges.add(edge_tuple)

    # 업데이트된 knowledge_graph를 json 파일로 저장
    with open("knowledge_graph.json", "w", encoding="utf-8") as f:
        json.dump(knowledge_graph, f, ensure_ascii=False, indent=2)

    print("knowledge_graph.json 파일이 성공적으로 업데이트되었습니다.")

# 함수 사용 예시
update_knowledge_graph(nodes, edges)