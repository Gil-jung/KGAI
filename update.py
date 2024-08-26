from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

nodes = [
    {
        "name": "최대 가능도 추정",
        "category": "통계학 방법론",
        "properties": {
            "정의": "주어진 데이터에 대해 가능도를 최대화하는 모수를 찾는 방법",
            "주요 개념": ["가능도 함수", "로그 가능도", "최적화"],
            "응용 분야": ["머신러닝", "통계적 추론", "모델 파라미터 추정"],
            "장점": ["일관성", "효율성", "불편성(대표본에서)"],
            "단점": ["과적합 가능성", "계산 복잡성(일부 모델에서)"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00078_maximum_likelihood_estimation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "최대 가능도 추정의 정당화",
        "category": "통계학 이론",
        "properties": {
            "주요 논점": ["일관성", "효율성", "불편성"],
            "관련 개념": ["대수의 법칙", "중심극한정리", "피셔 정보"],
            "의의": "MLE의 이론적 근거와 성질 설명",
            "한계": "소표본에서의 성능 보장 어려움"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00079_justification_for_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 위험 최소화",
        "category": "머신러닝 원리",
        "properties": {
            "정의": "훈련 데이터에 대한 경험적 위험(손실)을 최소화하는 학습 방법",
            "관련 개념": ["손실 함수", "과적합", "일반화"],
            "응용": ["지도학습 알고리즘", "모델 학습"],
            "장단점": ["구현 용이", "다양한 문제에 적용 가능", "과적합 위험", "노이즈에 민감"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00080_empirical_risk_minimization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "대리 손실",
        "category": "머신러닝 기법",
        "properties": {
            "정의": "원래의 손실 함수를 대체하는 최적화하기 쉬운 함수",
            "목적": "계산 효율성 향상, 최적화 용이성",
            "예시": ["힌지 손실", "로지스틱 손실", "지수 손실"],
            "응용": ["서포트 벡터 머신", "로지스틱 회귀", "부스팅 알고리즘"],
            "주의사항": "원래 목적과의 일치성 확인 필요"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00081_surrogate_loss.md", "r", encoding="utf-8").read()
    },
    {
        "name": "적률법",
        "category": "통계학 방법론",
        "properties": {
            "정의": "표본 적률을 이론적 적률과 일치시켜 모수를 추정하는 방법",
            "장점": ["계산 간편", "직관적"],
            "단점": ["효율성 낮음", "고차 적률의 불안정성"],
            "응용": ["간단한 분포 파라미터 추정", "초기값 설정"],
            "관련 개념": ["표본 적률", "모집단 적률", "적률 생성 함수"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00082_the_method_of_moments.md", "r", encoding="utf-8").read()
    },
    {
        "name": "온라인 (재귀) 추정",
        "category": "통계학 및 머신러닝 기법",
        "properties": {
            "정의": "데이터를 순차적으로 처리하며 모델을 업데이트하는 방법",
            "장점": ["메모리 효율성", "실시간 학습 가능", "대규모 데이터셋 처리"],
            "단점": ["지역 최적해에 빠질 가능성", "하이퍼파라미터 민감성"],
            "응용": ["스트리밍 데이터 분석", "강화학습", "시계열 예측"],
            "알고리즘 예시": ["확률적 경사 하강법", "칼만 필터"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00083_online_estimation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "정칙화",
        "category": "머신러닝 기법",
        "properties": {
            "정의": "모델의 복잡성을 제한하여 과적합을 방지하는 기법",
            "목적": ["일반화 성능 향상", "과적합 방지"],
            "방법": ["L1 정칙화(Lasso)", "L2 정칙화(Ridge)", "엘라스틱넷"],
            "응용": ["선형 회귀", "로지스틱 회귀", "신경망"],
            "주의사항": "정칙화 강도의 적절한 선택 필요"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00084_regularization.md", "r", encoding="utf-8").read()
    },
    {
        "name": "검증 집합을 사용해 정칙자 고르기",
        "category": "모델 선택 기법",
        "properties": {
            "목적": "최적의 정칙화 파라미터 선택",
            "방법": ["홀드아웃 검증", "k-겹 교차 검증"],
            "장점": ["과적합 방지", "모델 일반화 성능 향상"],
            "단점": ["계산 비용 증가", "데이터 분할로 인한 정보 손실"],
            "고려사항": ["데이터셋 크기", "모델 복잡도", "계산 자원"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00085_picking_the_regularizer_using_a_validation_set.md", "r", encoding="utf-8").read()
    },
    {
        "name": "교차 검증",
        "category": "모델 평가 기법",
        "properties": {
            "정의": "데이터를 여러 부분집합으로 나누어 모델을 반복적으로 학습 및 평가하는 방법",
            "종류": ["k-겹 교차 검증", "리브 원 아웃", "반복 홀드아웃"],
            "장점": ["편향 감소", "과적합 감지", "작은 데이터셋에 유용"],
            "단점": ["계산 비용 증가", "시간 소요"],
            "응용": ["모델 선택", "하이퍼파라미터 튜닝", "성능 추정"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00086_cross_validation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "조기 중단",
        "category": "모델 훈련 기법",
        "properties": {
            "정의": "검증 오차가 증가하기 시작할 때 모델 훈련을 중단하는 방법",
            "목적": ["과적합 방지", "훈련 시간 단축"],
            "적용 분야": ["신경망", "그래디언트 부스팅"],
            "장점": ["자동 정칙화 효과", "계산 효율성"],
            "주의사항": ["검증 세트 선택", "중단 기준 설정"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00087_early_stopping.md", "r", encoding="utf-8").read()
    },
    {
        "name": "더 많은 데이터 사용하기",
        "category": "머신러닝 전략",
        "properties": {
            "장점": ["모델 성능 향상", "과적합 감소"],
            "고려사항": ["데이터 품질", "레이블링 비용", "계산 자원"],
            "기법": ["데이터 증강", "준지도 학습", "전이 학습"],
            "한계": "데이터 증가에 따른 수확 체감",
            "응용": ["컴퓨터 비전", "자연어 처리", "음성 인식"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00088_using_more_data.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 통계학",
        "category": "통계학 분야",
        "properties": {
            "정의": "사전 확률과 관측 데이터를 결합하여 사후 확률을 추론하는 통계적 접근",
            "주요 개념": ["사전 분포", "우도", "사후 분포", "베이즈 정리"],
            "장점": ["불확실성 정량화", "사전 지식 통합", "작은 표본에서도 유용"],
            "단점": ["계산 복잡성", "사전 분포 선택의 주관성"],
            "응용 분야": ["의사결정 이론", "머신러닝", "예측 모델링"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00089_bayesian_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "켤레 사전 분포",
        "category": "베이지안 통계 개념",
        "properties": {
            "정의": "우도 함수와 결합하여 같은 형태의 사후 분포를 생성하는 사전 분포",
            "장점": ["계산 편의성", "해석 용이성"],
            "예시": ["베타-이항", "디리클레-다항", "정규-정규"],
            "응용": ["베이지안 추론", "순차적 학습"],
            "한계": "복잡한 모델에서의 제한된 적용성"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00090_conjugate_priors.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베타-이항 모델",
        "category": "베이지안 통계 모델",
        "properties": {
            "구성": ["베타 사전 분포", "이항 우도"],
            "용도": "이진 결과의 확률 추정",
            "장점": ["직관적 해석", "순차적 업데이트 용이"],
            "응용": ["A/B 테스팅", "의학적 진단", "마케팅 반응 예측"],
            "관련 개념": ["베타 분포", "이항 분포", "켤레 사전"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00091_the_beta_binomial_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "디리클레-다항 모델",
        "category": "베이지안 통계 모델",
        "properties": {
            "구성": ["디리클레 사전 분포", "다항 우도"],
            "용도": "다중 범주 확률 추정",
            "특징": ["다변량 베타 분포의 일반화", "범주형 데이터 모델링"],
            "응용": ["문서 분류", "유전자 발현 분석", "시장 점유율 예측"],
            "관련 개념": ["디리클레 분포", "다항 분포", "켤레 사전"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00092_the_dirichlet_multinomial_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스-가우스 모델",
        "category": "베이지안 통계 모델",
        "properties": {
            "구성": ["정규 사전 분포", "정규 우도"],
            "용도": "연속 변수의 평균 추정",
            "특징": ["켤레성", "분석적 해 존재"],
            "응용": ["센서 보정", "품질 관리", "금융 시계열 분석"],
            "관련 개념": ["정규 분포", "정밀도(precision)", "베이지안 선형 회귀"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00093_the_gaussian_gaussian_model.md", "r", encoding="utf-8").read()
    },
    {
        "name": "켤레 사전 분포를 넘어서",
        "category": "고급 베이지안 방법론",
        "properties": {
            "목적": "복잡한 모델에 대한 유연한 추론",
            "방법": ["MCMC", "변분 추론", "근사 베이즈 계산"],
            "장점": ["모델 유연성 증가", "복잡한 사전 지식 표현 가능"],
            "단점": ["계산 복잡성 증가", "수렴 문제"],
            "응용": ["계층적 베이지안 모델", "비모수적 베이지안 방법", "베이지안 딥러닝"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00094_beyond_conjugate_priors.md", "r", encoding="utf-8").read()
    },
    {
        "name": "신용 구간",
        "category": "베이지안 추론",
        "properties": {
            "정의": "모수의 참값이 특정 확률로 포함되는 구간",
            "특징": ["사후 분포에 기반", "불확실성 정량화"],
            "종류": ["최고밀도구간(HDI)", "동일꼬리구간(ETI)"],
            "장점": ["직관적 해석", "비대칭 분포에도 적용 가능"],
            "응용": ["모수 추정", "가설 검정", "의사결정 지원"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00095_credible_intervals.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 머신러닝",
        "category": "머신러닝 접근법",
        "properties": {
            "정의": "베이지안 원리를 머신러닝에 적용하는 방법",
            "특징": ["불확실성 모델링", "과적합 방지", "모델 선택 용이"],
            "기법": ["베이지안 신경망", "가우시안 프로세스", "베이지안 최적화"],
            "장점": ["모델 불확실성 추정", "작은 데이터셋에서도 효과적"],
            "단점": ["계산 복잡성", "해석의 어려움"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00096_bayesian_machine_learning.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 머신러닝의 연산적 이슈",
        "category": "머신러닝 구현 문제",
        "properties": {
            "주요 문제": ["고차원 적분", "복잡한 사후 분포"],
            "해결 방법": ["MCMC", "변분 추론", "라플라스 근사"],
            "트레이드오프": ["정확성 vs 계산 효율성", "모델 복잡도 vs 해석 가능성"],
            "최신 기술": ["확률적 변분 추론", "하이브리드 몬테카를로 방법"],
            "응용 분야": ["대규모 데이터 분석", "실시간 의사결정 시스템"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00097_computational_issues.md", "r", encoding="utf-8").read()
    },
    {
        "name": "빈도주의 통계학",
        "category": "통계학 패러다임",
        "properties": {
            "정의": "반복된 표본 추출을 가정한 통계적 추론 방법",
            "주요 개념": ["p-값", "신뢰구간", "가설검정"],
            "장점": ["객관성", "널리 사용됨", "계산 효율성"],
            "단점": ["해석의 어려움", "작은 표본에서의 한계"],
            "비교 대상": "베이지안 통계학"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00098_frequentist_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "표본 분포",
        "category": "통계적 추론 개념",
        "properties": {
            "정의": "통계량의 확률 분포",
            "중요성": ["추정량의 특성 이해", "가설 검정의 기초"],
            "예시": ["표본 평균의 분포", "표본 분산의 분포"],
            "관련 정리": ["중심극한정리", "대수의 법칙"],
            "응용": ["신뢰구간 구성", "검정통계량 도출"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00099_sampling_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "MLE의 표본 분포의 가우스 근사",
        "category": "통계적 추론 기법",
        "properties": {
            "원리": "대표본에서 MLE의 정규 분포 근사",
            "조건": ["충분히 큰 표본 크기", "정규성 가정"],
            "장점": ["간편한 신뢰구간 구성", "가설 검정 용이"],
            "한계": ["소표본에서의 부정확성", "복잡한 모델에서의 제한"],
            "관련 개념": ["피셔 정보", "크래머-라오 하한"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00100_gaussian_approximation_of_the_sampling_distribution_of_the_mle.md", "r", encoding="utf-8").read()
    },
    {
        "name": "임의 추정량의 표본 분포의 부트스트랩 근사",
        "category": "통계적 추론 기법",
        "properties": {
            "원리": "재표본추출을 통한 표본 분포 추정",
            "장점": ["분포 가정 불필요", "복잡한 통계량에 적용 가능"],
            "단점": ["계산 집약적", "극단값에 민감"],
            "변형": ["파라메트릭 부트스트랩", "블록 부트스트랩"],
            "응용": ["신뢰구간 추정", "편향 보정", "모델 불확실성 평가"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00101_bootstrap_approximation_of_the_sampling_distribution_of_any_estimator.md", "r", encoding="utf-8").read()
    },
    {
        "name": "신뢰 구간",
        "category": "통계적 추정 방법",
        "properties": {
            "정의": "모수의 참값을 포함할 것으로 기대되는 구간",
            "해석": "반복된 표본추출에서의 포함 비율",
            "구성 방법": ["정규 근사", "피벗 방법", "부트스트랩"],
            "장점": ["불확실성 정량화", "가설 검정과의 연관성"],
            "주의사항": ["신뢰수준의 의미", "구간 폭과 표본 크기의 관계"]
        },
        "markdown_content": open("Documents/PML1/04_statistics/00102_confidence_intervals.md", "r", encoding="utf-8").read()
    },
    {
        "name": "주의: 신뢰 구간은 신용할 만하지 않다",
        "category": "통계적 해석 주의사항",
        "properties": {
            "문제점": ["해석의 오류", "개별 구간의 불확실성"],
            "오해의 원인": ["용어의 모호성", "빈도주의적 해석의 어려움"],
            "대안": ["베이지안 신용 구간", "예측 구간"],
            "중요성": "통계적 결과의 올바른 해석",
            "교육적 함의": "통계적 추론의 한계 이해"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00103_caution_confidence_intervals_are_not_credible.md", "r", encoding="utf-8").read()
    },
    {
        "name": "편향-분산 트레이드오프",
        "category": "머신러닝 개념",
        "properties": {
            "정의": "모델의 편향과 분산 사이의 균형",
            "편향": "모델의 단순화로 인한 오차",
            "분산": "데이터 변동에 대한 모델의 민감도",
            "트레이드오프": "편향 감소 시 분산 증가, 반대도 성립",
            "최적화 방법": ["정칙화", "모델 복잡도 조절", "앙상블 방법"],
            "응용": "모델 선택 및 하이퍼파라미터 튜닝"
        },
        "markdown_content": open("Documents/PML1/04_statistics/00104_the_bias_variance_tradeoff.md", "r", encoding="utf-8").read()
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
    {"source_name": "통계학", "target_name": "최대 가능도 추정", "relationship_type": "포함"},
    {"source_name": "최대 가능도 추정", "target_name": "최대 가능도 추정의 정당화", "relationship_type": "관련_개념"},
    {"source_name": "머신러닝", "target_name": "경험적 위험 최소화", "relationship_type": "학습_원리"},
    {"source_name": "경험적 위험 최소화", "target_name": "대리 손실", "relationship_type": "관련_기법"},
    {"source_name": "통계학", "target_name": "적률법", "relationship_type": "포함"},
    {"source_name": "머신러닝", "target_name": "온라인 (재귀) 추정", "relationship_type": "학습_방법"},
    {"source_name": "머신러닝", "target_name": "정칙화", "relationship_type": "기법"},
    {"source_name": "정칙화", "target_name": "검증 집합을 사용해 정칙자 고르기", "relationship_type": "최적화_방법"},
    {"source_name": "머신러닝", "target_name": "교차 검증", "relationship_type": "평가_기법"},
    {"source_name": "머신러닝", "target_name": "조기 중단", "relationship_type": "훈련_기법"},
    {"source_name": "머신러닝", "target_name": "더 많은 데이터 사용하기", "relationship_type": "성능_향상_전략"},
    {"source_name": "통계학", "target_name": "베이즈 통계학", "relationship_type": "분야"},
    {"source_name": "베이즈 통계학", "target_name": "켤레 사전 분포", "relationship_type": "개념"},
    {"source_name": "켤레 사전 분포", "target_name": "베타-이항 모델", "relationship_type": "예시"},
    {"source_name": "켤레 사전 분포", "target_name": "디리클레-다항 모델", "relationship_type": "예시"},
    {"source_name": "켤레 사전 분포", "target_name": "가우스-가우스 모델", "relationship_type": "예시"},
    {"source_name": "베이즈 통계학", "target_name": "켤레 사전 분포를 넘어서", "relationship_type": "고급_주제"},
    {"source_name": "베이즈 통계학", "target_name": "신용 구간", "relationship_type": "추론_방법"},
    {"source_name": "머신러닝", "target_name": "베이즈 머신러닝", "relationship_type": "접근법"},
    {"source_name": "베이즈 머신러닝", "target_name": "베이즈 머신러닝의 연산적 이슈", "relationship_type": "구현_문제"},
    {"source_name": "통계학", "target_name": "빈도주의 통계학", "relationship_type": "패러다임"},
    {"source_name": "빈도주의 통계학", "target_name": "표본 분포", "relationship_type": "핵심_개념"},
    {"source_name": "최대 가능도 추정", "target_name": "MLE의 표본 분포의 가우스 근사", "relationship_type": "근사_방법"},
    {"source_name": "통계학", "target_name": "임의 추정량의 표본 분포의 부트스트랩 근사", "relationship_type": "추정_기법"},
    {"source_name": "빈도주의 통계학", "target_name": "신뢰 구간", "relationship_type": "추정_방법"},
    {"source_name": "신뢰 구간", "target_name": "주의: 신뢰 구간은 신용할 만하지 않다", "relationship_type": "해석_주의사항"},
    {"source_name": "머신러닝", "target_name": "편향-분산 트레이드오프", "relationship_type": "핵심_개념"},
    {"source_name": "베이즈 통계학", "target_name": "빈도주의 통계학", "relationship_type": "대비되는_접근"},
    {"source_name": "정칙화", "target_name": "편향-분산 트레이드오프", "relationship_type": "관련_개념"},
    {"source_name": "교차 검증", "target_name": "검증 집합을 사용해 정칙자 고르기", "relationship_type": "응용"}
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