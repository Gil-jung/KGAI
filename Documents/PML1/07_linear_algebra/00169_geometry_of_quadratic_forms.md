# 이차 형식의 기하학 (Geometry of Quadratic Forms)

이차 형식(quadratic form)은 선형 대수학과 기하학에서 중요한 개념으로, 특히 고차원 공간에서의 함수의 곡률(curvature)과 같은 기하학적 속성을 분석하는 데 사용됩니다. 이차 형식의 기하학적 의미는 함수의 성질을 이해하고, 최적화 문제나 분류 문제에서 중요한 역할을 합니다.

## 1. 이차 형식의 정의

이차 형식은 일반적으로 벡터 $\mathbf{x} \in \mathbb{R}^n$와 대칭 행렬 $\mathbf{A} \in \mathbb{R}^{n \times n}$에 대해 다음과 같이 정의됩니다:

$$
Q(\mathbf{x}) = \mathbf{x}^\top \mathbf{A} \mathbf{x}
$$

여기서:
- $\mathbf{x}^\top$는 벡터 $\mathbf{x}$의 전치(transpose)입니다.
- $\mathbf{A}$는 대칭 행렬로, 이 행렬의 특성에 따라 이차 형식의 기하학적 성질이 결정됩니다.

## 2. 이차 형식의 기하학적 의미

이차 형식의 기하학적 성질은 행렬 $\mathbf{A}$의 고윳값(eigenvalue)과 관련이 깊습니다. 이차 형식이 나타내는 곡면의 형태는 다음과 같은 고윳값의 부호에 따라 달라집니다:

### 2.1. 양의 정부호 (Positive Definite)

행렬 $\mathbf{A}$의 모든 고윳값이 양수이면, 이차 형식 $Q(\mathbf{x})$는 양의 정부호(positive definite)입니다. 이 경우, 곡면은 원점에서 볼록(convex)한 형태를 띠며, 이는 **타원체(ellipsoid)**를 나타냅니다.

$$
Q(\mathbf{x}) > 0 \quad \text{for all non-zero } \mathbf{x}
$$

### 2.2. 음의 정부호 (Negative Definite)

행렬 $\mathbf{A}$의 모든 고윳값이 음수이면, 이차 형식 $Q(\mathbf{x})$는 음의 정부호(negative definite)입니다. 이 경우 곡면은 원점에서 오목(concave)한 형태를 가지며, 이는 반타원체(hyperboloid)를 나타냅니다.

$$
Q(\mathbf{x}) < 0 \quad \text{for all non-zero } \mathbf{x}
$$

### 2.3. 부정부호 (Indefinite)

행렬 $\mathbf{A}$가 양수와 음수 고윳값을 모두 가지는 경우, 이차 형식은 부정부호(indefinite)입니다. 이 경우 곡면은 **쌍곡면(hyperbolic paraboloid)**의 형태를 가집니다.

### 2.4. 반정부호 (Semi-Definite)

행렬 $\mathbf{A}$가 0이 아닌 고윳값 중 양수와 0을 가지거나, 음수와 0을 가지는 경우, 이차 형식은 양의 반정부호(positive semi-definite) 또는 음의 반정부호(negative semi-definite)입니다. 이 경우 곡면은 평면에 근접하거나 평평한 부분을 포함할 수 있습니다.

$$
Q(\mathbf{x}) \geq 0 \quad \text{or} \quad Q(\mathbf{x}) \leq 0
$$

## 3. 이차 형식의 변환과 주축 정리

이차 형식의 기하학적 성질을 분석하기 위해 종종 주축 정리(Principal Axis Theorem)를 사용합니다. 이 정리는 임의의 이차 형식을 좌표 변환을 통해 대각 형태로 변환할 수 있음을 나타내며, 이 변환을 통해 이차 형식의 해석이 단순해집니다.

변환된 이차 형식은 다음과 같이 나타낼 수 있습니다:

$$
Q(\mathbf{y}) = \mathbf{y}^\top \mathbf{\Lambda} \mathbf{y}
$$

여기서 $\mathbf{\Lambda}$는 $\mathbf{A}$의 고윳값으로 구성된 대각 행렬입니다.

## 4. 응용: 이차 형식과 최적화 문제

이차 형식은 최적화 문제, 특히 이차 함수(quadratic function)를 최적화하는 문제에서 자주 등장합니다. 예를 들어, 목적 함수가 이차 형식으로 표현될 때, 이차 형식의 기하학적 성질을 활용해 함수의 극값을 찾는 방법이 있습니다. 양의 정부호인 경우 함수는 전역 최솟값(global minimum)을 가지며, 이는 최적화 문제의 중요한 해결 방법입니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
