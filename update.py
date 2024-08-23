from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "독립과 조건부 독립",
        "category": "확률론 개념",
        "properties": {
            "독립_정의": "한 사건의 발생이 다른 사건의 확률에 영향을 주지 않음",
            "조건부_독립_정의": "주어진 조건 하에서 두 사건이 독립",
            "특징": ["확률의 곱셈 법칙", "베이즈 정리와의 관계"],
            "응용": ["나이브 베이즈 분류기", "그래프 모델"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00027_independence_and_conditional_independence.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베르누이 분포와 이항 분포",
        "category": "확률 분포",
        "properties": {
            "베르누이_분포_정의": "성공/실패 두 가지 결과만 가능한 단일 시행의 확률 분포",
            "베르누이_분포_매개변수": "성공 확률 p",
            "이항_분포_정의": "n번의 독립적인 베르누이 시행에서 성공 횟수의 확률 분포",
            "이항_분포_매개변수": ["시행 횟수 n", "성공 확률 p"],
            "응용": ["품질 관리", "의학 연구", "선거 예측"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00032_bernoulli_and_binomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "범주형 및 다항 분포",
        "category": "확률 분포",
        "properties": {
            "범주형_분포_정의": "유한한 수의 가능한 결과에 대한 확률 분포",
            "범주형_분포_특징": ["이산적", "상호 배타적 결과"],
            "다항_분포_정의": "여러 범주에 대한 시행 횟수의 결합 분포",
            "다항_분포_매개변수": ["시행 횟수 n", "각 범주의 확률"],
            "응용": ["텍스트 분류", "유전자 발현 분석"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00035_categorical_and_multinomial_distributions.md", "r", encoding="utf-8").read()
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

# for idx in range(19, 58):
#     node = manager.get_node(idx)
#     created_nodes.append(node)
# print(created_nodes)

# 엣지 생성
edges = [
    {"source_name": "머신러닝", "target_name": "확률", "relationship_type": "기반_이론"},
    {"source_name": "확률", "target_name": "불확실성의 형태", "relationship_type": "관련_개념"},
    {"source_name": "확률", "target_name": "논리의 확장으로서의 확률", "relationship_type": "이론적_기반"},
    {"source_name": "베이즈 규칙", "target_name": "확률", "relationship_type": "관련_개념"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "누적 분포 함수", "relationship_type": "관련_개념"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "확률 밀도 함수", "relationship_type": "관련_개념"},
    {"source_name": "확률", "target_name": "확률 변수", "relationship_type": "기본_개념"},
    {"source_name": "확률 변수", "target_name": "이산 확률 변수", "relationship_type": "하위_분류"},
    {"source_name": "확률 변수", "target_name": "연속 확률 변수", "relationship_type": "하위_분류"},
    {"source_name": "확률 변수", "target_name": "관련된 확률 변수의 집합", "relationship_type": "확장_개념"},
    {"source_name": "확률 변수", "target_name": "독립과 조건부 독립", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수", "target_name": "분포의 적률", "relationship_type": "특성"},
    {"source_name": "확률", "target_name": "베이즈 규칙", "relationship_type": "핵심_정리"},
    {"source_name": "베이즈 규칙", "target_name": "역 문제", "relationship_type": "응용"},
    {"source_name": "이산 확률 변수", "target_name": "베르누이 분포와 이항 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "일변량 가우스(정규) 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "스튜던트 t 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "코시 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "라플라스 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "베타 분포", "relationship_type": "예시"},
    {"source_name": "연속 확률 변수", "target_name": "감마 분포", "relationship_type": "예시"},
    {"source_name": "확률 변수", "target_name": "경험적 분포", "relationship_type": "예시"},
    {"source_name": "확률 변수", "target_name": "확률 변수의 변환", "relationship_type": "연산"},
    {"source_name": "확률 변수의 변환", "target_name": "이산형 확률 변수의 변환", "relationship_type": "하위_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "연속형 확률 변수의 변환", "relationship_type": "하위_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "가역 변환 (전단사)", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수", "target_name": "선형 변환의 적률", "relationship_type": "특성"},
    {"source_name": "확률 변수", "target_name": "합성곱 정리", "relationship_type": "관련_개념"},
    {"source_name": "확률", "target_name": "중심 극한 정리", "relationship_type": "핵심_정리"},
    {"source_name": "확률", "target_name": "몬테카를로 근사", "relationship_type": "응용"},
    {"source_name": "불확실성의 형태", "target_name": "확률", "relationship_type": "처리_방법"},
    {"source_name": "논리의 확장으로서의 확률", "target_name": "베이즈 규칙", "relationship_type": "응용"},
    {"source_name": "시그모이드(로지스틱) 함수", "target_name": "이항 로지스틱 회귀", "relationship_type": "사용"},
    {"source_name": "소프트맥스 함수", "target_name": "다중 클래스 로지스틱 회귀", "relationship_type": "사용"},
    {"source_name": "Log-Sum-Exp 트릭", "target_name": "소프트맥스 함수", "relationship_type": "계산_기법"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포에서의 회귀", "relationship_type": "응용"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포가 널리 쓰이는 이유", "relationship_type": "특징"},
    {"source_name": "디랙 델타 함수", "target_name": "확률 밀도 함수", "relationship_type": "극한_경우"},
    {"source_name": "중심 극한 정리", "target_name": "일변량 가우스(정규) 분포", "relationship_type": "이론적_근거"}
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

# 기존 파일 읽기
if os.path.exists("knowledge_graph.json"):
    with open("knowledge_graph.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)
else:
    existing_data = {"nodes": [], "edges": []}

# 새로운 노드와 엣지 추가
existing_data["nodes"].extend(created_nodes)
existing_data["edges"].extend(created_edges)

# # 중복 제거 (옵션)
# # existing_data["nodes"] = list({node["id"]: node for node in existing_data["nodes"]}.values())
# # existing_data["edges"] = list({(edge["source_id"], edge["target_id"]): edge for edge in existing_data["edges"]}.values())

# 파일에 저장
with open("knowledge_graph.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print("지식그래프가 knowledge_graph.json 파일에 추가되었습니다.")