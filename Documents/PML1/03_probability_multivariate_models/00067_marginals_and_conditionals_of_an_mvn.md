# 다변량 정규 분포(MVN)의 주변 및 조건부 분포

**다변량 정규 분포(Multivariate Normal Distribution, MVN)**는 다변량 데이터의 확률 분포를 나타내는 중요한 통계 모델입니다. MVN의 가장 중요한 성질 중 하나는 주변 분포와 조건부 분포가 모두 정규 분포라는 점입니다. 이 성질은 다양한 기계 학습 및 통계 모델에서 중요한 역할을 합니다.

## 1. 다변량 정규 분포(MVN) 정의

MVN은 평균 벡터 \(\mu\)와 공분산 행렬 \(\Sigma\)로 정의됩니다. 이때, n차원의 다변량 정규 분포는 다음과 같이 표현됩니다:

\[
\mathbf{x} \sim \mathcal{N}(\mu, \Sigma)
\]

여기서:
- \(\mathbf{x}\)는 n차원의 랜덤 벡터입니다.
- \(\mu\)는 n차원의 평균 벡터입니다.
- \(\Sigma\)는 \(n \times n\) 크기의 공분산 행렬입니다.

MVN의 확률 밀도 함수는 다음과 같습니다:

\[
p(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\Sigma|^{1/2}} \exp \left( -\frac{1}{2} (\mathbf{x} - \mu)^\top \Sigma^{-1} (\mathbf{x} - \mu) \right)
\]

## 2. 주변 분포(Marginal Distribution)

MVN의 성질 중 하나는 벡터 \(\mathbf{x}\)의 일부 성분에 대한 주변 분포도 정규 분포라는 점입니다. 예를 들어, \(\mathbf{x}\)를 두 개의 서브벡터 \(\mathbf{x}_1\)과 \(\mathbf{x}_2\)로 나눌 수 있다고 가정합니다:

\[
\mathbf{x} = \begin{pmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{pmatrix}, \quad \mu = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \quad \Sigma = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}
\]

이 경우 \(\mathbf{x}_1\)의 주변 분포는 \(\mathbf{x}_1 \sim \mathcal{N}(\mu_1, \Sigma_{11})\)로 표현됩니다.

## 3. 조건부 분포(Conditional Distribution)

MVN의 또 다른 중요한 성질은 한 부분에 대한 조건부 분포도 정규 분포를 따른다는 것입니다. 위의 \(\mathbf{x}\)와 \(\mu\), \(\Sigma\) 표현을 사용하면, \(\mathbf{x}_1\)이 주어진 \(\mathbf{x}_2\)에 대한 조건부 분포는 다음과 같이 표현됩니다:

\[
\mathbf{x}_1 \mid \mathbf{x}_2 = \mathbf{c} \sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2})
\]

여기서:
- \(\mu_{1|2} = \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (\mathbf{c} - \mu_2)\)
- \(\Sigma_{1|2} = \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}\)

이 조건부 분포의 평균은 \(\mathbf{x}_2\)에 의존하며, 공분산은 \(\mathbf{x}_2\)와 독립적입니다.

## 4. 응용 예시

### 4.1 베이즈 추론
MVN의 조건부 분포 성질은 베이즈 추론에서 자주 활용됩니다. 베이즈 업데이트 과정에서 조건부 분포를 계산하여 사후 분포(posterior distribution)를 구하는 데 유용합니다.

### 4.2 다변량 회귀 분석
다변량 회귀 분석에서는 종속 변수 벡터가 독립 변수 벡터에 대해 MVN을 따른다고 가정하는 경우가 많습니다. 이 경우 조건부 분포를 사용하여 회귀 계수와 예측치를 계산할 수 있습니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
