# 다변량 가우스(정규) 분포

**다변량 가우스(정규) 분포**(Multivariate Gaussian Distribution)는 여러 개의 확률 변수를 포함하는 다차원 공간에서의 확률 분포를 나타냅니다. 이는 특히 머신러닝과 통계학에서 데이터의 분포를 모델링하고 분석하는 데 널리 사용됩니다.

## 1. 정의

다변량 가우스 분포는 평균 벡터 $\mu$와 공분산 행렬 $\Sigma$에 의해 정의됩니다. n차원의 다변량 가우스 분포의 확률 밀도 함수(PDF)는 다음과 같이 표현됩니다:

$$
p(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x} - \mu)^\top \Sigma^{-1} (\mathbf{x} - \mu)\right)
$$

여기서:
- $\mathbf{x}$는 $n$차원 열 벡터로, 확률 변수를 나타냅니다.
- $\mu$는 평균 벡터로, 각 차원의 평균을 나타냅니다.
- $\Sigma$는 $n \times n$ 공분산 행렬로, 데이터의 분산과 각 차원 간의 상관관계를 나타냅니다.
- $|\Sigma|$는 공분산 행렬 $\Sigma$의 행렬식(Determinant)을 의미합니다.

## 2. 다변량 가우스 분포의 특성

### 2.1 평균 벡터 $\mu$
- 평균 벡터 $\mu$는 각 차원의 기대값(즉, 평균)을 나타냅니다.
- $\mu$의 차원은 다변량 가우스 분포의 차원과 동일하며, $\mu$가 위치한 점이 전체 분포의 중심이 됩니다.

### 2.2 공분산 행렬 $\Sigma$
- 공분산 행렬 $\Sigma$는 데이터의 분산과 각 차원 간의 상관관계를 나타냅니다.
- $\Sigma$의 대각선 성분은 각 변수의 분산을 나타내고, 비대각선 성분은 변수들 간의 공분산을 나타냅니다.
- 공분산 행렬이 대각 행렬인 경우, 각 차원 간에 상관관계가 없으며, 다변량 가우스 분포는 독립적인 일변량 가우스 분포들의 곱으로 나타낼 수 있습니다.

### 2.3 등고선과 타원
- 다변량 가우스 분포의 등고선(Contour)은 타원 모양을 띠며, 타원의 중심은 평균 벡터 $\mu$에 위치합니다.
- 타원의 크기와 방향은 공분산 행렬 $\Sigma$에 의해 결정되며, 타원의 주축 방향은 공분산 행렬의 고유벡터와 일치합니다.

## 3. 다변량 가우스 분포의 응용

### 3.1 머신러닝
- 다변량 가우스 분포는 머신러닝에서 데이터의 생성 모델로 자주 사용되며, 특히 가우시안 혼합 모델(Gaussian Mixture Model, GMM)에서 중요한 역할을 합니다.
- 가우스 나이브 베이즈 분류기와 같은 베이즈 모델에서 클래스별 조건부 확률로 다변량 가우스 분포를 사용하기도 합니다.

### 3.2 차원 축소
- 주성분 분석(PCA)은 다변량 가우스 분포의 공분산 행렬을 사용하여 데이터를 저차원 공간으로 투영합니다.
- 공분산 행렬의 고유값 분해를 통해 데이터의 주요 성분을 찾는 과정에서 다변량 가우스 분포의 성질이 활용됩니다.

### 3.3 이상치 탐지
- 다변량 가우스 분포를 이용해 데이터가 평균에서 벗어나는 정도를 측정하여 이상치를 탐지할 수 있습니다.
- 높은 차원의 공간에서 이상치를 탐지하는 데 효과적입니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
