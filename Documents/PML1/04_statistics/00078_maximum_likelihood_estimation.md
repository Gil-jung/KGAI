# 최대 가능도 추정 (Maximum Likelihood Estimation, MLE)

최대 가능도 추정(MLE)은 주어진 데이터로부터 모형의 매개변수를 추정하는 강력한 통계적 방법입니다. MLE는 주어진 데이터 세트가 관측될 가능도를 최대화하는 매개변수를 선택함으로써, 데이터가 주어진 모형에 의해 가장 잘 설명될 수 있도록 합니다.

## 1. 기본 원리

주어진 데이터 세트 $X = \{x_1, x_2, \dots, x_n\}$가 있고, 이 데이터가 매개변수 $\theta$를 가지는 확률 분포 $P(X|\theta)$를 따른다고 가정합니다. 여기서 $X$는 관측된 데이터이며, $\theta$는 우리가 추정하고자 하는 모형의 매개변수입니다.

최대 가능도 추정의 목표는 주어진 데이터 $X$가 관측될 가능도(likelihood)를 최대화하는 매개변수 $\theta$를 찾는 것입니다. 가능도 함수는 다음과 같이 정의됩니다:

$$
L(\theta; X) = P(X|\theta)
$$

이 함수는 $\theta$에 대한 함수로서, 주어진 데이터 $X$가 주어졌을 때 $\theta$의 값에 따른 데이터의 가능도를 나타냅니다.

## 2. 로그 가능도 함수

계산의 편의를 위해, 가능도 함수의 로그를 취한 로그 가능도(log-likelihood)를 사용하는 것이 일반적입니다. 로그 가능도 함수는 다음과 같이 정의됩니다:

$$
\ell(\theta; X) = \log L(\theta; X) = \log P(X|\theta)
$$

로그 가능도는 가능도와 동일한 극값을 가지므로, 로그 가능도를 최대화하는 $\theta$를 찾는 것이 가능도를 최대화하는 것과 동일합니다.

## 3. MLE의 계산

MLE는 로그 가능도 함수를 $\theta$에 대해 최대화하는 $\theta$를 찾는 문제로 귀결됩니다. 즉, 로그 가능도 함수의 $\theta$에 대한 도함수를 구하고, 이를 0으로 설정하여 $\theta$의 최적 값을 찾습니다:

$$
\frac{\partial \ell(\theta; X)}{\partial \theta} = 0
$$

이 방정식을 풀어 $\theta$의 값을 찾으면, 이 값이 최대 가능도 추정치가 됩니다.

## 4. 예제: 정규 분포의 MLE

정규 분포 $\mathcal{N}(\mu, \sigma^2)$를 예로 들어, 평균 $\mu$와 분산 $\sigma^2$의 최대 가능도 추정치를 구해보겠습니다. 정규 분포에서 각 데이터 포인트 $x_i$에 대한 확률 밀도 함수는 다음과 같습니다:

$$
P(x_i|\mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)
$$

데이터 세트 $X = \{x_1, x_2, \dots, x_n\}$의 전체 가능도는 개별 데이터 포인트의 가능도의 곱으로 주어집니다:

$$
L(\mu, \sigma^2; X) = \prod_{i=1}^{n} P(x_i|\mu, \sigma^2)
$$

이 식의 로그를 취하면 로그 가능도 함수는 다음과 같습니다:

$$
\ell(\mu, \sigma^2; X) = -\frac{n}{2} \log(2\pi\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2
$$

이제, $\mu$와 $\sigma^2$에 대해 로그 가능도를 최대화하는 값을 구할 수 있습니다. 먼저, $\mu$에 대한 도함수를 구하고 이를 0으로 설정하여 $\mu$의 최적 값을 찾습니다:

$$
\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2} \sum_{i=1}^{n} (x_i - \mu) = 0
$$

이 방정식을 풀면, $\mu$의 최대 가능도 추정치는 다음과 같이 주어집니다:

$$
\hat{\mu} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

마찬가지로, $\sigma^2$에 대한 도함수를 구하고 이를 0으로 설정하여 $\sigma^2$의 최적 값을 찾습니다:

$$
\frac{\partial \ell}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4} \sum_{i=1}^{n} (x_i - \mu)^2 = 0
$$

이 방정식을 풀면, $\sigma^2$의 최대 가능도 추정치는 다음과 같습니다:

$$
\hat{\sigma}^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{\mu})^2
$$

이 결과는 데이터의 표본 평균과 표본 분산과 동일합니다.

## 5. MLE의 성질

최대 가능도 추정은 다음과 같은 성질을 가집니다:

- **일관성(Consistency)**: 표본 크기 $n$이 무한대로 증가할 때, MLE는 참 매개변수 값에 수렴합니다.
- **불편성(Unbiasedness)**: 충분한 표본 크기에서 MLE는 불편 추정치가 될 수 있습니다.
- **효율성(Efficiency)**: MLE는 최소 분산을 가지는 최적 추정량을 제공합니다.

이러한 성질들로 인해, MLE는 다양한 통계 및 기계 학습 문제에서 널리 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
