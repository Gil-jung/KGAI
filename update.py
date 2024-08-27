from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "베이즈 결정 이론",
        "category": "통계학",
        "properties": {
            "핵심_개념": ["사후 확률", "손실 함수", "위험 최소화"],
            "응용": ["분류", "회귀", "예측"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00105_bayesian_decision_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 결정 이론의 분류 문제",
        "category": "머신러닝",
        "properties": {
            "관련_개념": ["결정 경계", "오분류 비용"],
            "기술": ["최대 사후 확률 분류기"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00106_classification_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "ROC 곡선",
        "category": "성능 평가",
        "properties": {
            "이름": "Receiver Operating Characteristic",
            "평가": ["참 양성률", "거짓 양성률"],
            "응용": ["이진 분류기 평가"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00107_roc_curves.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정밀도-재현율 곡선",
        "category": "성능 평가",
        "properties": {
            "평가": ["정밀도", "재현율"],
            "응용": ["불균형 데이터셋 평가"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00108_precision_recall_curves.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 결정 이론의 회귀 문제",
        "category": "머신러닝",
        "properties": {
            "관련_개념": ["제곱 손실 함수", "조건부 기댓값"],
            "기술": ["베이지안 회귀"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00109_regression_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률적 예측 문제",
        "category": "머신러닝",
        "properties": {
            "관련_개념": ["예측 분포", "불확실성 추정"],
            "응용": ["위험 평가", "의사결정 지원"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00110_probabilistic_prediction_problems.md", "r", encoding="utf-8").read()
    },
    {
        "name": "올바른 모델 선택",
        "category": "모델 선택",
        "properties": {
            "기술": ["교차 검증", "정보 기준"],
            "문제": ["과적합", "편향-분산 트레이드오프"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00111_right_model_selection.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 가설 검정",
        "category": "통계학",
        "properties": {
            "핵심_개념": ["베이즈 인자", "사후 확률"],
            "장점": ["불확실성 정량화", "사전 정보 활용"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00112_bayesian_hypothesis_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 모델 선택",
        "category": "모델 선택",
        "properties": {
            "기술": ["주변 가능도", "베이즈 인자"],
            "장점": ["모델 복잡성 자동 조절", "불확실성 정량화"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00113_bayesian_model_selection.md", "r", encoding="utf-8").read()
    },
    {
        "name": "오컴의 면도날",
        "category": "과학 철학",
        "properties": {
            "원칙": "단순한 설명을 선호",
            "응용": ["모델 선택", "과학적 이론 평가"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00114_occam_razor.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증과 주변 가능도 사이의 관계",
        "category": "모델 평가",
        "properties": {
            "관련_개념": ["교차 검증", "주변 가능도"],
            "결과": ["모델 선택 방법의 일관성"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00115_connection_between_cross_validation_and_marginal_likelihood.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정보 기준",
        "category": "모델 선택",
        "properties": {
            "예시": ["AIC", "BIC"],
            "원칙": ["모델 적합도와 복잡성 균형"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00116_information_criteria.md", "r", encoding="utf-8").read()
    },
    {
        "name": "효과 크기에 대한 사후 추론 및 베이즈 유의도 검정",
        "category": "통계학",
        "properties": {
            "기술": ["베이즈 인자", "사후 분포 분석"],
            "장점": ["효과 크기 추정", "불확실성 정량화"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00117_posteria_inference_and_bayes_significance_testing_for_effect_size.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 결정 이론",
        "category": "통계학",
        "properties": {
            "핵심_개념": ["위험 함수", "미니맥스 추정량"],
            "대비": "베이즈 결정 이론"
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00118_frequentist_decision_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "추정량의 위험 계산하기",
        "category": "통계학",
        "properties": {
            "기술": ["몬테카를로 시뮬레이션", "이론적 분석"],
            "응용": ["추정량 성능 평가", "모델 선택"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00119_computing_the_risk_of_an_estimator.md", "r", encoding="utf-8").read()
    },
    {
        "name": "일치추정량",
        "category": "통계학",
        "properties": {
            "정의": "표본 크기 증가에 따른 참값 수렴",
            "예시": ["최대 가능도 추정량", "모멘트 추정량"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00120_consistent_estimators.md", "r", encoding="utf-8").read()
    },
    {
        "name": "허용 가능 추정량",
        "category": "통계학",
        "properties": {
            "정의": "다른 추정량에 의해 지배되지 않음",
            "의미": ["최적성", "효율성"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00121_admissible_estimators.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 위험",
        "category": "머신러닝",
        "properties": {
            "정의": "훈련 데이터에 대한 평균 손실",
            "한계": ["과적합 위험", "일반화 성능 과대평가"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00122_empirical_risk.md", "r", encoding="utf-8").read()
    },
    {
        "name": "구조적 위험",
        "category": "머신러닝",
        "properties": {
            "정의": "경험적 위험과 복잡성 페널티의 합",
            "장점": ["과적합 감소", "일반화 성능 향상"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00123_structural_risk.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증",
        "category": "모델 평가",
        "properties": {
            "기술": ["k-fold", "leave-one-out"],
            "응용": ["모델 선택", "성능 추정"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00124_cross_validation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "통계적 학습론",
        "category": "머신러닝",
        "properties": {
            "핵심_개념": ["VC 차원", "PAC 학습"],
            "목표": ["일반화 오류 분석", "학습 알고리즘 설계"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00125_statistical_learning_theory.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 가설 검정",
        "category": "통계학",
        "properties": {
            "핵심_개념": ["p-값", "유의수준"],
            "한계": ["이진 결정", "효과 크기 무시"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00126_frequentist_hypothesis_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가능도비 검정",
        "category": "통계학",
        "properties": {
            "정의": "두 모델의 가능도 비율 비교",
            "응용": ["모델 선택", "가설 검정"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00127_likelihood_ratio_test.md", "r", encoding="utf-8").read()
    },
    {
        "name": "귀무가설 유의도 검정",
        "category": "통계학",
        "properties": {
            "단계": ["귀무가설 설정", "검정통계량 계산", "p-값 비교"],
            "한계": ["오용 가능성", "효과 크기 무시"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00128_null_hypothesis_significance_testing.md", "r", encoding="utf-8").read()
    },
    {
        "name": "p-값",
        "category": "통계학",
        "properties": {
            "정의": "귀무가설 하에서 관측값 이상의 극단적 결과 확률",
            "오해": ["효과 크기", "가설의 확률"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00129_p_values.md", "r", encoding="utf-8").read()
    },
    {
        "name": "p-값이 유해하다고 간주되는 이유",
        "category": "통계학",
        "properties": {
            "비판": ["오용", "오해", "출판 편향"],
            "대안": ["효과 크기", "신뢰 구간"]
        },
        "markdown_content": open("Documents/PML1/05_decision_theory/00130_p_value_considered_harmful.md", "r", encoding="utf-8").read()
    },
    {
        "name": "왜 모두가 베이즈적이지 않은가?",
        "category": "통계학",
        "properties": {
            "도전": ["계산 복잡성", "사전 분포 선택"],
            "장점": ["불확실성 정량화", "사전 지식 통합"]
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
    {"source_name": "베이즈 결정 이론", "target_name": "베이즈 결정 이론의 분류 문제", "relationship_type": "응용"},
    {"source_name": "베이즈 결정 이론", "target_name": "베이즈 결정 이론의 회귀 문제", "relationship_type": "응용"},
    {"source_name": "베이즈 결정 이론의 분류 문제", "target_name": "ROC 곡선", "relationship_type": "평가_도구"},
    {"source_name": "베이즈 결정 이론의 분류 문제", "target_name": "정밀도-재현율 곡선", "relationship_type": "평가_도구"},
    {"source_name": "베이즈 결정 이론", "target_name": "확률적 예측 문제", "relationship_type": "관련_개념"},
    {"source_name": "베이즈 결정 이론", "target_name": "베이즈 가설 검정", "relationship_type": "관련_기법"},
    {"source_name": "베이즈 모델 선택", "target_name": "오컴의 면도날", "relationship_type": "관련_원리"},
    {"source_name": "베이즈 모델 선택", "target_name": "교차 검증과 주변 가능도 사이의 관계", "relationship_type": "관련_개념"},
    {"source_name": "베이즈 모델 선택", "target_name": "정보 기준", "relationship_type": "관련_기법"}, 
    {"source_name": "베이즈 가설 검정", "target_name": "효과 크기에 대한 사후 추론 및 베이즈 유의도 검정", "relationship_type": "관련_기법"}, 
    {"source_name": "베이즈 결정 이론", "target_name": "빈도주의 결정 이론", "relationship_type": "대비되는_접근"},
    {"source_name": "빈도주의 결정 이론", "target_name": "추정량의 위험 계산하기", "relationship_type": "관련_기법"}, 
    {"source_name": "빈도주의 결정 이론", "target_name": "일치추정량", "relationship_type": "관련_개념"}, 
    {"source_name": "빈도주의 결정 이론", "target_name": "허용 가능 추정량", "relationship_type": "관련_개념"}, 
    {"source_name": "경험적 위험", "target_name": "구조적 위험", "relationship_type": "관련_개념"}, 
    {"source_name": "올바른 모델 선택", "target_name": "교차 검증", "relationship_type": "평가_방법"}, 
    {"source_name": "올바른 모델 선택", "target_name": "통계적 학습론", "relationship_type": "이론적_기반"}, 
    {"source_name": "빈도주의 가설 검정", "target_name": "가능도비 검정", "relationship_type": "검정_방법"}, 
    {"source_name": "빈도주의 가설 검정", "target_name": "귀무가설 유의도 검정", "relationship_type": "검정_방법"}, 
    {"source_name": "귀무가설 유의도 검정", "target_name": "p-값", "relationship_type": "관련_개념"}, 
    {"source_name": "p-값", "target_name": "p-값이 유해하다고 간주되는 이유", "relationship_type": "비판"}, 
    {"source_name": "베이즈 결정 이론", "target_name": "왜 모두가 베이즈적이지 않은가?", "relationship_type": "논의_주제"}
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