# 슈어 보수 (Schur Complement)

슈어 보수(Schur Complement)는 행렬 이론에서 중요한 개념으로, 주어진 블록 행렬(block matrix)의 특정 부분 행렬에 대한 보수 행렬(complement matrix)을 계산하는 방법입니다. 이 개념은 수치 선형 대수학, 확률론, 최적화 이론 등에서 매우 유용하게 사용됩니다.

## 1. 블록 행렬의 정의

슈어 보수를 정의하기 위해 먼저 블록 행렬을 고려합니다. 임의의 행렬 $\mathbf{M}$이 다음과 같이 네 개의 블록으로 구성된 $n \times n$ 행렬이라고 가정합시다:

$$
\mathbf{M} = \begin{pmatrix}
\mathbf{A} & \mathbf{B} \\
\mathbf{C} & \mathbf{D}
\end{pmatrix}
$$

여기서 $\mathbf{A}$는 $p \times p$ 행렬, $\mathbf{B}$는 $p \times q$ 행렬, $\mathbf{C}$는 $q \times p$ 행렬, $\mathbf{D}$는 $q \times q$ 행렬입니다.

## 2. 슈어 보수의 정의

블록 행렬 $\mathbf{M}$의 슈어 보수는 $\mathbf{A}$ 또는 $\mathbf{D}$를 기준으로 정의될 수 있습니다.

### $\mathbf{A}$에 대한 슈어 보수

만약 $\mathbf{A}$가 가역적(invertible)이라면, $\mathbf{D}$에 대한 $\mathbf{A}$의 슈어 보수는 다음과 같이 정의됩니다:

$$
\mathbf{S} = \mathbf{D} - \mathbf{C} \mathbf{A}^{-1} \mathbf{B}
$$

여기서 $\mathbf{S}$는 $\mathbf{D}$의 $\mathbf{A}$에 대한 슈어 보수(Schur complement of $\mathbf{D}$ with respect to $\mathbf{A}$)입니다.

### $\mathbf{D}$에 대한 슈어 보수

비슷하게, $\mathbf{D}$가 가역적이라면, $\mathbf{A}$에 대한 $\mathbf{D}$의 슈어 보수는 다음과 같이 정의됩니다:

$$
\mathbf{S}' = \mathbf{A} - \mathbf{B} \mathbf{D}^{-1} \mathbf{C}
$$

여기서 $\mathbf{S}'$는 $\mathbf{A}$의 $\mathbf{D}$에 대한 슈어 보수입니다.

## 3. 슈어 보수의 응용

### 3.1 행렬의 역 계산

블록 행렬의 역행렬은 슈어 보수를 통해 간단히 표현될 수 있습니다. 예를 들어, $\mathbf{A}$가 가역적이라면, $\mathbf{M}$의 역행렬은 다음과 같이 주어집니다:

$$
\mathbf{M}^{-1} = \begin{pmatrix}
\mathbf{A}^{-1} + \mathbf{A}^{-1} \mathbf{B} \mathbf{S}^{-1} \mathbf{C} \mathbf{A}^{-1} & -\mathbf{A}^{-1} \mathbf{B} \mathbf{S}^{-1} \\
-\mathbf{S}^{-1} \mathbf{C} \mathbf{A}^{-1} & \mathbf{S}^{-1}
\end{pmatrix}
$$

### 3.2 조건부 분포

확률론에서는 다변량 정규분포의 조건부 분포를 계산할 때 슈어 보수가 사용됩니다. 주어진 확률변수들의 공분산 행렬이 블록 행렬로 표현될 때, 특정 부분 행렬에 대한 조건부 분산은 슈어 보수를 통해 구할 수 있습니다.

### 3.3 행렬 부등식과 최적화

슈어 보수는 행렬 부등식에서 중요한 역할을 하며, 특히 반정확성(semi-definiteness) 문제에서 유용하게 사용됩니다. 또한, 최적화 문제에서 라그랑주 승수법을 이용한 문제 해법에 자주 등장합니다.

## 4. 슈어 보수의 성질

- **대칭성**: $\mathbf{M}$이 대칭 행렬일 경우, $\mathbf{S}$도 대칭 행렬이 됩니다.
- **양의 정부호성**: 만약 $\mathbf{M}$이 양의 정부호 행렬(positive definite matrix)이면, $\mathbf{S}$도 양의 정부호 행렬이 됩니다.
- **치환 불변성**: 슈어 보수는 행렬의 치환에 대해 불변 성질을 가집니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
