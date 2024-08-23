# 확률적 그래프 모델 학습

확률적 그래프 모델(Probabilistic Graphical Models, PGM)의 학습은 주어진 데이터로부터 모델의 매개변수와 구조를 추정하는 과정을 의미합니다. PGM 학습은 크게 두 가지 측면에서 이루어집니다: **매개변수 학습**과 **구조 학습**. 이 문서에서는 이 두 가지 학습 방법과 각각의 주요 알고리즘에 대해 설명합니다.

## 1. 매개변수 학습

매개변수 학습은 주어진 그래프 구조에서 확률 분포를 파라미터화하는 과정입니다. 예를 들어, 베이지안 네트워크에서는 조건부 확률 분포(CPD)를 추정하고, 마르코프 랜덤 필드에서는 포텐셜 함수(potential function)를 추정합니다. 

### 1.1 완전 데이터

만약 모든 변수의 값이 완전히 주어져 있다면, 매개변수 학습은 상대적으로 간단해집니다. 최대우도추정법(Maximum Likelihood Estimation, MLE)과 최대사후확률추정법(Maximum A Posteriori, MAP)이 가장 일반적으로 사용됩니다.

- **최대우도추정법 (MLE)**: 
  주어진 데이터 집합 $D = \{x_1, x_2, \dots, x_N\}$에 대해, MLE는 매개변수 $\theta$를 다음과 같이 추정합니다:

  $$
  \hat{\theta}_{\text{MLE}} = \underset{\theta}{\text{argmax}} \ p(D | \theta)
  $$

- **최대사후확률추정법 (MAP)**:
  사전 분포(prior distribution) $p(\theta)$가 주어진 경우, MAP 추정은 다음과 같이 이루어집니다:

  $$
  \hat{\theta}_{\text{MAP}} = \underset{\theta}{\text{argmax}} \ p(\theta | D) = \underset{\theta}{\text{argmax}} \ p(D | \theta) p(\theta)
  $$

### 1.2 불완전 데이터

실제로는 일부 데이터가 관측되지 않았거나 누락된 경우가 많습니다. 이 경우, **기대-최대화 알고리즘(Expectation-Maximization, EM)**이 주로 사용됩니다.

- **기대-최대화 알고리즘 (EM)**:
  EM 알고리즘은 다음 두 단계로 반복적으로 수행됩니다:
  
  1. **기대 단계 (E-step)**: 현재 추정된 매개변수를 사용하여 숨겨진 변수의 기대값을 계산합니다.
  2. **최대화 단계 (M-step)**: 기대 단계에서 계산된 값을 사용하여 매개변수를 업데이트합니다.

  이 과정을 반복하여 로그우도(log-likelihood)가 최대가 될 때까지 매개변수를 최적화합니다.

## 2. 구조 학습

구조 학습은 데이터로부터 그래프의 구조를 추정하는 과정을 의미합니다. 이는 특정 변수들 간의 의존 관계를 발견하고, 그 관계를 나타내는 그래프를 학습하는 것입니다.

### 2.1 점수 기반 방법

점수 기반 방법에서는 가능한 모든 그래프 구조에 점수를 부여하고, 가장 높은 점수를 얻는 구조를 선택합니다. 대표적인 점수 함수로는 **BIC(Bayesian Information Criterion)**와 **AIC(Akaike Information Criterion)**가 있습니다.

- **BIC (Bayesian Information Criterion)**:
  
  $$
  \text{BIC} = -2 \log p(D | \hat{\theta}, G) + k \log N
  $$
  
  여기서 $k$는 모델의 자유도(degrees of freedom)이고, $N$은 데이터 포인트의 수입니다.

- **AIC (Akaike Information Criterion)**:

  $$
  \text{AIC} = -2 \log p(D | \hat{\theta}, G) + 2k
  $$

### 2.2 제약 기반 방법

제약 기반 방법에서는 독립성 테스트(independence test)를 사용하여 변수 간의 조건부 독립성을 탐색하고, 이를 기반으로 그래프 구조를 구성합니다.

## 3. 혼합 학습

혼합 학습에서는 구조와 매개변수를 동시에 학습합니다. 이 경우, 구조와 매개변수를 번갈아가며 학습하는 방법이 사용되며, 이 과정은 **최적화 문제**로 볼 수 있습니다.

## 4. 결론

확률적 그래프 모델의 학습은 복잡한 데이터의 구조와 확률적 관계를 이해하는 데 필수적입니다. 매개변수 학습과 구조 학습은 각각의 문제에 적합한 다양한 알고리즘을 통해 이루어지며, 실제 데이터의 복잡성에 따라 적절한 방법을 선택해야 합니다.

## 5. 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
