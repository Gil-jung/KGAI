# 응용: 다변량 정규 분포(MVN)의 조건부 분포 유도하기

다변량 정규 분포(Multivariate Normal Distribution, MVN)는 여러 변수들 간의 선형 관계를 모델링하는 데 사용됩니다. MVN의 중요한 특성 중 하나는, 부분 벡터에 대해 조건부 분포를 유도할 수 있다는 점입니다. 이는 특히 베이즈 추론과 같은 통계적 기법에서 매우 유용합니다.

## 1. 다변량 정규 분포(MVN)의 정의

차원이 $n$인 다변량 정규 분포 $\mathbf{x} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$는 평균 벡터 $\boldsymbol{\mu} \in \mathbb{R}^n$와 공분산 행렬 $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times n}$로 정의됩니다.

$$
p(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\boldsymbol{\Sigma}|^{1/2}} \exp \left(-\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)
$$

## 2. MVN의 조건부 분포 유도

MVN에서 변수 벡터 $\mathbf{x}$를 두 부분으로 나눌 수 있습니다:

$$
\mathbf{x} = \begin{pmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{pmatrix}
$$

여기서 $\mathbf{x}_1 \in \mathbb{R}^{n_1}$, $\mathbf{x}_2 \in \mathbb{R}^{n_2}$, 그리고 $n_1 + n_2 = n$입니다. 이에 따라 평균 벡터와 공분산 행렬도 다음과 같이 나눌 수 있습니다:

$$
\boldsymbol{\mu} = \begin{pmatrix} \boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2 \end{pmatrix}, \quad \boldsymbol{\Sigma} = \begin{pmatrix} \boldsymbol{\Sigma}_{11} & \boldsymbol{\Sigma}_{12} \\ \boldsymbol{\Sigma}_{21} & \boldsymbol{\Sigma}_{22} \end{pmatrix}
$$

여기서:
- $\boldsymbol{\mu}_1$과 $\boldsymbol{\mu}_2$는 각각 $\mathbf{x}_1$과 $\mathbf{x}_2$의 평균 벡터
- $\boldsymbol{\Sigma}_{11}$과 $\boldsymbol{\Sigma}_{22}$는 각각 $\mathbf{x}_1$과 $\mathbf{x}_2$의 공분산 행렬
- $\boldsymbol{\Sigma}_{12}$는 $\mathbf{x}_1$과 $\mathbf{x}_2$ 사이의 공분산 행렬입니다.

### 2.1. $\mathbf{x}_1$이 주어진 $\mathbf{x}_2$의 조건부 분포

$\mathbf{x}_2$가 주어진 $\mathbf{x}_1$의 조건부 분포는 다음과 같이 유도됩니다:

$$
\mathbf{x}_1 | \mathbf{x}_2 \sim \mathcal{N}(\boldsymbol{\mu}_{1|2}, \boldsymbol{\Sigma}_{1|2})
$$

여기서:
- 조건부 평균:

$$
\boldsymbol{\mu}_{1|2} = \boldsymbol{\mu}_1 + \boldsymbol{\Sigma}_{12} \boldsymbol{\Sigma}_{22}^{-1} (\mathbf{x}_2 - \boldsymbol{\mu}_2)
$$

- 조건부 공분산 행렬:

$$
\boldsymbol{\Sigma}_{1|2} = \boldsymbol{\Sigma}_{11} - \boldsymbol{\Sigma}_{12} \boldsymbol{\Sigma}_{22}^{-1} \boldsymbol{\Sigma}_{21}
$$

### 2.2. 조건부 분포의 의미

이 결과는 $\mathbf{x}_2$가 주어졌을 때, $\mathbf{x}_1$이 얼마나 분산하는지를 나타냅니다. 또한, $\mathbf{x}_2$의 값이 $\mathbf{x}_1$의 예상값(평균)에 어떻게 영향을 미치는지 보여줍니다. 이러한 조건부 분포는 베이지안 추론, 회귀 분석, 그리고 상태 공간 모델 등 다양한 응용에서 핵심적인 역할을 합니다.

## 3. 응용

### 3.1. 베이즈 추론

MVN의 조건부 분포는 베이즈 추론에서 매우 중요한 역할을 합니다. 베이즈 추론에서 사전 분포와 데이터의 관찰값이 주어졌을 때 사후 분포를 계산하는 데 사용됩니다.

### 3.2. 회귀 분석

다변량 회귀에서 조건부 분포는 설명 변수들에 대해 종속 변수의 분포를 모델링하는 데 사용됩니다.

### 3.3. 상태 공간 모델

시간에 따라 변화하는 시스템의 상태를 추적하는 데 사용되는 상태 공간 모델에서 조건부 분포는 과거 상태나 관찰값이 주어졌을 때 현재 상태의 분포를 추정하는 데 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
