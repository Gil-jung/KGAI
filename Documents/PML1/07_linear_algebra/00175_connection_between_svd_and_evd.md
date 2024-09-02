# SVD와 EVD 사이의 관계

특이값 분해(Singular Value Decomposition, SVD)와 고유값 분해(Eigenvalue Decomposition, EVD)는 선형대수에서 중요한 역할을 하는 두 가지 행렬 분해 방법입니다. 이 두 방법은 본질적으로 서로 밀접하게 관련되어 있으며, 행렬의 구조와 성질을 이해하는 데 유용한 도구로 사용됩니다.

## 1. 고유값 분해 (Eigenvalue Decomposition, EVD)
고유값 분해는 정방행렬(square matrix)에 적용되는 분해 방법으로, 행렬 $A$를 다음과 같이 분해할 수 있습니다:

$$
A = V \Lambda V^{-1}
$$

여기서:
- $A$는 $n \times n$ 정방행렬입니다.
- $V$는 $A$의 고유벡터(eigenvectors)로 구성된 행렬입니다.
- $\Lambda$는 대각행렬(diagonal matrix)로, 대각 원소는 $A$의 고유값(eigenvalues)입니다.

EVD는 주로 대칭행렬, 직교행렬, 또는 Hermitian 행렬 등 특정 유형의 행렬에 대해 정의됩니다.

## 2. 특이값 분해 (Singular Value Decomposition, SVD)
특이값 분해는 임의의 $m \times n$ 행렬 $A$에 대해 다음과 같은 분해를 제공합니다:

$$
A = U \Sigma V^T
$$

여기서:
- $U$는 $m \times m$ 단위직교행렬(unitary orthogonal matrix)로, $A$의 좌특이벡터(left singular vectors)로 구성됩니다.
- $\Sigma$는 $m \times n$ 대각행렬로, 대각 원소는 $A$의 특이값(singular values)입니다.
- $V^T$는 $n \times n$ 단위직교행렬로, $A$의 우특이벡터(right singular vectors)로 구성됩니다.

SVD는 정방행렬뿐만 아니라 임의의 행렬에 대해 정의되며, 고유값 분해보다 일반화된 형태로 볼 수 있습니다.

## 3. SVD와 EVD의 관계
특정한 조건에서, SVD와 EVD는 밀접한 관계를 가집니다. 예를 들어, $A$가 대칭행렬인 경우 SVD와 EVD는 동일한 형태로 나타날 수 있습니다. 이때, 행렬 $A$의 SVD는 다음과 같은 형태를 가집니다:

$$
A = U \Sigma U^T
$$

이는 $A = U \Lambda U^T$로 나타나는 고유값 분해와 유사합니다. 여기서 $\Sigma$의 대각 원소는 $\Lambda$의 대각 원소(고유값)의 절댓값이며, $U$는 $A$의 고유벡터로 구성됩니다.

따라서, **SVD는 EVD의 일반화된 형태**로 이해할 수 있으며, 대칭 행렬의 경우 두 분해 방법이 동일한 결과를 나타냅니다. 비대칭 행렬의 경우 SVD는 EVD보다 더 넓은 범위에서 적용 가능하며, 모든 행렬에 대해 SVD가 존재합니다.

## 4. 결론
SVD와 EVD는 모두 행렬의 분해를 통한 행렬의 특성을 분석하는 강력한 도구입니다. SVD는 EVD의 일반화된 형태로, 대칭 행렬에 대해 동일한 결과를 제공하며, 임의의 행렬에 대해 항상 정의됩니다. 이 둘의 관계를 이해함으로써 다양한 행렬의 특성과 성질을 더 깊이 있게 분석할 수 있습니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
