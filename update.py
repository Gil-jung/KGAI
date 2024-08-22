from knowledge_graph_manager import KnowledgeGraphManager
import json, os

manager = KnowledgeGraphManager()

old_nodes = [
    {
        "name": "확률",
        "category": "수학적 개념",
        "properties": {
            "정의": "사건이 발생할 가능성을 수치화한 것",
            "주요_개념": ["표본 공간", "사건", "확률 측도"],
            "응용_분야": ["통계학", "머신러닝", "의사결정 이론"],
            "확률론의_공리": ["비음수성", "정규화", "가산 가법성"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00020_probability.md", "r", encoding="utf-8").read()
    },
    {
        "name": "불확실성의 형태",
        "category": "확률 및 통계 개념",
        "properties": {
            "주요_형태": ["내재적 불확실성", "인식론적 불확실성"],
            "내재적_불확실성_예시": ["양자역학의 불확정성", "유전적 변이"],
            "인식론적_불확실성_예시": ["측정 오차", "모델의 한계"],
            "불확실성_처리_방법": ["확률론", "퍼지 논리", "구간 분석"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00021_types_of_uncertainty.md", "r", encoding="utf-8").read()
    },
    {
        "name": "논리의 확장으로서의 확률",
        "category": "확률 이론",
        "properties": {
            "주요_개념": ["명제 논리", "확률적 추론"],
            "확률의_특징": ["불확실성 표현", "부분적 지식 처리"],
            "응용_분야": ["베이지안 추론", "의사결정 이론"],
            "관련_이론": ["콕스의 정리", "최대 엔트로피 원리"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00022_probability_as_an_extension_of_logic.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 변수",
        "category": "확률론 개념",
        "properties": {
            "정의": "확률 공간의 원소를 실수로 대응시키는 함수",
            "종류": ["이산 확률 변수", "연속 확률 변수"],
            "특성": ["확률 분포", "기댓값", "분산"],
            "응용": ["통계적 모델링", "확률적 알고리즘"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00023_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산 확률 변수",
        "category": "확률론 개념",
        "properties": {
            "정의": "유한하거나 가산 무한한 값을 가지는 확률 변수",
            "특징": ["확률 질량 함수", "이산적 값"],
            "예시": ["동전 던지기", "주사위 굴리기"],
            "주요_분포": ["베르누이 분포", "이항 분포", "포아송 분포"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00024_discrete_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속 확률 변수",
        "category": "확률론 개념",
        "properties": {
            "정의": "연속적인 값을 가지는 확률 변수",
            "특징": ["확률 밀도 함수", "연속적 값"],
            "예시": ["시간", "길이", "온도"],
            "주요_분포": ["정규 분포", "지수 분포", "감마 분포"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00025_continuous_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "관련된 확률 변수의 집합",
        "category": "확률론 개념",
        "properties": {
            "정의": "서로 관련된 여러 확률 변수들의 모음",
            "특징": ["결합 분포", "조건부 분포", "주변 분포"],
            "응용": ["다변량 분석", "시계열 분석"],
            "주요_개념": ["공분산", "상관계수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00026_sets_of_related_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "독립과 조건부 독립",
        "category": "확률론 개념",
        "properties": {
            "정의": {
                "독립": "한 사건의 발생이 다른 사건의 확률에 영향을 주지 않음",
                "조건부 독립": "주어진 조건 하에서 두 사건이 독립"
            },
            "특징": ["확률의 곱셈 법칙", "베이즈 정리와의 관계"],
            "응용": ["나이브 베이즈 분류기", "그래프 모델"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00027_independence_and_conditional_independence.md", "r", encoding="utf-8").read()
    },
    {
        "name": "분포의 적률",
        "category": "통계학 개념",
        "properties": {
            "정의": "확률 분포의 특성을 나타내는 수치",
            "주요_적률": ["평균", "분산", "왜도", "첨도"],
            "응용": ["분포 특성 파악", "통계적 추론"],
            "관련_개념": ["적률 생성 함수", "특성 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00028_moments_of_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "요약 통계량의 한계",
        "category": "통계학 개념",
        "properties": {
            "주요_한계": ["정보 손실", "분포의 전체 특성 미반영"],
            "예시": ["앤스콤의 4분할", "심슨의 역설"],
            "대안_방법": ["시각화", "비모수적 방법"],
            "고려사항": ["데이터의 특성", "분석 목적"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00029_limitations_of_summary_statistics.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베이즈 규칙",
        "category": "확률론 개념",
        "properties": {
            "정의": "조건부 확률을 이용해 사후 확률을 계산하는 규칙",
            "구성_요소": ["사전 확률", "우도", "증거", "사후 확률"],
            "응용_분야": ["기계 학습", "의사결정 이론", "정보 검색"],
            "관련_개념": ["베이지안 추론", "최대 사후 확률"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00030_bayes_rule.md", "r", encoding="utf-8").read()
    },
    {
        "name": "역 문제",
        "category": "수학 및 과학 개념",
        "properties": {
            "정의": "관찰된 결과로부터 원인이나 매개변수를 추론하는 문제",
            "특징": ["불량 조건", "해의 불안정성"],
            "응용_분야": ["의료 영상", "지구물리학", "신호 처리"],
            "해결_방법": ["정규화", "베이지안 접근법"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00031_inverse_problem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베르누이 분포와 이항 분포",
        "category": "확률 분포",
        "properties": {
            "베르누이_분포": {
                "정의": "성공/실패 두 가지 결과만 가능한 단일 시행의 확률 분포",
                "매개변수": "성공 확률 p"
            },
            "이항_분포": {
                "정의": "n번의 독립적인 베르누이 시행에서 성공 횟수의 확률 분포",
                "매개변수": ["시행 횟수 n", "성공 확률 p"]
            },
            "응용": ["품질 관리", "의학 연구", "선거 예측"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00032_bernoulli_and_binomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "시그모이드(로지스틱) 함수",
        "category": "수학 함수",
        "properties": {
            "정의": "입력을 0과 1 사이의 값으로 변환하는 S자 형태의 함수",
            "수식": "σ(x) = 1 / (1 + e^(-x))",
            "특징": ["단조 증가", "미분 가능", "출력 범위 (0, 1)"],
            "응용": ["로지스틱 회귀", "신경망 활성화 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00033_sigmoid_logistic_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이항 로지스틱 회귀",
        "category": "통계학 및 기계학습 기법",
        "properties": {
            "정의": "이진 분류를 위한 통계적 모델",
            "특징": ["선형 결정 경계", "확률적 출력"],
            "매개변수 추정": ["최대 우도 추정", "경사 하강법"],
            "평가 지표": ["정확도", "ROC 곡선", "F1 점수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00034_binomial_logistic_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "범주형 및 다항 분포",
        "category": "확률 분포",
        "properties": {
            "범주형_분포": {
                "정의": "유한한 수의 가능한 결과에 대한 확률 분포",
                "특징": ["이산적", "상호 배타적 결과"]
            },
            "다항_분포": {
                "정의": "여러 범주에 대한 시행 횟수의 결합 분포",
                "매개변수": ["시행 횟수 n", "각 범주의 확률"]
            },
            "응용": ["텍스트 분류", "유전자 발현 분석"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00035_categorical_and_multinomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "소프트맥스 함수",
        "category": "수학 함수",
        "properties": {
            "정의": "입력 벡터를 확률 분포로 변환하는 함수",
            "특징": ["출력의 합이 1", "지수 함수 사용"],
            "응용": ["다중 클래스 분류", "신경망 출력층"],
            "관련_개념": ["크로스 엔트로피 손실"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00036_softmax_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "다중 클래스 로지스틱 회귀",
        "category": "통계학 및 기계학습 기법",
        "properties": {
            "정의": "여러 클래스 중 하나로 분류하는 모델",
            "특징": ["소프트맥스 함수 사용", "선형 결정 경계"],
            "학습_방법": ["최대 우도 추정", "경사 하강법"],
            "평가_지표": ["정확도", "혼동 행렬", "F1 점수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00037_multiclass_logistic_regression.md", "r", encoding="utf-8").read()
    },
    {
        "name": "Log-Sum-Exp 트릭",
        "category": "수치 계산 기법",
        "properties": {
            "목적": "수치적 안정성 향상",
            "적용_분야": ["소프트맥스 계산", "로그 우도 계산"],
            "수학적_기반": ["지수 함수의 성질", "로그 함수의 성질"],
            "장점": ["오버플로우 방지", "언더플로우 방지"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00038_log_sum_exp_trick.md", "r", encoding="utf-8").read()
 },
    {
        "name": "일변량 가우스(정규) 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "종 모양의 대칭적인 확률 분포",
            "매개변수": ["평균 μ", "표준편차 σ"],
            "특징": ["중심극한정리와의 관계", "최대 엔트로피 분포"],
            "응용": ["자연 현상 모델링", "측정 오차 분석", "통계적 추론"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00039_univariate_gaussian_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "누적 분포 함수",
        "category": "확률론 개념",
        "properties": {
            "정의": "확률 변수가 특정 값 이하일 확률을 나타내는 함수",
            "특징": ["단조 증가", "우연속", "극한값 0과 1"],
            "응용": ["확률 계산", "분위수 추정", "통계적 검정"],
            "관련_개념": ["확률 밀도 함수", "분위 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00040_cumulative_distribution_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 밀도 함수",
        "category": "확률론 개념",
        "properties": {
            "정의": "연속 확률 변수의 확률 분포를 나타내는 함수",
            "특징": ["비음수", "적분값 1", "연속 확률 변수에만 적용"],
            "응용": ["확률 계산", "우도 함수", "커널 밀도 추정"],
            "관련_개념": ["누적 분포 함수", "확률 질량 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00041_probability_density_function.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스 분포에서의 회귀",
        "category": "통계학 및 기계학습 기법",
        "properties": {
            "정의": "가우스 분포를 가정한 회귀 분석",
            "특징": ["최소제곱법과의 관계", "최대 우도 추정"],
            "가정": ["오차의 정규성", "등분산성", "독립성"],
            "응용": ["선형 회귀", "다항 회귀", "일반화 선형 모델"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00042_regression_for_gaussian.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가우스 분포가 널리 쓰이는 이유",
        "category": "확률론 및 통계학 개념",
        "properties": {
            "주요_이유": ["중심극한정리", "최대 엔트로피 원리", "수학적 편의성"],
            "특징": ["대칭성", "파라미터의 해석 용이성"],
            "한계": ["극단값 처리", "비대칭 데이터"],
            "대안_분포": ["t 분포", "로그정규 분포", "혼합 가우시안 모델"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00043_why_is_the_gaussian_distribution_so_widely_used.md", "r", encoding="utf-8").read()
    },
    {
        "name": "디랙 델타 함수",
        "category": "수학적 개념",
        "properties": {
            "정의": "특정 지점에서 무한대 값을 가지고 다른 곳에서는 0인 함수",
            "특징": ["적분값 1", "일반화된 함수"],
            "응용": ["신호 처리", "양자역학", "확률론"],
            "관련_개념": ["단위 계단 함수", "그린 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00044_dirac_delta_function_as_a_limiting_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "스튜던트 t 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "정규 분포의 평균을 추정할 때 사용되는 분포",
            "매개변수": ["자유도"],
            "특징": ["정규 분포보다 두꺼운 꼬리", "작은 표본에 적합"],
            "응용": ["가설 검정", "신뢰 구간 추정", "로버스트 회귀"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00045_student_t_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "코시 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "두꺼운 꼬리를 가진 대칭 분포",
            "특징": ["중앙값과 최빈값 존재", "평균과 분산 미정의"],
            "응용": ["로버스트 통계", "신호 처리", "물리학"],
            "관련_개념": ["안정 분포", "로렌츠 분포"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00046_cauchy_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "라플라스 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "두 지수 분포를 결합한 형태의 대칭 분포",
            "특징": ["첨예한 피크", "지수적 감소"],
            "응용": ["신호 처리", "압축 센싱", "베이지안 추론"],
            "관련_개념": ["L1 정규화", "중앙값 회귀"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00047_laplace_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베타 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "0과 1 사이의 값을 가지는 연속 확률 분포",
            "매개변수": ["α (알파)", "β (베타)"],
            "특징": ["다양한 형태 표현 가능", "켤레 사전 분포"],
            "응용": ["베이지안 추론", "비율 추정", "신뢰도 분석"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00048_beta_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "감마 분포",
        "category": "확률 분포",
        "properties": {
            "정의": "양의 실수 값을 가지는 연속 확률 분포",
            "매개변수": ["형상 매개변수 k", "척도 매개변수 θ"],
            "특징": ["지수 분포와 카이제곱 분포의 일반화", "가법성"],
            "응용": ["대기 시간 모델링", "신뢰성 분석", "베이지안 추론"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00049_gamma_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "경험적 분포",
        "category": "통계학 개념",
        "properties": {
            "정의": "관측된 데이터로부터 직접 추정된 확률 분포",
            "특징": ["비모수적 방법", "대규모 데이터에 적합"],
            "장점": ["분포 가정 불필요", "데이터 특성 반영"],
            "단점": ["과적합 위험", "극단값에 민감"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00050_empirical_distribution.md", "r", encoding="utf-8").read()
    },
    {
        "name": "확률 변수의 변환",
        "category": "확률론 개념",
        "properties": {
            "정의": "확률 변수에 함수를 적용하여 새로운 확률 변수를 생성",
            "방법": ["변수 변환법", "야코비안 행렬 사용"],
            "응용": ["확률 분포 생성", "통계적 추론", "몬테카를로 방법"],
            "주의사항": ["역함수의 존재", "다차원 변환"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00051_transformations_of_random_variables.md", "r", encoding="utf-8").read()
    },
    {
        "name": "이산형 확률 변수의 변환",
        "category": "확률론 개념",
        "properties": {
            "방법": ["확률 질량 함수 변환", "합성 함수 사용"],
            "특징": ["이산적 값 유지", "확률 보존"],
            "응용": ["암호화", "이산 신호 처리"],
            "예시": ["이항 분포에서 베르누이 분포로의 변환"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00052_discrete_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "연속형 확률 변수의 변환",
        "category": "확률론 개념",
        "properties": {
            "방법": ["확률 밀도 함수 변환", "야코비안 사용"],
            "특징": ["연속성 유지", "적분 변환"],
            "응용": ["비선형 회귀", "신호 처리"],
            "예시": ["정규 분포에서 로그 정규 분포로의 변환"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00053_continuous_case.md", "r", encoding="utf-8").read()
    },
    {
        "name": "가역 변환 (전단사)",
        "category": "수학적 개념",
        "properties": {
            "정의": "일대일 대응이면서 전체인 함수",
            "특징": ["역함수 존재", "입출력 차원 동일"],
            "응용": ["암호화", "정규화 흐름"],
            "예시": ["지수 함수와 로그 함수"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00054_invertible_transformations_bijections.md", "r", encoding="utf-8").read()
    },
    {
        "name": "선형 변환의 적률",
        "category": "확률론 개념",
        "properties": {
            "정의": "선형 변환 후 확률 변수의 적률 계산",
            "특징": ["평균과 분산의 선형 변환", "고차 적률 변환"],
            "응용": ["표준화", "주성분 분석"],
            "관련_개념": ["공분산 행렬 변환"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00055_moments_of_a_linear_transformation.md", "r", encoding="utf-8").read()
    },
    {
        "name": "합성곱 정리",
        "category": "확률론 개념",
        "properties": {
            "정의": "독립 확률 변수 합의 확률 밀도 함수 계산",
            "특징": ["푸리에 변환과의 관계", "특성 함수 사용"],
            "응용": ["신호 처리", "통신 이론", "금융 공학"],
            "한계": ["비독립 변수에 대한 적용 어려움"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00056_the_convolution_theorem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "중심 극한 정리",
        "category": "확률론 정리",
        "properties": {
            "정의": "독립 동일 분포 확률 변수의 합이 정규 분포에 수렴",
            "조건": ["유한한 평균과 분산", "독립성"],
            "응용": ["통계적 추론", "표본 평균의 분포"],
            "변형": ["리아푸노프 중심 극한 정리", "베리-에센 정리"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00057_central_limit_theorem.md", "r", encoding="utf-8").read()
    },
    {
        "name": "몬테카를로 근사",
        "category": "계산 방법론",
        "properties": {
            "정의": "무작위 표본을 이용한 수치적 결과 추정 방법",
            "특징": ["확률적 시뮬레이션", "대수의 법칙 활용"],
            "응용": ["적분 계산", "최적화", "위험 분석"],
            "한계": ["계산 비용", "차원의 저주"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00058_monte_carlo_approximation.md", "r", encoding="utf-8").read()
    }
]   



# 노드 생성
nodes = [
    {
        "name": "독립과 조건부 독립",
        "category": "확률론 개념",
        "properties": {
            "정의": {
                "독립": "한 사건의 발생이 다른 사건의 확률에 영향을 주지 않음",
                "조건부 독립": "주어진 조건 하에서 두 사건이 독립"
            },
            "특징": ["확률의 곱셈 법칙", "베이즈 정리와의 관계"],
            "응용": ["나이브 베이즈 분류기", "그래프 모델"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00027_independence_and_conditional_independence.md", "r", encoding="utf-8").read()
    },
    {
        "name": "베르누이 분포와 이항 분포",
        "category": "확률 분포",
        "properties": {
            "베르누이_분포": {
                "정의": "성공/실패 두 가지 결과만 가능한 단일 시행의 확률 분포",
                "매개변수": "성공 확률 p"
            },
            "이항_분포": {
                "정의": "n번의 독립적인 베르누이 시행에서 성공 횟수의 확률 분포",
                "매개변수": ["시행 횟수 n", "성공 확률 p"]
            },
            "응용": ["품질 관리", "의학 연구", "선거 예측"]
        },
        "markdown_content": open("Documents/PML1/02_probability_univariate_models/00032_bernoulli_and_binomial_distributions.md", "r", encoding="utf-8").read()
    },
    {
        "name": "범주형 및 다항 분포",
        "category": "확률 분포",
        "properties": {
            "범주형_분포": {
                "정의": "유한한 수의 가능한 결과에 대한 확률 분포",
                "특징": ["이산적", "상호 배타적 결과"]
            },
            "다항_분포": {
                "정의": "여러 범주에 대한 시행 횟수의 결합 분포",
                "매개변수": ["시행 횟수 n", "각 범주의 확률"]
            },
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

# 엣지 생성
edges = [
    # {"source_name": "머신러닝", "target_name": "확률", "relationship_type": "기반_이론"},

    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[1]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[2]['id'], "relationship_type": "이론적_기반"},
    {"source_id": created_nodes[10]['id'], "target_id": created_nodes[0]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[19]['id'], "target_id": created_nodes[20]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[19]['id'], "target_id": created_nodes[21]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[3]['id'], "relationship_type": "기본_개념"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[4]['id'], "relationship_type": "하위_분류"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[5]['id'], "relationship_type": "하위_분류"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[6]['id'], "relationship_type": "확장_개념"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[7]['id'], "relationship_type": "관련_개념"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[8]['id'], "relationship_type": "특성"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[10]['id'], "relationship_type": "핵심_정리"},
    {"source_id": created_nodes[10]['id'], "target_id": created_nodes[11]['id'], "relationship_type": "응용"},
    {"source_id": created_nodes[4]['id'], "target_id": created_nodes[12]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[19]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[25]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[26]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[27]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[28]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[5]['id'], "target_id": created_nodes[29]['id'], "relationship_type": "예시"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[30]['id'], "relationship_type": "응용"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[31]['id'], "relationship_type": "연산"},
    {"source_id": created_nodes[31]['id'], "target_id": created_nodes[32]['id'], "relationship_type": "하위_주제"},
    {"source_id": created_nodes[31]['id'], "target_id": created_nodes[33]['id'], "relationship_type": "하위_주제"},
    {"source_id": created_nodes[31]['id'], "target_id": created_nodes[34]['id'], "relationship_type": "특수_경우"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[35]['id'], "relationship_type": "특성"},
    {"source_id": created_nodes[3]['id'], "target_id": created_nodes[36]['id'], "relationship_type": "관련_정리"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[37]['id'], "relationship_type": "중요_정리"},
    {"source_id": created_nodes[0]['id'], "target_id": created_nodes[38]['id'], "relationship_type": "계산_방법"},
    {"source_id": created_nodes[1]['id'], "target_id": created_nodes[0]['id'], "relationship_type": "처리_방법"},
    {"source_id": created_nodes[2]['id'], "target_id": created_nodes[10]['id'], "relationship_type": "응용"},
    {"source_id": created_nodes[13]['id'], "target_id": created_nodes[14]['id'], "relationship_type": "핵심_요소"},
    {"source_id": created_nodes[16]['id'], "target_id": created_nodes[17]['id'], "relationship_type": "핵심_요소"},
    {"source_id": created_nodes[18]['id'], "target_id": created_nodes[16]['id'], "relationship_type": "계산_기법"},
    {"source_id": created_nodes[19]['id'], "target_id": created_nodes[22]['id'], "relationship_type": "응용"},
    {"source_id": created_nodes[19]['id'], "target_id": created_nodes[23]['id'], "relationship_type": "중요성"},
    {"source_id": created_nodes[24]['id'], "target_id": created_nodes[21]['id'], "relationship_type": "극한_경우"},
    {"source_id": created_nodes[37]['id'], "target_id": created_nodes[19]['id'], "relationship_type": "이론적_근거"}
]

edges = [
    {"source_name": "확률", "target_name": "불확실성의 형태", "relationship_type": "관련_개념"},
    {"source_name": "확률", "target_name": "논리의 확장으로서의 확률", "relationship_type": "이론적_기반"},
    {"source_name": "확률", "target_name": "확률 변수", "relationship_type": "핵심_개념"},
    {"source_name": "확률 변수", "target_name": "이산 확률 변수", "relationship_type": "종류"},
    {"source_name": "확률 변수", "target_name": "연속 확률 변수", "relationship_type": "종류"},
    {"source_name": "머신러닝", "target_name": "확률", "relationship_type": "기반_이론"},
    {"source_name": "베이즈 규칙", "target_name": "확률", "relationship_type": "관련_개념"},
    {"source_name": "베이즈 규칙", "target_name": "역 문제", "relationship_type": "응용"},
    {"source_name": "이산 확률 변수", "target_name": "베르누이 분포와 이항 분포", "relationship_type": "예시"},
    {"source_name": "시그모이드(로지스틱) 함수", "target_name": "이항 로지스틱 회귀", "relationship_type": "사용"},
    {"source_name": "소프트맥스 함수", "target_name": "다중 클래스 로지스틱 회귀", "relationship_type": "사용"},
    {"source_name": "확률 변수", "target_name": "일변량 가우스(정규) 분포", "relationship_type": "분포_예시"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "누적 분포 함수", "relationship_type": "관련_개념"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "확률 밀도 함수", "relationship_type": "관련_개념"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포에서의 회귀", "relationship_type": "응용"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포가 널리 쓰이는 이유", "relationship_type": "특징"},
    {"source_name": "확률 변수", "target_name": "스튜던트 t 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "코시 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "라플라스 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "베타 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "감마 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "경험적 분포", "relationship_type": "분포_예시"},
    {"source_name": "확률 변수", "target_name": "확률 변수의 변환", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수의 변환", "target_name": "이산형 확률 변수의 변환", "relationship_type": "세부_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "연속형 확률 변수의 변환", "relationship_type": "세부_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "가역 변환 (전단사)", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수", "target_name": "선형 변환의 적률", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수", "target_name": "합성곱 정리", "relationship_type": "관련_개념"},
    {"source_name": "확률 변수", "target_name": "중심 극한 정리", "relationship_type": "관련_정리"},
    {"source_name": "확률", "target_name": "몬테카를로 근사", "relationship_type": "응용_기법"}
]

edges.extend([
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
    {"source_name": "확률 변수", "target_name": "경험적 분포", "relationship_type": "응용"},
    {"source_name": "확률 변수", "target_name": "확률 변수의 변환", "relationship_type": "연산"},
    {"source_name": "확률 변수의 변환", "target_name": "이산형 확률 변수의 변환", "relationship_type": "하위_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "연속형 확률 변수의 변환", "relationship_type": "하위_주제"},
    {"source_name": "확률 변수의 변환", "target_name": "가역 변환 (전단사)", "relationship_type": "특수_경우"},
    {"source_name": "확률 변수", "target_name": "선형 변환의 적률", "relationship_type": "특성"},
    {"source_name": "확률 변수", "target_name": "합성곱 정리", "relationship_type": "관련_정리"},
    {"source_name": "확률", "target_name": "중심 극한 정리", "relationship_type": "중요_정리"},
    {"source_name": "확률", "target_name": "몬테카를로 근사", "relationship_type": "계산_방법"},
    {"source_name": "불확실성의 형태", "target_name": "확률", "relationship_type": "처리_방법"},
    {"source_name": "논리의 확장으로서의 확률", "target_name": "베이즈 규칙", "relationship_type": "응용"},
    {"source_name": "시그모이드(로지스틱) 함수", "target_name": "이항 로지스틱 회귀", "relationship_type": "핵심_요소"},
    {"source_name": "소프트맥스 함수", "target_name": "다중 클래스 로지스틱 회귀", "relationship_type": "핵심_요소"},
    {"source_name": "Log-Sum-Exp 트릭", "target_name": "소프트맥스 함수", "relationship_type": "계산_기법"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포에서의 회귀", "relationship_type": "응용"},
    {"source_name": "일변량 가우스(정규) 분포", "target_name": "가우스 분포가 널리 쓰이는 이유", "relationship_type": "중요성"},
    {"source_name": "디랙 델타 함수", "target_name": "확률 밀도 함수", "relationship_type": "극한_경우"},
    {"source_name": "중심 극한 정리", "target_name": "일변량 가우스(정규) 분포", "relationship_type": "이론적_근거"}
])

created_edges = []
for edge in edges:
    result = manager.add_edge(**edge)
    if result:
        created_edges.append(result)
        print(f"엣지 생성 성공: {result['relationship_type']}")
    else:
        print(f"엣지 생성 실패: {edge['relationship_type']}")

# 기존 파일 읽기
if os.path.exists("knowledge_graph.json"):
    with open("knowledge_graph.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)
else:
    existing_data = {"nodes": [], "edges": []}

# 새로운 노드와 엣지 추가
existing_data["nodes"].extend(created_nodes)
existing_data["edges"].extend(created_edges)

# 중복 제거 (옵션)
# existing_data["nodes"] = list({node["id"]: node for node in existing_data["nodes"]}.values())
# existing_data["edges"] = list({(edge["source_id"], edge["target_id"]): edge for edge in existing_data["edges"]}.values())

# 파일에 저장
with open("knowledge_graph.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print("지식그래프가 knowledge_graph.json 파일에 추가되었습니다.")