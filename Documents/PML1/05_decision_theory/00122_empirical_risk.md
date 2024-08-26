# 경험적 위험 (Empirical Risk)

## 개요

경험적 위험(empirical risk)은 통계학 및 기계 학습에서 주어진 데이터셋에 대해 모델이 얼마나 잘 수행되는지를 측정하는 개념입니다. 이는 손실 함수의 평균값으로 정의되며, 모델이 학습 과정에서 최소화하려는 대상입니다. 경험적 위험은 실제 데이터에 대한 성능을 반영하기 때문에 학습 과정에서 중요한 역할을 합니다.

## 경험적 위험의 정의

경험적 위험은 주어진 데이터셋 \( \{(x_i, y_i)\}_{i=1}^n \)에 대해 모델 \( f(x; \theta) \)이 얼마나 잘 예측하는지를 측정하기 위해 손실 함수 \( L(y, f(x; \theta)) \)를 사용하여 정의됩니다. 여기서 \( \theta \)는 모델의 파라미터를 나타냅니다.

경험적 위험 \( R_{emp}(\theta) \)는 다음과 같이 정의됩니다:

$$
R_{emp}(\theta) = \frac{1}{n} \sum_{i=1}^n L(y_i, f(x_i; \theta))
$$

여기서 \( n \)은 데이터셋의 크기를 의미하며, 각 데이터 포인트 \( (x_i, y_i) \)에 대해 손실을 계산한 후, 그 평균을 구하는 방식으로 경험적 위험을 계산합니다.

## 손실 함수

손실 함수 \( L(y, f(x; \theta)) \)는 모델의 예측 \( f(x; \theta) \)과 실제 값 \( y \) 간의 차이를 측정하는 함수입니다. 자주 사용되는 손실 함수로는 다음이 있습니다:

- **제곱 오차 손실(Squared Error Loss)**: 회귀 문제에서 자주 사용되며, 예측 값과 실제 값 간의 차이를 제곱하여 손실을 계산합니다.

$$
L(y, f(x; \theta)) = (y - f(x; \theta))^2
$$

- **로지스틱 손실(Logistic Loss)**: 이진 분류 문제에서 자주 사용되며, 모델의 확률 예측과 실제 라벨 간의 로그 손실을 계산합니다.

$$
L(y, f(x; \theta)) = - \left[ y \log(f(x; \theta)) + (1-y) \log(1-f(x; \theta)) \right]
$$

## 경험적 위험 최소화

모델 학습의 목표는 경험적 위험을 최소화하는 파라미터 \( \theta \)를 찾는 것입니다. 이를 **경험적 위험 최소화(Empirical Risk Minimization, ERM)**라고 합니다. 경험적 위험을 최소화하기 위해 최적화 기법이 사용되며, 이는 모델이 주어진 데이터에 대해 최대한 잘 맞는 예측을 하도록 유도합니다.

$$
\hat{\theta} = \arg\min_{\theta} R_{emp}(\theta)
$$

하지만 경험적 위험 최소화는 과적합(overfitting)의 문제를 일으킬 수 있습니다. 이는 모델이 학습 데이터에 너무 잘 맞추어져, 새로운 데이터에 대해 일반화(generalization) 성능이 떨어지는 현상을 의미합니다.

## 일반화와 경험적 위험

경험적 위험과 모델의 일반화 성능은 서로 밀접하게 관련되어 있습니다. 경험적 위험은 학습 데이터셋에 대해 모델이 얼마나 잘 맞는지를 측정하지만, 진정한 목표는 **일반화 위험**(generalization risk) 또는 **진실 위험**(true risk)을 최소화하는 것입니다. 일반화 위험은 미지의 새로운 데이터에 대한 성능을 평가하며, 이는 다음과 같이 정의됩니다:

$$
R(\theta) = \mathbb{E}_{(x,y) \sim P} [L(y, f(x; \theta))]
$$

여기서 \( P \)는 데이터의 진짜 분포를 나타냅니다. 일반적으로, 경험적 위험은 일반화 위험의 추정치로 간주됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
