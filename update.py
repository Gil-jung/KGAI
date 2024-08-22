from knowledge_graph_manager import KnowledgeGraphManager
import json

manager = KnowledgeGraphManager()

# 노드 생성
nodes = [
    {
        "name": "확률",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00020_probability.md", "r", encoding="utf-8").read()
    },
    {
        "name": "불확실성의 형태",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00021_types_of_uncertainty.md", "r", encoding="utf-8").read()
    },
    {
        "name": "논리의 확장으로서의 확률",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00022_probability_as_an_extension_of_logic.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 변수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00023_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산 확률 변수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00024_discrete_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속 확률 변수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00025_continuous_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "관련된 확률 변수의 집합",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00026_sets_of_related_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "독립과 조건부 독립",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00027_independence_and_conditional_independence.md", "r", encoding="utf-8").read()
    },
    {
        "name": "분포의 적률",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00028_moments_of_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "요약 통계량의 한계",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00029_limitations_of_summary_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 규칙",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00030_bayes_rule.md", "r", encoding="utf-8").read()
    },
    {
        "name": "역 문제",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00031_inverse_problem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베르누이 분포와 이항 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00032_bernoulli_and_binomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "시그모이드(로지스틱) 함수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00033_sigmoid_logistic_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이항 로지스틱 회귀",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00034_binomial_logistic_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "범주형 및 다항 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00035_categorical_and_multinomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "소프트맥스 함수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00036_softmax_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "다중 클래스 로지스틱 회귀",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00037_multiclass_logistic_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "Log-Sum-Exp 트릭",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00038_log_sum_exp_trick.md", "r", encoding="utf-8").read()
    },
    {
        "name": "일변량 가우스(정규) 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00039_univariate_gaussian_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "누적 분포 함수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00040_cumulative_distribution_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 밀도 함수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00041_probability_density_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스 분포에서의 회귀",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00042_regression_for_gaussian.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스 분포가 널리 쓰이는 이유",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00043_why_is_the_gaussian_distribution_so_widely_used.md", "r", encoding="utf-8").read()
    },
    {
        "name": "디랙 델타 함수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00044_dirac_delta_function_as_a_limiting_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "스튜던트 t 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00045_student_t_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "코시 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00046_cauchy_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "라플라스 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00047_laplace_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베타 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00048_beta_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "감마 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00049_gamma_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 분포",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00050_empirical_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 변수의 변환",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00051_transformations_of_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산형 확률 변수의 변환",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00052_discrete_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속형 확률 변수의 변환",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00053_continuous_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가역 변환 (전단사)",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00054_invertible_transformations_bijections.md", "r", encoding="utf-8").read()
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
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[1]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[2]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[3]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[1]['id'], "target_id": created_nodes[4]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[1]['id'], "target_id": created_nodes[5]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[2]['id'], "target_id": created_nodes[8]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[2]['id'], "target_id": created_nodes[9]['id'], "relationship_type": "포함"},
    # {"source_id": created_nodes[2]['id'], "target_id": created_nodes[10]['id'], "relationship_type": "관련"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[6]['id'], "relationship_type": "관련_개념"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[7]['id'], "relationship_type": "관련_개념"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[12]['id'], "relationship_type": "사용"},
    # {"source_id": created_nodes[12]['id'], "target_id": created_nodes[13]['id'], "relationship_type": "예시"},
    # {"source_id": created_nodes[12]['id'], "target_id": created_nodes[14]['id'], "relationship_type": "예시"},
    # {"source_id": created_nodes[12]['id'], "target_id": created_nodes[15]['id'], "relationship_type": "전처리_기법"},
    # {"source_id": created_nodes[12]['id'], "target_id": created_nodes[16]['id'], "relationship_type": "전처리_기법"},
    # {"source_id": created_nodes[12]['id'], "target_id": created_nodes[17]['id'], "relationship_type": "전처리_기법"},
    # {"source_id": created_nodes[0]['id'], "target_id": created_nodes[18]['id'], "relationship_type": "관련"},
    # {"source_id": created_nodes[2]['id'], "target_id": created_nodes[11]['id'], "relationship_type": "평가_방법"}
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