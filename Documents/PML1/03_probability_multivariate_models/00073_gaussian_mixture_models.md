# 가우스 혼합 모델 (Gaussian Mixture Model, GMM)

**가우스 혼합 모델(Gaussian Mixture Model, GMM)**은 통계적 모델 중 하나로, 관측된 데이터가 여러 개의 가우스 분포의 조합으로부터 생성되었다고 가정하는 모델입니다. 이는 **군집화(Clustering)**나 **밀도 추정(Density Estimation)** 등에서 자주 사용되며, 주어진 데이터가 잠재적으로 여러 그룹(클러스터)으로부터 생성되었을 때 이를 효과적으로 모델링할 수 있습니다.

## 1. 가우스 혼합 모델의 정의

가우스 혼합 모델은 $K$개의 가우시안 분포의 혼합으로 표현되며, 각 데이터 포인트 $x_n$이 $K$개의 서로 다른 가우스 분포에서 선택적으로 샘플링되었다고 가정합니다. GMM은 다음과 같은 확률 밀도 함수로 표현됩니다:

$$
p(x \mid \theta) = \sum_{k=1}^{K} \pi_k \mathcal{N}(x \mid \mu_k, \Sigma_k)
$$

여기서:

- $K$는 가우스 분포의 개수 (클러스터의 개수),
- $\pi_k$는 각 가우시안 성분의 혼합 계수 (즉, 각 가우시안 성분이 선택될 확률로, $\sum_{k=1}^{K} \pi_k = 1$),
- $\mathcal{N}(x \mid \mu_k, \Sigma_k)$는 평균 $\mu_k$와 공분산 $\Sigma_k$를 가지는 $k$번째 가우스 분포,
- $\theta$는 모든 파라미터들 $(\pi_k, \mu_k, \Sigma_k)$을 포함한 파라미터 벡터.

이 모델은 데이터를 설명하기 위해 여러 개의 가우스 분포를 혼합하여 각 데이터 포인트가 특정 가우시안 분포에 의해 생성된 것으로 간주합니다.

## 2. EM 알고리즘을 통한 추정

가우스 혼합 모델의 매개변수를 추정하는 가장 일반적인 방법은 **EM 알고리즘**(Expectation-Maximization Algorithm)입니다. EM 알고리즘은 숨겨진 변수가 있는 모델의 최대우도 추정을 수행하는 반복적 방법으로, GMM에서는 각 데이터 포인트가 어느 가우스 성분에서 생성되었는지 알 수 없기 때문에 이를 잠재 변수로 다루어 EM 알고리즘을 사용합니다.

### 2.1. E-Step (기대 단계)

각 데이터 포인트가 $k$번째 가우시안 분포에서 생성되었을 확률, 즉 책임도(responsibility) $\gamma(z_{nk})$를 계산합니다:

$$
\gamma(z_{nk}) = \frac{\pi_k \mathcal{N}(x_n \mid \mu_k, \Sigma_k)}{\sum_{j=1}^{K} \pi_j \mathcal{N}(x_n \mid \mu_j, \Sigma_j)}
$$

여기서 $\gamma(z_{nk})$는 데이터 포인트 $x_n$이 $k$번째 성분에 속할 확률을 의미합니다.

### 2.2. M-Step (최대화 단계)

E-Step에서 계산된 책임도를 바탕으로 가우시안 성분의 파라미터를 업데이트합니다:

- 혼합 계수 $\pi_k$:

$$
\pi_k = \frac{1}{N} \sum_{n=1}^{N} \gamma(z_{nk})
$$

- 평균 $\mu_k$:

$$
\mu_k = \frac{\sum_{n=1}^{N} \gamma(z_{nk}) x_n}{\sum_{n=1}^{N} \gamma(z_{nk})}
$$

- 공분산 행렬 $\Sigma_k$:

$$
\Sigma_k = \frac{\sum_{n=1}^{N} \gamma(z_{nk}) (x_n - \mu_k)(x_n - \mu_k)^T}{\sum_{n=1}^{N} \gamma(z_{nk})}
$$

이러한 단계들을 반복적으로 수행하여, 각 성분의 매개변수 $\pi_k, \mu_k, \Sigma_k$가 수렴할 때까지 모델을 학습합니다.

## 3. 가우스 혼합 모델의 해석

가우스 혼합 모델의 각 가우시안 성분은 데이터 내의 군집을 나타내며, EM 알고리즘을 통해 학습된 파라미터들은 이러한 군집의 위치(평균 $\mu_k$), 크기(공분산 $\Sigma_k$), 그리고 각 군집의 중요도(혼합 계수 $\pi_k$)를 설명합니다. 따라서 GMM은 군집화 문제에서 널리 사용되며, 특히 데이터가 비구조적이거나 복잡한 경우에도 효과적으로 작동할 수 있습니다.

또한 GMM은 고차원 데이터의 밀도를 추정하는 데에도 유용하며, 다양한 패턴 인식 및 기계 학습 문제에서 중요한 도구로 활용됩니다.

## 4. GMM의 한계와 확장

GMM은 매우 유용한 모델이지만, 다음과 같은 한계가 있습니다:

- 가우스 분포의 가정: 각 성분이 가우스 분포라는 가정을 따르므로, 실제 데이터가 가우스 분포에서 크게 벗어날 경우 성능이 저하될 수 있습니다.
- 성분 수 $K$의 선택: 적절한 성분 수를 선택하는 것은 어려울 수 있으며, 성분 수가 적절하지 않으면 과적합 또는 과소적합의 위험이 있습니다.

이러한 한계를 극복하기 위해 **베이지안 가우스 혼합 모델(Bayesian Gaussian Mixture Model)**과 같은 확장 모델들이 제안되었으며, 성분 수의 자동 결정 및 더 복잡한 데이터 분포를 처리할 수 있도록 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
