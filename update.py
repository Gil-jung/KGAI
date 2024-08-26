from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "최대 가능도 추정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00078_maximum_likelihood_estimation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "최대 가능도 추정의 정당화",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00079_justification_of_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 위험 최소화",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00080_empirical_risk_minimization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "대리 손실",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00081_surrogate_loss.md", "r", encoding="utf-8").read()
    },
    {
        "name": "적률법",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00082_method_of_moments.md", "r", encoding="utf-8").read()
    },
    {
        "name": "온라인 (재귀) 추정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00083_online_estimation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정칙화",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00084_regularization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "검증 집합을 사용해 정칙자 고르기",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00085_picking_the_regularizer_using_a_validation_set.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00086_cross_validation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조기 중단",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00087_early_stopping.md", "r", encoding="utf-8").read()
    },
    {
        "name": "더 많은 데이터 사용하기",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00088_using_more_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 통계학",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00089_bayesian_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "켤레 사전 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00090_conjugate_priors.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베타-이항 모델",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00091_the_beta_binomial_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "디리클레-다항 모델",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00092_the_dirichlet_multinomial_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스-가우스 모델",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00093_the_gaussian_gaussian_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "켤레 사전 분포를 넘어서",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00094_beyond_conjugate_priors.md", "r", encoding="utf-8").read()
    },
    {
        "name": "신용 구간",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00095_credible_intervals.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 머신러닝",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00096_bayesian_machine_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 머신러닝의 연산적 이슈",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00097_computational_issues.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 통계학",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00098_frequentist_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "표본 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00099_sampling_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "MLE의 표본 분포의 가우스 근사",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00100_gaussian_approximation_of_the_sampling_distribution_of_the_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "임의 추정량의 표본 분포의 부트스트랩 근사",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00101_bootstrap_approximation_of_the_sampling_distribution_of_any_estimator.md", "r", encoding="utf-8").read()
    },
    {
        "name": "신뢰 구간",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00102_confidence_intervals.md", "r", encoding="utf-8").read()
    },
    {
        "name": "주의: 신뢰 구간은 신용할 만하지 않다",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00103_caution_confidence_intervals_are_not_credible.md", "r", encoding="utf-8").read()
    },
    {
        "name": "편향-분산 트레이드오프",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/04_statistics/00104_the_bias_variance_tradeoff.md", "r", encoding="utf-8").read()
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
    # {"source_name": "확률 변수", "target_name": "여러 확률 변수의 결합 분포", "relationship_type": "확장_개념"},
    # {"source_name": "여러 확률 변수의 결합 분포", "target_name": "공분산", "relationship_type": "관련_개념"},
    # {"source_name": "공분산", "target_name": "상관", "relationship_type": "관련_개념"},
    # {"source_name": "상관", "target_name": "무상관은 독립을 뜻하지 않는다", "relationship_type": "주의_사항"},
    # {"source_name": "상관", "target_name": "상관성은 인과성을 뜻하지 않는다", "relationship_type": "주의_사항"},
    # {"source_name": "상관", "target_name": "심슨의 역설", "relationship_type": "관련_현상"},
    # {"source_name": "여러 확률 변수의 결합 분포", "target_name": "다변량 가우스(정규) 분포", "relationship_type": "특수_경우"},
    # {"source_name": "다변량 가우스(정규) 분포", "target_name": "마할라노비스 거리", "relationship_type": "관련_개념"},
    # {"source_name": "다변량 가우스(정규) 분포", "target_name": "다변량 정규 분포(MVN)의 주변 및 조건부 분포", "relationship_type": "특성"},
    # {"source_name": "다변량 가우스(정규) 분포", "target_name": "선형 가우스 체계", "relationship_type": "응용"},
    # {"source_name": "베이즈 규칙", "target_name": "가우스를 위한 베이즈 규칙", "relationship_type": "특수_경우"},
    # {"source_name": "일변량 가우스(정규) 분포", "target_name": "다변량 가우스(정규) 분포", "relationship_type": "확장"},
    # {"source_name": "확률 변수", "target_name": "지수족", "relationship_type": "분포_집합"},
    # {"source_name": "지수족", "target_name": "로그 분할 함수는 누율 생성 함수다", "relationship_type": "특성"},
    # {"source_name": "머신러닝", "target_name": "여러 확률 변수의 결합 분포", "relationship_type": "기반_이론"},
    # {"source_name": "머신러닝", "target_name": "공분산", "relationship_type": "사용_개념"},
    # {"source_name": "머신러닝", "target_name": "상관", "relationship_type": "사용_개념"},
    # {"source_name": "데이터", "target_name": "상관성은 인과성을 뜻하지 않는다", "relationship_type": "분석_주의사항"},
    # {"source_name": "머신러닝", "target_name": "가우스를 위한 베이즈 규칙", "relationship_type": "사용_기법"},
    # {"source_name": "머신러닝", "target_name": "지수족", "relationship_type": "사용_모델"},
    # {"source_name": "지수족", "target_name": "지수족의 최대 엔트로피 미분", "relationship_type": "이론적_근거"},
    # {"source_name": "다변량 가우스(정규) 분포", "target_name": "가우스 혼합 모델", "relationship_type": "기반_모델"},
    # {"source_name": "베르누이 분포", "target_name": "베르누이 혼합 모델", "relationship_type": "기반_모델"},
    # {"source_name": "확률 변수", "target_name": "확률적 그래프 모델", "relationship_type": "모델링_대상"},
    # {"source_name": "확률적 그래프 모델", "target_name": "확률적 그래프 모델 추론", "relationship_type": "관련_작업"},
    # {"source_name": "확률적 그래프 모델", "target_name": "확률적 그래프 모델 학습", "relationship_type": "관련_작업"}
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