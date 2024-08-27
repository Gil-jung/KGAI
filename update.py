from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "베이즈 결정 이론",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00105_bayesian_decision_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 결정 이론의 분류 문제",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00106_classification_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "ROC 곡선",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00107_roc_curves.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정밀도-재현율 곡선",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00108_precision_recall_curves.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 결정 이론의 회귀 문제",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00109_regression_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률적 예측 문제",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00110_probabilistic_prediction_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "올바른 모델 선택",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00111_right_model_selection.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 가설 검정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00112_bayesian_hypothesis_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 모델 선택",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00113_bayesian_model_selection.md", "r", encoding="utf-8").read()
    },
    {
        "name": "오컴의 면도날",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00114_occam_razor.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증과 주변 가능도 사이의 관계",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00115_connection_between_cross_validation_and_marginal_likelihood.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정보 기준",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00116_information_criteria.md", "r", encoding="utf-8").read()
    },
    {
        "name": "효과 크기에 대한 사후 추론 및 베이즈 유의도 검정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00117_posteria_inference_and_bayes_significance_testing_for_effect_size.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 결정 이론",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00118_frequentist_decision_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "추정량의 위험 계산하기",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00119_computing_the_risk_of_an_estimator.md", "r", encoding="utf-8").read()
    },
    {
        "name": "일치추정량",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00120_consistent_estimators.md", "r", encoding="utf-8").read()
    },
    {
        "name": "허용 가능 추정량",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00121_admissible_estimators.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 위험",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00122_empirical_risk.md", "r", encoding="utf-8").read()
    },
    {
        "name": "구조적 위험",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00123_structural_risk.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00124_cross_validation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "통계적 학습론",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00125_statistical_learning_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 가설 검정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00126_frequentist_hypothesis_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가능도비 검정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00127_likelihood_ratio_test.md", "r", encoding="utf-8").read()
    },
    {
        "name": "귀무가설 유의도 검정",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00128_null_hypothesis_significance_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "p-값",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00129_p_values.md", "r", encoding="utf-8").read()
    },
    {
        "name": "p-값이 유해하다고 간주되는 이유",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00130_p_value_considered_harmful.md", "r", encoding="utf-8").read()
    },
    {
        "name": "왜 모두가 베이즈적이지 않은가?",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00131_why_isn_t_everyone_a_bayesian.md", "r", encoding="utf-8").read()
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
    # {"source_name": "통계학", "target_name": "최대 가능도 추정", "relationship_type": "포함"},
    # {"source_name": "최대 가능도 추정", "target_name": "최대 가능도 추정의 정당화", "relationship_type": "관련_개념"},
    # {"source_name": "머신러닝", "target_name": "경험적 위험 최소화", "relationship_type": "학습_원리"},
    # {"source_name": "경험적 위험 최소화", "target_name": "대리 손실", "relationship_type": "관련_기법"},
    # {"source_name": "통계학", "target_name": "적률법", "relationship_type": "포함"},
    # {"source_name": "머신러닝", "target_name": "온라인 (재귀) 추정", "relationship_type": "학습_방법"},
    # {"source_name": "머신러닝", "target_name": "정칙화", "relationship_type": "기법"},
    # {"source_name": "정칙화", "target_name": "검증 집합을 사용해 정칙자 고르기", "relationship_type": "최적화_방법"},
    # {"source_name": "머신러닝", "target_name": "교차 검증", "relationship_type": "평가_기법"},
    # {"source_name": "머신러닝", "target_name": "조기 중단", "relationship_type": "훈련_기법"},
    # {"source_name": "머신러닝", "target_name": "더 많은 데이터 사용하기", "relationship_type": "성능_향상_전략"},
    # {"source_name": "통계학", "target_name": "베이즈 통계학", "relationship_type": "분야"},
    # {"source_name": "베이즈 통계학", "target_name": "켤레 사전 분포", "relationship_type": "개념"},
    # {"source_name": "켤레 사전 분포", "target_name": "베타-이항 모델", "relationship_type": "예시"},
    # {"source_name": "켤레 사전 분포", "target_name": "디리클레-다항 모델", "relationship_type": "예시"},
    # {"source_name": "켤레 사전 분포", "target_name": "가우스-가우스 모델", "relationship_type": "예시"},
    # {"source_name": "베이즈 통계학", "target_name": "켤레 사전 분포를 넘어서", "relationship_type": "고급_주제"},
    # {"source_name": "베이즈 통계학", "target_name": "신용 구간", "relationship_type": "추론_방법"},
    # {"source_name": "머신러닝", "target_name": "베이즈 머신러닝", "relationship_type": "접근법"},
    # {"source_name": "베이즈 머신러닝", "target_name": "베이즈 머신러닝의 연산적 이슈", "relationship_type": "구현_문제"},
    # {"source_name": "통계학", "target_name": "빈도주의 통계학", "relationship_type": "패러다임"},
    # {"source_name": "빈도주의 통계학", "target_name": "표본 분포", "relationship_type": "핵심_개념"},
    # {"source_name": "최대 가능도 추정", "target_name": "MLE의 표본 분포의 가우스 근사", "relationship_type": "근사_방법"},
    # {"source_name": "통계학", "target_name": "임의 추정량의 표본 분포의 부트스트랩 근사", "relationship_type": "추정_기법"},
    # {"source_name": "빈도주의 통계학", "target_name": "신뢰 구간", "relationship_type": "추정_방법"},
    # {"source_name": "신뢰 구간", "target_name": "주의: 신뢰 구간은 신용할 만하지 않다", "relationship_type": "해석_주의사항"},
    # {"source_name": "머신러닝", "target_name": "편향-분산 트레이드오프", "relationship_type": "핵심_개념"},
    # {"source_name": "베이즈 통계학", "target_name": "빈도주의 통계학", "relationship_type": "대비되는_접근"},
    # {"source_name": "정칙화", "target_name": "편향-분산 트레이드오프", "relationship_type": "관련_개념"},
    # {"source_name": "교차 검증", "target_name": "검증 집합을 사용해 정칙자 고르기", "relationship_type": "응용"}
]

created_edges = []
for edge in edges:
    source_id = manager.search_nodes(edge['source_name'])[0]['id']
    target_id = manager.search_nodes(edge['target_name'])[0]['id']
    result = manager.add_edge(source_id, target_id, edge['relationship_type'])
    if result:
        created_edges.append(result)
        print(f"엣지 생성 성공: {edge['source_name'], edge['target_name'], edge['relationship_type']}")
    else:
        print(f"엣지 생성 실패: {edge['source_name'], edge['target_name'], edge['relationship_type']}")


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
                    "source_id": source_id,
                    "target_id": target_id,
                    "relationship_type": edge["relationship_type"]
                }
                knowledge_graph["edges"].append(new_edge)
                existing_edges.add(edge_tuple)

    # 업데이트된 knowledge_graph를 json 파일로 저장
    with open("knowledge_graph.json", "w", encoding="utf-8") as f:
        json.dump(knowledge_graph, f, ensure_ascii=False, indent=2)

    print("knowledge_graph.json 파일이 성공적으로 업데이트되었습니다.")

# 함수 사용 예시
update_knowledge_graph(nodes, edges)