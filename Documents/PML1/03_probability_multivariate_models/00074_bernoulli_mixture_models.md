# 베르누이 혼합 모델 (Bernoulli Mixture Model)

베르누이 혼합 모델(Bernoulli Mixture Model, BMM)은 이진 데이터(binary data)를 모델링하기 위한 확률적 모델입니다. BMM은 여러 개의 베르누이 분포의 혼합을 통해 데이터를 설명합니다. 이 모델은 주로 이진 데이터의 군집화와 밀도 추정에 활용됩니다.

## 1. 베르누이 혼합 모델의 정의

베르누이 혼합 모델은 다음과 같은 형태로 정의됩니다:

$$
p(x) = \sum_{k=1}^{K} \pi_k \prod_{j=1}^{d} \text{Bern}(x_j | \theta_{kj})
$$

여기서:
- $K$는 혼합 성분(Mixture Component)의 수입니다.
- $\pi_k$는 각 성분 $k$의 혼합 가중치(Mixture Weight)로, $\sum_{k=1}^{K} \pi_k = 1$을 만족합니다.
- $\text{Bern}(x_j | \theta_{kj})$는 성분 $k$에 대한 베르누이 분포입니다. 이는 $x_j$가 1일 확률이 $\theta_{kj}$인 베르누이 분포로 정의됩니다.
- $d$는 데이터의 차원(이진 변수의 수)입니다.

베르누이 혼합 모델은 각 데이터 포인트가 여러 개의 베르누이 분포 중 하나로부터 생성된 것으로 가정합니다.

## 2. 베르누이 분포

베르누이 혼합 모델의 기본 구성 요소는 베르누이 분포입니다. 베르누이 분포는 이진 확률 변수 $x$에 대해 정의되며, 다음과 같은 확률 질량 함수(PMF)를 가집니다:

$$
\text{Bern}(x | \theta) = \theta^x (1 - \theta)^{1 - x}
$$

여기서:
- $x \in \{0, 1\}$는 이진 확률 변수입니다.
- $\theta \in [0, 1]$는 $x = 1$일 확률입니다.

베르누이 분포는 이진 결과를 모델링하는 데 매우 적합한 분포입니다.

## 3. 매개변수 추정: 기대 최대화 (EM) 알고리즘

BMM의 매개변수 $\{\pi_k, \theta_{kj}\}$를 추정하기 위해 **기대 최대화(Expectation-Maximization, EM) 알고리즘**이 자주 사용됩니다. 이 알고리즘은 다음과 같은 두 단계로 구성됩니다:

### 3.1 기대 단계 (Expectation Step, E-step)
현재 매개변수를 바탕으로 각 데이터 포인트가 성분 $k$에서 생성되었을 확률을 계산합니다.

$$
\gamma(z_{nk}) = \frac{\pi_k \prod_{j=1}^{d} \text{Bern}(x_{nj} | \theta_{kj})}{\sum_{l=1}^{K} \pi_l \prod_{j=1}^{d} \text{Bern}(x_{nj} | \theta_{lj})}
$$

여기서 $\gamma(z_{nk})$는 데이터 포인트 $x_n$가 성분 $k$에 속할 확률입니다.

### 3.2 최대화 단계 (Maximization Step, M-step)
E-step에서 계산된 확률을 바탕으로 매개변수를 업데이트합니다.

$$
\pi_k = \frac{1}{N} \sum_{n=1}^{N} \gamma(z_{nk})
$$

$$
\theta_{kj} = \frac{\sum_{n=1}^{N} \gamma(z_{nk}) x_{nj}}{\sum_{n=1}^{N} \gamma(z_{nk})}
$$

이 과정을 반복하여 매개변수가 수렴할 때까지 최적화를 수행합니다.

## 4. 활용 분야

베르누이 혼합 모델은 다음과 같은 이진 데이터 분석 문제에 활용됩니다:
- **클러스터링**: 이진 데이터의 군집을 찾아내는 데 사용됩니다.
- **밀도 추정**: 주어진 이진 데이터 분포를 베르누이 분포의 혼합으로 근사합니다.
- **이상 탐지**: 비정상적인 이진 데이터 포인트를 탐지하는 데 사용됩니다.

## 5. 한계 및 확장

BMM은 이진 데이터를 모델링하는 데 유용하지만, 모델의 성능은 혼합 성분 수 $K$와 초기화에 민감할 수 있습니다. 또한, 모델이 데이터의 복잡성을 완전히 반영하지 못할 수 있습니다. 이를 극복하기 위해 혼합 모델의 다양한 확장이 제안되고 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
