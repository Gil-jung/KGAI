# 행렬의 속성

행렬은 수학과 공학에서 널리 사용되는 도구로, 다양한 속성을 가지고 있습니다. 이 속성들은 행렬 연산, 선형 변환, 그리고 데이터 분석에 중요한 역할을 합니다. 이 문서에서는 주요 행렬의 속성들을 다루며, 각각의 개념을 쉽게 이해할 수 있도록 설명합니다.

## 1. 대각행렬 (Diagonal Matrix)

대각행렬은 주대각선 요소를 제외한 나머지 요소가 모두 0인 행렬입니다. $n \times n$ 행렬 $D$가 대각행렬이라면, $D_{ij} = 0$ (단, $i \neq j$)입니다. 대각행렬의 예시는 다음과 같습니다:

$$
D = \begin{pmatrix}
d_1 & 0 & \cdots & 0 \\
0 & d_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_n
\end{pmatrix}
$$

### 대각행렬의 특성:
- 대각행렬의 역행렬도 대각행렬입니다. 이 경우, 각 대각 요소의 역수가 역행렬의 대각 요소가 됩니다.
- 대각행렬의 행렬식은 모든 대각 요소의 곱입니다.

## 2. 대칭행렬 (Symmetric Matrix)

대칭행렬은 전치행렬과 자신이 동일한 행렬을 의미합니다. 즉, $A$가 대칭행렬이라면, $A = A^T$입니다. 대칭행렬은 다음과 같은 특성을 가집니다:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{12} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{1n} & a_{2n} & \cdots & a_{nn}
\end{pmatrix}
$$

### 대칭행렬의 특성:
- 대칭행렬의 고유값은 항상 실수입니다.
- 대칭행렬은 항상 직교대각화가 가능합니다. 즉, 직교행렬 $Q$와 대각행렬 $\Lambda$가 존재하여 $A = Q\Lambda Q^T$로 표현할 수 있습니다.

## 3. 직교행렬 (Orthogonal Matrix)

행렬 $Q$가 직교행렬이라면, $Q^T Q = I$ (단위행렬)입니다. 즉, 직교행렬의 역행렬은 전치행렬과 같습니다. 직교행렬은 다음과 같이 표현될 수 있습니다:

$$
Q = \begin{pmatrix}
q_{11} & q_{12} & \cdots & q_{1n} \\
q_{21} & q_{22} & \cdots & q_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
q_{n1} & q_{n2} & \cdots & q_{nn}
\end{pmatrix}
$$

### 직교행렬의 특성:
- 직교행렬의 열벡터들은 서로 직교하고, 단위벡터입니다.
- 직교행렬의 행렬식은 $\pm 1$입니다.

## 4. 특이행렬 (Singular Matrix)와 비특이행렬 (Non-Singular Matrix)

행렬이 **특이행렬**이라면, 그 행렬은 역행렬이 존재하지 않습니다. 즉, 행렬식이 0인 경우입니다. 반대로, **비특이행렬**은 행렬식이 0이 아니며, 역행렬이 존재합니다.

### 특이행렬의 특성:
- 특이행렬은 선형종속성을 가지며, 행렬의 열벡터들이 서로 독립적이지 않습니다.
- 비특이행렬은 선형독립성을 가지며, 고유값이 모두 0이 아닙니다.

## 5. 양의 정부호 행렬 (Positive Definite Matrix)

양의 정부호 행렬은 모든 비제로 벡터 $x$에 대해 $x^T A x > 0$을 만족하는 대칭행렬 $A$를 말합니다. 이러한 행렬은 다음과 같은 특성을 가집니다:

### 양의 정부호 행렬의 특성:
- 모든 고유값이 양수입니다.
- $A$가 양의 정부호 행렬이라면, $x^T A x = 0$일 때, $x = 0$입니다.

## 6. 특이값 분해 (Singular Value Decomposition, SVD)

특이값 분해는 임의의 $m \times n$ 행렬 $A$를 세 행렬 $U \Sigma V^T$로 분해하는 방법입니다. 여기서 $U$와 $V$는 직교행렬이고, $\Sigma$는 대각행렬입니다. 특이값 분해는 다음과 같은 특성을 가집니다:

$$
A = U \Sigma V^T
$$

### 특이값 분해의 특성:
- $\Sigma$의 대각선 요소들은 $A$의 특이값입니다.
- 특이값 분해는 행렬의 순위를 계산하거나, 근사 행렬을 구하는 데 유용하게 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
