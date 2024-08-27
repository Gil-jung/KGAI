# KL 발산과 최대우도추정법 (MLE)

## 개요

KL 발산(Kullback-Leibler Divergence)과 최대우도추정법(MLE, Maximum Likelihood Estimation)은 통계적 학습과 정보 이론에서 중요한 개념으로, 서로 밀접하게 연관되어 있습니다. KL 발산은 두 확률 분포 간의 차이를 측정하는 도구로, 정보 손실의 척도 역할을 하며, MLE는 주어진 데이터로부터 모델의 파라미터를 추정하는 방법론입니다. 이 두 개념은 본질적으로 같은 목표를 가지고 있으며, 그 관계를 이해하는 것은 통계적 모델링의 기초를 이해하는 데 필수적입니다.

## 1. **KL 발산의 정의**

KL 발산은 두 확률 분포 $P$와 $Q$ 사이의 차이를 측정하는 비대칭 척도로 정의됩니다:

$$
D_{KL}(P \parallel Q) = \int p(x) \log \left(\frac{p(x)}{q(x)}\right) dx
$$

여기서 $p(x)$는 실제 데이터 분포(참 분포)이고, $q(x)$는 모델이 예측하는 분포입니다. KL 발산은 $P$로부터 $Q$로 얼마나 정보가 손실되는지를 나타내며, $D_{KL}(P \parallel Q) = 0$일 때, 두 분포는 동일합니다.

## 2. **최대우도추정법(MLE)의 정의**

최대우도추정법(MLE)은 주어진 데이터 집합에 대해 가장 높은 우도를 가지는 모델 파라미터를 찾는 방법입니다. 즉, 데이터 $X = \{x_1, x_2, \dots, x_n\}$에 대해, 모델 파라미터 $\theta$를 다음과 같이 선택합니다:

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}} \; \prod_{i=1}^{n} p(x_i \mid \theta)
$$

이를 로그우도 함수로 변환하면:

$$
\hat{\theta}_{MLE} = \underset{\theta}{\text{argmax}} \; \sum_{i=1}^{n} \log p(x_i \mid \theta)
$$

여기서 $p(x_i \mid \theta)$는 데이터 $x_i$가 주어진 파라미터 $\theta$ 하에서 관찰될 확률입니다.

## 3. **KL 발산과 MLE의 관계**

KL 발산과 MLE는 서로 밀접하게 연결되어 있으며, MLE는 KL 발산을 최소화하는 방향으로 작동합니다. 구체적으로, 모델 $Q$를 파라미터 $\theta$로 표현하고 참 분포 $P$를 실제 데이터 분포로 표현할 때, KL 발산을 최소화하는 $\theta$는 MLE를 수행하는 것과 동일합니다.

### **유도 과정**

KL 발산을 최소화하는 $\theta$를 찾는 문제를 살펴보면:

$$
\hat{\theta} = \underset{\theta}{\text{argmin}} \; D_{KL}(P \parallel Q_\theta)
$$

KL 발산의 정의를 적용하면:

$$
\hat{\theta} = \underset{\theta}{\text{argmin}} \; \int p(x) \log \left(\frac{p(x)}{q(x \mid \theta)}\right) dx
$$

이는 다음과 같이 정리됩니다:

$$
\hat{\theta} = \underset{\theta}{\text{argmin}} \; \int p(x) \log p(x) dx - \int p(x) \log q(x \mid \theta) dx
$$

첫 번째 항은 $\theta$와 무관하므로 무시할 수 있고, 결과적으로 MLE와 같은 형태가 됩니다:

$$
\hat{\theta} = \underset{\theta}{\text{argmax}} \; \int p(x) \log q(x \mid \theta) dx
$$

이 식은 MLE가 KL 발산을 최소화하는 방식으로 작동함을 보여줍니다.

## 4. **실제 적용과 중요성**

- **모델 적합성**: KL 발산과 MLE의 관계를 이해하면, 모델이 데이터에 얼마나 잘 적합하는지 평가할 수 있습니다. MLE가 데이터를 잘 설명하는 파라미터를 찾는 과정이 곧 KL 발산을 최소화하는 과정임을 알 수 있습니다.
- **모델 선택**: MLE를 통해 추정된 파라미터가 KL 발산을 최소화할 때, 이는 주어진 데이터에 가장 적합한 모델임을 의미합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
