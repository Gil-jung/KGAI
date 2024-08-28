from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "정보의 불확실성 또는 무질서도 측정",
            "특징": ["비음수", "가법성"],
            "응용": ["정보 압축", "통계 물리학"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00132_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산 확률 변수의 엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "이산 확률 분포의 평균 정보량",
            "수식": "H(X) = -Σ p(x) log p(x)",
            "특징": ["0과 log(n) 사이의 값", "균등 분포에서 최대"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00133_entropy_for_discrete_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "두 확률 분포 간의 차이 측정",
            "수식": "H(p,q) = -Σ p(x) log q(x)",
            "응용": ["기계학습 손실 함수", "모델 평가"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00134_cross_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "결합 엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "두 개 이상의 확률 변수의 총 불확실성",
            "특징": ["개별 엔트로피의 합보다 작거나 같음"],
            "응용": ["다변량 분석", "정보 이론적 의존성 측정"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00135_joint_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조건부 엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "한 변수가 주어졌을 때 다른 변수의 불확실성",
            "특징": ["0보다 크거나 같음", "독립일 때 최대"],
            "응용": ["특징 선택", "의사결정 트리"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00136_conditional_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "퍼플렉서티",
        "category": "정보이론",
        "properties": {
            "정의": "확률 모델의 예측 성능 측정",
            "수식": "2^H(p)",
            "응용": ["언어 모델 평가", "텍스트 생성"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00137_perplexity.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속 확률 변수를 위한 미분 엔트로피",
        "category": "정보이론",
        "properties": {
            "정의": "연속 확률 변수의 불확실성 측정",
            "특징": ["이산 엔트로피의 연속 버전", "음수 값 가능"],
            "응용": ["신호 처리", "통계 물리학"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00138_differential_entropy_for_continuous_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상대 엔트로피 (KL 발산)",
        "category": "정보이론",
        "properties": {
            "정의": "두 확률 분포 간의 차이 측정",
            "특징": ["비대칭적", "항상 비음수"],
            "응용": ["모델 선택", "정보 압축"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00139_relative_entropy.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL 발산의 해석",
        "category": "정보이론",
        "properties": {
            "의미": "정보 이득 또는 정보 손실",
            "관점": ["베이지안 추론", "정보 코딩"],
            "한계": ["비대칭성", "삼각 부등식 불만족"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00140_kl_divergence_interpretation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL의 비음성",
        "category": "정보이론",
        "properties": {
            "의미": "KL 발산은 항상 0 이상",
            "증명": "젠센 부등식 사용",
            "중요성": ["분포 차이의 하한", "모델 평가 기준"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00141_non_negativity_of_kl.md", "r", encoding="utf-8").read()
    },
    {
        "name": "KL 발산과 최대우도추정법 (MLE)",
        "category": "통계학",
        "properties": {
            "관계": "MLE는 KL 발산 최소화와 동등",
            "의의": "통계적 추론의 정보이론적 해석",
            "응용": ["모델 파라미터 추정", "분포 근사"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00142_kl_divergence_and_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "전진 KL 대 후진 KL",
        "category": "정보이론",
        "properties": {
            "차이점": ["평균 계산 순서", "근사 특성"],
            "전진 KL": "평균-탐색 행동",
            "후진 KL": "모드-탐색 행동"
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00143_forward_vs_reverse_kl.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상호 정보",
        "category": "정보이론",
        "properties": {
            "정의": "두 변수 간의 상호 의존성 측정",
            "특징": ["대칭적", "비음수"],
            "응용": ["특징 선택", "인과관계 분석"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00144_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "상호 정보의 해석",
        "category": "정보이론",
        "properties": {
            "의미": "한 변수가 다른 변수에 대해 제공하는 정보량",
            "관점": ["불확실성 감소", "의존성 측정"],
            "한계": ["비선형 관계 감지", "인과관계 미표현"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00145_mutual_information_interpretation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조건부 상호 정보",
        "category": "정보이론",
        "properties": {
            "정의": "주어진 조건 하에서의 상호 정보",
            "특징": ["3개 이상 변수 간 관계 분석"],
            "응용": ["특징 선택", "인과 추론"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00146_conditional_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "일반화 상관계수로서의 MI",
        "category": "정보이론",
        "properties": {
            "의의": "비선형 관계 측정 가능",
            "장점": ["분포 가정 불필요", "척도 불변성"],
            "한계": "해석의 어려움"
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00147_mi_as_a_generalized_correlation_coefficient.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정규화 상호 정보",
        "category": "정보이론",
        "properties": {
            "목적": "상호 정보의 척도 표준화",
            "방법": ["엔트로피로 나누기", "최대값으로 정규화"],
            "응용": ["클러스터링", "특징 선택"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00148_normalized_mutual_information.md", "r", encoding="utf-8").read()
    },
    {
        "name": "최대 정보 계수",
        "category": "정보이론",
        "properties": {
            "정의": "비선형 관계의 강도 측정",
            "특징": ["0과 1 사이 값", "모든 함수적 관계 감지"],
            "응용": ["데이터 탐색", "변수 간 관계 분석"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00149_maximal_information_coefficient.md", "r", encoding="utf-8").read()
    },
    {
        "name": "데이터 처리 부등식",
        "category": "정보이론",
        "properties": {
            "정의": "데이터 처리로 정보 증가 불가",
            "의의": "정보 손실의 하한 제공",
            "응용": ["기계학습 알고리즘 설계", "정보 압축"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00150_data_processing_inequality.md", "r", encoding="utf-8").read()
    },
    {
        "name": "충분 통계량",
        "category": "통계학",
        "properties": {
            "정의": "모든 관련 정보를 포함하는 통계량",
            "특징": ["차원 축소", "정보 보존"],
            "응용": ["효율적 추정", "데이터 압축"]
        },
        "markdown_content": open("Documents/PML1/06_information_theory/00151_sufficient_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "파노의 부등식",
        "category": "정보이론",
        "properties": {
            "정의": "오류 확률의 하한 제공",
            "의의": "통신 시스템의 성능 한계 설정",
            "응용": ["코딩 이론", "신호 처리"]
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
    {"source_name": "엔트로피", "target_name": "이산 확률 변수의 엔트로피", "relationship_type": "구체화"},
    {"source_name": "엔트로피", "target_name": "연속 확률 변수를 위한 미분 엔트로피", "relationship_type": "구체화"},
    {"source_name": "엔트로피", "target_name": "교차 엔트로피", "relationship_type": "관련_개념"},
    {"source_name": "엔트로피", "target_name": "결합 엔트로피", "relationship_type": "확장"},
    {"source_name": "엔트로피", "target_name": "조건부 엔트로피", "relationship_type": "확장"},
    {"source_name": "엔트로피", "target_name": "퍼플렉서티", "relationship_type": "응용"},
    {"source_name": "엔트로피", "target_name": "상대 엔트로피 (KL 발산)", "relationship_type": "관련_개념"},
    {"source_name": "교차 엔트로피", "target_name": "상대 엔트로피 (KL 발산)", "relationship_type": "관련_개념"},
    {"source_name": "조건부 엔트로피", "target_name": "상호 정보", "relationship_type": "관련_개념"},
    {"source_name": "상대 엔트로피 (KL 발산)", "target_name": "KL 발산의 해석", "relationship_type": "해석"},
    {"source_name": "상대 엔트로피 (KL 발산)", "target_name": "KL의 비음성", "relationship_type": "특성"},
    {"source_name": "상대 엔트로피 (KL 발산)", "target_name": "KL 발산과 최대우도추정법 (MLE)", "relationship_type": "응용"},
    {"source_name": "상대 엔트로피 (KL 발산)", "target_name": "전진 KL 대 후진 KL", "relationship_type": "변형"},
    {"source_name": "상호 정보", "target_name": "상호 정보의 해석", "relationship_type": "해석"},
    {"source_name": "상호 정보", "target_name": "조건부 상호 정보", "relationship_type": "확장"},
    {"source_name": "상호 정보", "target_name": "일반화 상관계수로서의 MI", "relationship_type": "응용"},
    {"source_name": "상호 정보", "target_name": "정규화 상호 정보", "relationship_type": "변형"},
    {"source_name": "상호 정보", "target_name": "최대 정보 계수", "relationship_type": "관련_개념"}
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