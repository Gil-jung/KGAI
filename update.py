from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00132_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산 확률 변수의 엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00133_entropy_for_discrete_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00134_cross_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "결합 엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00135_joint_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조건부 엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00136_conditional_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "퍼플렉서티",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00137_perplexity.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속 확률 변수를 위한 미분 엔트로피",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00138_differential_entropy_for_continuous_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상대 엔트로피 (KL 발산)",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00139_relative_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL 발산의 해석",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00140_kl_divergence_interpretation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL의 비음성",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00141_non_negativity_of_kl.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL 발산과 최대우도추정법 (MLE)",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00142_kl_divergence_and_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "전진 KL 대 후진 KL",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00143_forward_vs_reverse_kl.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상호 정보",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00144_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상호 정보의 해석",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00145_mutual_information_interpretation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조건부 상호 정보",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00146_conditional_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "일반화 상관계수로서의 MI",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00147_mi_as_a_generalized_correlation_coefficient.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정규화 상호 정보",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00148_normalized_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "최대 정보 계수",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00149_maximal_information_coefficient.md", "r", encoding="utf-8").read()
    },
    {
        "name": "데이터 처리 부등식",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00150_data_processing_inequality.md", "r", encoding="utf-8").read()
    },
    {
        "name": "충분 통계량",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00151_sufficient_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "파노의 부등식",
        "category": "",
        "properties": {

        },
        "markdown_content": open("Documents/PML1/06_information_theory/00152_fano_inequality.md", "r", encoding="utf-8").read()
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
    # {"source_name": "베이즈 결정 이론", "target_name": "베이즈 결정 이론의 분류 문제", "relationship_type": "응용"},
    # {"source_name": "베이즈 결정 이론", "target_name": "베이즈 결정 이론의 회귀 문제", "relationship_type": "응용"},
    # {"source_name": "베이즈 결정 이론의 분류 문제", "target_name": "ROC 곡선", "relationship_type": "평가_도구"},
    # {"source_name": "베이즈 결정 이론의 분류 문제", "target_name": "정밀도-재현율 곡선", "relationship_type": "평가_도구"},
    # {"source_name": "베이즈 결정 이론", "target_name": "확률적 예측 문제", "relationship_type": "관련_개념"},
    # {"source_name": "베이즈 결정 이론", "target_name": "베이즈 가설 검정", "relationship_type": "관련_기법"},
    # {"source_name": "베이즈 모델 선택", "target_name": "오컴의 면도날", "relationship_type": "관련_원리"},
    # {"source_name": "베이즈 모델 선택", "target_name": "교차 검증과 주변 가능도 사이의 관계", "relationship_type": "관련_개념"},
    # {"source_name": "베이즈 모델 선택", "target_name": "정보 기준", "relationship_type": "관련_기법"}, 
    # {"source_name": "베이즈 가설 검정", "target_name": "효과 크기에 대한 사후 추론 및 베이즈 유의도 검정", "relationship_type": "관련_기법"}, 
    # {"source_name": "베이즈 결정 이론", "target_name": "빈도주의 결정 이론", "relationship_type": "대비되는_접근"},
    # {"source_name": "빈도주의 결정 이론", "target_name": "추정량의 위험 계산하기", "relationship_type": "관련_기법"}, 
    # {"source_name": "빈도주의 결정 이론", "target_name": "일치추정량", "relationship_type": "관련_개념"}, 
    # {"source_name": "빈도주의 결정 이론", "target_name": "허용 가능 추정량", "relationship_type": "관련_개념"}, 
    # {"source_name": "경험적 위험", "target_name": "구조적 위험", "relationship_type": "관련_개념"}, 
    # {"source_name": "올바른 모델 선택", "target_name": "교차 검증", "relationship_type": "평가_방법"}, 
    # {"source_name": "올바른 모델 선택", "target_name": "통계적 학습론", "relationship_type": "이론적_기반"}, 
    # {"source_name": "빈도주의 가설 검정", "target_name": "가능도비 검정", "relationship_type": "검정_방법"}, 
    # {"source_name": "빈도주의 가설 검정", "target_name": "귀무가설 유의도 검정", "relationship_type": "검정_방법"}, 
    # {"source_name": "귀무가설 유의도 검정", "target_name": "p-값", "relationship_type": "관련_개념"}, 
    # {"source_name": "p-값", "target_name": "p-값이 유해하다고 간주되는 이유", "relationship_type": "비판"}, 
    # {"source_name": "베이즈 결정 이론", "target_name": "왜 모두가 베이즈적이지 않은가?", "relationship_type": "논의_주제"}
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