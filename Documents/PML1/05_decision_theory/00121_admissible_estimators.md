# 허용 가능 추정량 (Admissible Estimator)

## 개요

통계학에서 **허용 가능 추정량**은 선택된 손실 함수와 관련된 위험을 최소화하는 추정량입니다. 다른 추정량과 비교했을 때, 허용 가능 추정량은 주어진 손실 함수에 대해 더 나은 성능을 보이는 추정량이 존재하지 않는다는 것을 의미합니다. 이는 통계적 추론에서 추정량의 품질을 평가하는 중요한 개념입니다.

## 허용 가능 추정량의 정의

허용 가능 추정량의 개념은 손실 함수와 위험 함수에 의해 정의됩니다. 손실 함수 \( L(\theta, \hat{\theta}) \)는 실제 값 \( \theta \)와 추정량 \( \hat{\theta} \) 간의 차이에 따른 손실을 측정하며, 위험 함수 \( R(\theta, \hat{\theta}) \)는 손실 함수의 기댓값으로 정의됩니다:

$$
R(\theta, \hat{\theta}) = \mathbb{E}_{\theta} [L(\theta, \hat{\theta})]
$$

여기서 \( \mathbb{E}_{\theta} \)는 모수 \( \theta \)에 대한 기댓값을 의미합니다.

추정량 \( \hat{\theta}_1 \)이 허용 가능하다는 것은 임의의 다른 추정량 \( \hat{\theta}_2 \)에 대해 다음 조건이 성립함을 의미합니다:

$$
R(\theta, \hat{\theta}_2) \leq R(\theta, \hat{\theta}_1) \quad \text{for all} \quad \theta
$$

그리고 적어도 하나의 \( \theta \)에 대해 엄격한 부등식이 성립합니다:

$$
R(\theta, \hat{\theta}_2) < R(\theta, \hat{\theta}_1) \quad \text{for some} \quad \theta
$$

즉, \( \hat{\theta}_1 \)보다 \( \hat{\theta}_2 \)가 모든 경우에 대해 위험이 작거나 같으면서도, 일부 경우에는 더 작은 위험을 가지지 않으면, \( \hat{\theta}_1 \)은 허용 가능 추정량입니다.

## 허용 가능 추정량의 예

- **불편 추정량**: 불편 추정량이 허용 가능하지 않을 수 있습니다. 예를 들어, 최소제곱법(Least Squares Method)을 사용하는 선형 회귀 모델의 경우, 불편 추정량 대신 바이어스(bias)와 분산(variance) 사이의 트레이드오프를 고려한 추정량이 허용 가능할 수 있습니다.

- **베이즈 추정량**: 베이즈 추정량은 자주 허용 가능 추정량이 됩니다. 베이즈 추정량은 사전 확률(prior distribution)과 사후 확률(posterior distribution)에 기반하여 계산되며, 이는 주어진 데이터와 사전 정보에 최적화된 방식으로 위험을 최소화하기 때문입니다.

## 허용 가능 추정량의 중요성

허용 가능 추정량은 실용적인 측면에서 매우 중요합니다. 이는 추정 문제에서 선택할 수 있는 최적의 추정량을 식별할 수 있는 방법을 제공합니다. 허용 가능하지 않은 추정량은 대체로 더 나은 성능을 가진 추정량으로 대체될 수 있으므로, 이러한 추정량을 피하는 것이 바람직합니다.

허용 가능 추정량은 베이즈 결정 이론이나 빈도주의적 접근법에서도 중요한 개념으로 사용되며, 다양한 통계적 모델에서 최적의 추정 방법을 탐색하는 데 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
