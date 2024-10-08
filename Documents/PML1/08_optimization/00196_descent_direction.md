# 하강 방향 (Descent Direction)

최적화 문제에서 **하강 방향**(Descent Direction)은 목적 함수의 값을 줄이기 위해 사용되는 방향을 의미합니다. 최적화 알고리즘에서 해를 찾기 위해서는 현재 위치에서 목적 함수의 값을 감소시키는 방향으로 이동해야 하는데, 이때 이동할 수 있는 방향이 바로 하강 방향입니다.

## 1. 하강 방향의 정의

어떤 점 $x \in \mathbb{R}^n$에서 함수 $f(x)$의 하강 방향 $d \in \mathbb{R}^n$은 다음의 조건을 만족하는 방향입니다:

$$
\text{만약 } f'(x) \cdot d < 0 \text{이면, } d \text{는 하강 방향이다.}
$$

여기서 $f'(x)$는 $f(x)$의 그라디언트(gradient)를 의미하며, $\cdot$는 내적(inner product)을 나타냅니다.

### 1.1 하강 방향의 직관

- **그라디언트와 하강 방향**: 함수 $f(x)$의 그라디언트 $f'(x)$는 $f(x)$가 가장 빠르게 증가하는 방향을 가리킵니다. 따라서 하강 방향은 그라디언트의 반대 방향일 가능성이 큽니다.
- **양의 수 $\alpha$**: 일반적으로 $\alpha > 0$인 경우, $\alpha d$ 또한 하강 방향이 됩니다.

## 2. 하강 방향의 수학적 특징

하강 방향은 주어진 지점에서 목적 함수의 값을 감소시키기 위한 필수 조건입니다. 다음과 같은 상황에서 사용될 수 있습니다:

- **경사하강법(Gradient Descent)**: 경사하강법에서는 하강 방향으로 이동하여 목적 함수의 값을 최소화합니다. 경사하강법에서 하강 방향 $d$는 보통 그라디언트의 음수 방향인 $-f'(x)$로 설정됩니다.
  
  $$
  x_{k+1} = x_k - \alpha_k f'(x_k)
  $$

  여기서 $\alpha_k$는 스텝 크기(step size)입니다.

- **뉴턴 방법(Newton's Method)**: 뉴턴 방법에서는 하세 행렬(Hessian matrix)를 사용하여 하강 방향을 결정합니다. 이 방법은 그라디언트 기반의 방법보다 더 빠르게 수렴할 수 있습니다.

  $$
  d = -[H_f(x)]^{-1} f'(x)
  $$

  여기서 $H_f(x)$는 $f(x)$의 하세 행렬입니다.

## 3. 하강 방향의 역할

하강 방향은 최적화 문제를 해결하는 알고리즘의 핵심적인 요소로 작용합니다. 특히 비선형 최적화 문제에서는 다음과 같은 이유로 중요합니다:

- **수렴 속도 개선**: 하강 방향을 올바르게 선택하면 알고리즘의 수렴 속도를 크게 향상시킬 수 있습니다.
- **정확도 향상**: 하강 방향을 통해 목적 함수의 값을 지속적으로 줄여 최적해에 점점 더 가까워지게 됩니다.

## 4. 하강 방향의 실용적 적용

하강 방향은 다양한 최적화 알고리즘에서 중요한 역할을 합니다:

- **최소 제곱 문제**: 하강 방향은 최소 제곱 문제에서 잔차(residual)를 최소화하기 위한 방향으로 사용됩니다.
- **비제약 최적화**: 하강 방향은 비제약 최적화에서 목적 함수를 최소화하기 위한 기본적인 개념입니다.
- **제약 최적화**: 제약 조건이 있는 최적화 문제에서도 라그랑지 승수를 사용해 하강 방향을 정의할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
