# 가우스 혼합 모델 (Gaussian Mixture Model)

가우스 혼합 모델(Gaussian Mixture Model, GMM)은 데이터를 여러 개의 가우스 분포로 모델링하는 확률적 모델입니다. GMM은 군집화, 밀도 추정, 그리고 복잡한 데이터 구조를 설명하는 데 널리 사용됩니다. 각 데이터 포인트는 여러 개의 가우스 분포 중 하나로부터 생성된 것으로 간주되며, 이러한 가우스 분포의 혼합으로 전체 데이터 분포가 구성됩니다.

## 1. 가우스 혼합 모델의 정의

GMM은 다음과 같은 형태로 정의됩니다:

$$
p(x) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x | \mu_k, \Sigma_k)
$$

여기서:
- $K$는 혼합 성분(Mixture Component)의 수입니다.
- $\pi_k$는 각 성분 $k$의 혼합 가중치(Mixture Weight)로, $\sum_{k=1}^{K} \pi_k = 1$을 만족합니다.
- $\mathcal{N}(x | \mu_k, \Sigma_k)$는 성분 $k$에 대한 가우스 분포입니다.
  - $\mu_k$는 성분 $k$의 평균 벡터,
  - $\Sigma_k$는 성분 $k$의 공분산 행렬입니다.

GMM은 데이터를 여러 개의 가우스 분포로 표현함으로써 데이터의 복잡한 구조를 단순화하고 분석할 수 있게 해줍니다.

## 2. 가우스 분포

가우스 혼합 모델의 핵심은 각 성분이 가우스 분포를 따르는 것입니다. 가우스 분포는 다음과 같이 정의됩니다:

$$
\mathcal{N}(x | \mu, \Sigma) = \frac{1}{(2\pi)^{d/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)\right)
$$

여기서:
- $d$는 데이터의 차원 수,
- $\mu$는 평균 벡터,
- $\Sigma$는 공분산 행렬입니다.

가우스 분포는 벨 모양의 곡선을 나타내며, 평균 $\mu$를 중심으로 하고 공분산 $\Sigma$에 의해 그 모양이 결정됩니다.

## 3. 매개변수 추정: 기대 최대화 (EM) 알고리즘

GMM의 매개변수 $\{\pi_k, \mu_k, \Sigma_k\}$를 추정하기 위해 **기대 최대화(Expectation-Maximization, EM) 알고리즘**이 주로 사용됩니다. 이 알고리즘은 다음과 같은 두 단계로 구성됩니다:

### 3.1 기대 단계 (Expectation Step, E-step)
현재 매개변수를 바탕으로 각 데이터 포인트가 성분 $k$에서 생성되었을 확률을 계산합니다.

$$
\gamma(z_{nk}) = \frac{\pi_k \mathcal{N}(x_n | \mu_k, \Sigma_k)}{\sum_{j=1}^{K} \pi_j \mathcal{N}(x_n | \mu_j, \Sigma_j)}
$$

여기서 $\gamma(z_{nk})$는 데이터 포인트 $x_n$가 성분 $k$에 속할 확률입니다.

### 3.2 최대화 단계 (Maximization Step, M-step)
E-step에서 계산된 확률을 바탕으로 매개변수를 업데이트합니다.

$$
\pi_k = \frac{1}{N} \sum_{n=1}^{N} \gamma(z_{nk})
$$

$$
\mu_k = \frac{\sum_{n=1}^{N} \gamma(z_{nk}) x_n}{\sum_{n=1}^{N} \gamma(z_{nk})}
$$

$$
\Sigma_k = \frac{\sum_{n=1}^{N} \gamma(z_{nk}) (x_n - \mu_k)(x_n - \mu_k)^T}{\sum_{n=1}^{N} \gamma(z_{nk})}
$$

이 과정을 반복하여 매개변수가 수렴할 때까지 최적화를 수행합니다.

## 4. 활용 분야

GMM은 다음과 같은 다양한 문제에 활용됩니다:
- **클러스터링**: 데이터의 자연적인 군집을 찾아내는 데 사용됩니다.
- **밀도 추정**: 주어진 데이터 분포를 가우스 분포의 혼합으로 근사합니다.
- **이상 탐지**: 정상적인 데이터 분포에서 벗어난 포인트를 식별하는 데 사용됩니다.

## 5. 한계 및 확장

GMM은 강력한 도구이지만, 초기화에 민감하고 성분 수 $K$의 선택이 모델의 성능에 큰 영향을 미칠 수 있습니다. 또한, 모든 성분이 가우스 분포를 따르지 않는 경우에는 성능이 저하될 수 있습니다. 이러한 한계를 극복하기 위해 다양한 확장 모델들이 제안되었습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
