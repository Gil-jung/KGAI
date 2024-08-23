# 로그 분할 함수는 누율 생성 함수다

**로그 분할 함수**(log-partition function)와 **누율 생성 함수**(cumulant generating function)는 확률 분포, 특히 **지수족**(exponential family) 분포에서 중요한 역할을 합니다. 이 두 개념은 수학적으로 동일하며, 서로 밀접하게 연결되어 있습니다.

## 1. 지수족 분포와 로그 분할 함수

지수족 분포는 다음과 같은 형태로 표현됩니다:

$$
p(x|\theta) = h(x) \exp \left( \eta(\theta)^T T(x) - A(\theta) \right)
$$

여기서 $ A(\theta) $가 바로 **로그 분할 함수**입니다. 이 함수는 확률 밀도 함수가 올바르게 정규화되도록 보장하는 역할을 합니다. 즉, 모든 가능한 $x$에 대해 확률이 합이 1이 되도록 조정합니다.

로그 분할 함수는 다음과 같이 정의됩니다:

$$
A(\theta) = \log \left( \int h(x) \exp \left( \eta(\theta)^T T(x) \right) dx \right)
$$

이 함수는 $\theta$의 함수로, 지수족 분포의 자연 모수와 밀접하게 관련되어 있습니다.

## 2. 누율 생성 함수로서의 로그 분할 함수

로그 분할 함수는 **누율 생성 함수**(cumulant generating function)와 동일한 역할을 합니다. 누율 생성 함수는 확률 변수의 누적적 통계량(평균, 분산, 왜도 등)을 생성하는 데 사용됩니다. 이 함수는 다음과 같이 정의됩니다:

$$
K(\eta) = \log \mathbb{E} \left[ \exp(\eta^T X) \right]
$$

여기서 $K(\eta)$는 **누율 생성 함수**이고, $X$는 확률 변수입니다. $\eta$는 자연 모수로, 지수족 분포에서는 이 함수가 바로 로그 분할 함수와 동일합니다. 따라서,

$$
A(\theta) = K(\eta(\theta))
$$

즉, 로그 분할 함수 $A(\theta)$는 누율 생성 함수 $K(\eta)$와 동일한 역할을 하며, 이는 지수족 분포의 자연 모수 $\eta(\theta)$와 관련된 확률 변수의 누적적 통계량을 생성합니다.

## 3. 로그 분할 함수의 성질

로그 분할 함수는 다음과 같은 중요한 성질을 가지고 있습니다:

- **평균 계산**: 로그 분할 함수 $A(\theta)$의 1차 도함수는 기대값(평균)을 나타냅니다.
  
  $$
  \frac{\partial A(\theta)}{\partial \eta} = \mathbb{E}[T(X)]
  $$

- **분산 계산**: 로그 분할 함수의 2차 도함수는 분산을 나타냅니다.

  $$
  \frac{\partial^2 A(\theta)}{\partial \eta^2} = \text{Var}(T(X))
  $$

이처럼 로그 분할 함수는 지수족 분포의 자연 모수와 관련된 중요한 통계적 특성을 결정하는 역할을 합니다.

## 4. 결론

로그 분할 함수는 지수족 분포에서 확률 밀도 함수의 정규화를 보장하는 동시에, 누율 생성 함수로서의 역할을 통해 확률 변수의 누적적 통계량을 계산하는 데 사용됩니다. 이 두 개념이 동일하다는 사실은 지수족 분포를 이해하는 데 중요한 통찰을 제공합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
