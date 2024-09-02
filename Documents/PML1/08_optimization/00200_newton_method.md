# 뉴턴법 (Newton's Method)

**뉴턴법**(Newton's Method)은 최적화 문제에서 함수의 극값(최대값 또는 최소값)을 찾기 위해 사용하는 고전적인 방법 중 하나입니다. 이 방법은 주어진 함수의 이차 테일러 전개(Taylor expansion)를 기반으로, 최적화 문제를 반복적으로 해결하여 해를 구하는 방식입니다. 뉴턴법은 빠른 수렴 속도를 제공하며, 특히 함수가 충분히 매끄럽고, 2차 미분 가능하며, 초기 값이 최적해에 가까운 경우 매우 효율적입니다.

## 1. 기본 아이디어

뉴턴법은 다음과 같은 목표 함수를 고려합니다:

$$
f(\theta)
$$

여기서 $\theta$는 최적화하려는 파라미터 벡터입니다. 목표는 $f(\theta)$를 최소화하거나 최대화하는 $\theta$를 찾는 것입니다. 뉴턴법의 아이디어는 $f(\theta)$의 이차 테일러 전개를 사용하여 다음 반복 단계에서의 $\theta$ 값을 추정하는 것입니다.

## 2. 뉴턴법의 수식

먼저 $f(\theta)$를 $\theta$ 주변에서 테일러 전개하면 다음과 같이 나타낼 수 있습니다:

$$
f(\theta + \Delta \theta) \approx f(\theta) + \nabla_{\theta} f(\theta)^\top \Delta \theta + \frac{1}{2} \Delta \theta^\top H(\theta) \Delta \theta
$$

여기서:
- $\nabla_{\theta} f(\theta)$는 $\theta$에서의 함수 $f$의 기울기(Gradient)입니다.
- $H(\theta)$는 $\theta$에서의 함수 $f$의 헤세 행렬(Hessian matrix)입니다. 헤세 행렬은 이차 미분을 모아놓은 대칭 행렬로, $H(\theta) = \nabla_{\theta}^2 f(\theta)$로 표현됩니다.

뉴턴법은 이 테일러 전개에서 $\theta$의 다음 값을 추정하기 위해 다음과 같은 업데이트 규칙을 사용합니다:

$$
\theta_{t+1} = \theta_t - H(\theta_t)^{-1} \nabla_{\theta} f(\theta_t)
$$

이 식은 $t$번째 반복에서의 $\theta_t$ 값에서 기울기와 헤세 행렬을 사용해 $\theta_{t+1}$ 값을 계산하는 과정을 나타냅니다.

## 3. 뉴턴법의 특성

뉴턴법의 중요한 특성은 다음과 같습니다:

- **빠른 수렴 속도**: 뉴턴법은 일반적으로 이차 수렴(quadratic convergence)을 가지며, 초기 값이 최적해에 가깝다면 매우 빠르게 수렴합니다.
- **헤세 행렬 계산**: 헤세 행렬 $H(\theta)$를 계산하고, 이를 역행렬로 구하는 과정이 필요하므로 계산 복잡도가 높을 수 있습니다. 특히 고차원 문제에서 이 부분이 계산적으로 부담이 될 수 있습니다.
- **초기 값 의존성**: 초기 값이 최적해에 가까운 경우 매우 효율적이지만, 멀리 떨어져 있을 경우 국소 최적해에 빠지거나 수렴하지 않을 수도 있습니다.

## 4. 뉴턴법의 변형

### 준뉴턴법 (Quasi-Newton Methods)
헤세 행렬의 직접 계산이 어려운 경우, 준뉴턴법(Quasi-Newton Methods)이 사용될 수 있습니다. 이 방법들은 헤세 행렬의 근사치를 사용하여 뉴턴법의 효율성을 높이면서 계산 복잡도를 줄입니다. 대표적인 준뉴턴법으로는 BFGS(Broyden-Fletcher-Goldfarb-Shanno) 알고리즘이 있습니다.

### 댐프드 뉴턴법 (Damped Newton's Method)
헤세 행렬의 조건 수가 나쁘거나 함수가 비볼록(Non-convex)인 경우, 뉴턴법이 수렴하지 않거나 진동할 수 있습니다. 이를 방지하기 위해, 댐프드 뉴턴법(Damped Newton's Method)이 사용됩니다. 이 방법은 업데이트 단계에서 작은 스텝 크기(학습률)을 적용하여 수렴을 안정화합니다.

## 5. 뉴턴법의 적용

뉴턴법은 다양한 최적화 문제에 적용될 수 있으며, 특히 매끄러운(convex) 함수의 최적화에서 매우 효과적입니다. 그러나, 고차원 문제나 비선형 문제에서 헤세 행렬의 계산이 복잡해질 수 있으며, 이러한 경우 준뉴턴법과 같은 변형 기법이 자주 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
