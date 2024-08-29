# 고윳값 분해(Eigenvalue Decomposition, EVD)

고윳값 분해(Eigenvalue Decomposition, EVD)는 선형 대수에서 행렬을 분석하는 데 중요한 기법 중 하나로, 특히 대칭 행렬이나 정방 행렬(square matrix)의 특성을 이해하는 데 자주 사용됩니다. EVD는 행렬을 고윳값(eigenvalue)과 고유벡터(eigenvector)로 분해하는 방법으로, 기계 학습, 데이터 분석, 통계학 등 다양한 분야에서 활용됩니다.

## 1. 고윳값 분해의 정의

행렬 $\mathbf{A} \in \mathbb{R}^{n \times n}$가 주어졌을 때, $\mathbf{A}$의 고윳값 분해는 다음과 같이 표현할 수 있습니다:

$$
\mathbf{A} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^{-1}
$$

여기서:
- $\mathbf{V} \in \mathbb{R}^{n \times n}$: $\mathbf{A}$의 고유벡터들로 구성된 행렬.
- $\mathbf{\Lambda} \in \mathbb{R}^{n \times n}$: 대각 행렬(diagonal matrix)로, 대각 성분은 $\mathbf{A}$의 고윳값들로 구성됩니다.
- $\mathbf{V}^{-1}$: $\mathbf{V}$의 역행렬(inverse matrix).

이 때, 고유방정식(eigenvalue equation) $\mathbf{A}\mathbf{v} = \lambda \mathbf{v}$를 만족하는 $\lambda$는 고윳값, $\mathbf{v}$는 고유벡터입니다.

## 2. 대칭 행렬의 고윳값 분해

대칭 행렬(symmetric matrix) $\mathbf{A} = \mathbf{A}^\top$의 경우, 고윳값 분해는 특별한 성질을 가집니다:
- 고윳값은 모두 실수(real number)입니다.
- 고유벡터들은 서로 직교(orthogonal)하며, $\mathbf{V}$는 직교 행렬(orthogonal matrix)이 됩니다. 즉, $\mathbf{V}^{-1} = \mathbf{V}^\top$입니다.

따라서 대칭 행렬의 경우 고윳값 분해는 다음과 같이 표현됩니다:

$$
\mathbf{A} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^\top
$$

## 3. EVD의 응용

### 3.1. 주성분 분석 (Principal Component Analysis, PCA)

PCA는 고차원 데이터의 차원을 축소하는 데 사용되는 방법으로, 데이터의 공분산 행렬을 고윳값 분해하여 주성분(principal component)을 구합니다. 이 때 가장 큰 고윳값에 대응하는 고유벡터가 데이터의 가장 큰 변동성을 설명하는 축이 됩니다.

### 3.2. 행렬의 대각화

행렬 $\mathbf{A}$의 고윳값 분해를 통해 $\mathbf{A}$를 대각화(diagonalization)할 수 있습니다. 대각화된 행렬은 계산을 단순화하고, 행렬의 거듭제곱이나 지수 연산 등을 효율적으로 수행할 수 있게 합니다.

### 3.3. 차원 축소 및 데이터 분석

EVD는 데이터 분석에서 차원 축소, 데이터 압축, 신호 처리 등 다양한 응용에서 사용됩니다. 예를 들어, 데이터의 공분산 행렬을 고윳값 분해하면, 데이터의 주요 성분을 선택하여 노이즈를 줄이고, 중요한 특징만을 남길 수 있습니다.

## 4. 고윳값 분해의 한계

고윳값 분해는 모든 정방 행렬에 대해 항상 가능하지는 않습니다. 특히, 비대칭 행렬이나 복잡한 특성을 가진 행렬의 경우 고윳값이 복소수(complex number)가 될 수 있으며, 이 경우에는 고윳값 분해 대신 특이값 분해(Singular Value Decomposition, SVD)를 사용하는 것이 더 적합할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
