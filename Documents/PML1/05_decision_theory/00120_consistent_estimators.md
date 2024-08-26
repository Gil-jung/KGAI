# 일치추정량 (Consistent Estimator)

## 개요

통계학에서 일치추정량은 샘플의 크기가 증가함에 따라, 추정하고자 하는 모수의 실제 값에 점점 더 가까워지는 추정량을 의미합니다. 일치추정량은 샘플 크기 \( n \) 이 무한히 커질 때, 추정량이 참값으로 수렴하는 중요한 속성을 갖습니다.

## 일치성의 정의

일치성은 추정량 \(\hat{\theta}_n\)이 샘플 크기 \( n \) 이 무한대로 갈 때, 모수 \(\theta\)에 수렴하는 성질을 말합니다. 수렴의 종류에 따라 약한 일치성과 강한 일치성으로 나눌 수 있습니다.

### 약한 일치성 (Weak Consistency)

약한 일치성은 추정량이 샘플 크기 \( n \) 이 커질수록 모수 \(\theta\)로 확률적으로 수렴하는 것을 의미합니다. 이는 다음과 같이 표현됩니다:

$$
\hat{\theta}_n \xrightarrow{P} \theta \quad \text{as} \quad n \rightarrow \infty
$$

여기서 \( \xrightarrow{P} \) 는 확률적 수렴을 나타내며, 이는 임의의 작은 양수 \( \epsilon \)에 대해 다음 조건이 성립함을 의미합니다:

$$
\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| > \epsilon) = 0
$$

즉, 추정량 \(\hat{\theta}_n\)이 실제 값 \(\theta\)와 \( \epsilon \) 범위 밖에 있을 확률이 \( n \) 이 증가함에 따라 0으로 수렴하는 것을 의미합니다.

### 강한 일치성 (Strong Consistency)

강한 일치성은 추정량이 거의 확실하게 모수 \(\theta\)로 수렴하는 것을 의미합니다. 이는 다음과 같이 표현됩니다:

$$
\hat{\theta}_n \xrightarrow{a.s.} \theta \quad \text{as} \quad n \rightarrow \infty
$$

여기서 \( \xrightarrow{a.s.} \) 는 거의 확실한 수렴(almost sure convergence)을 의미합니다. 이는 다음 조건이 성립함을 의미합니다:

$$
P\left(\lim_{n \to \infty} \hat{\theta}_n = \theta \right) = 1
$$

강한 일치성은 약한 일치성보다 더 강력한 조건으로, 추정량이 참값에 수렴하는 경향이 더 강하다는 것을 나타냅니다.

## 일치추정량의 예

- **평균의 추정**: 주어진 샘플 \(X_1, X_2, \dots, X_n\)에서 모집단의 평균 \(\mu\)를 추정하는 추정량 \(\hat{\mu}_n = \frac{1}{n} \sum_{i=1}^{n} X_i\)은 일치추정량입니다. 이는 대수의 법칙(Law of Large Numbers)에 의해 \(\hat{\mu}_n\)이 \(\mu\)에 수렴함을 보장합니다.

- **분산의 추정**: 모집단의 분산 \(\sigma^2\)에 대한 불편 추정량 \( \hat{\sigma}^2_n = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \hat{\mu}_n)^2 \) 역시 일치추정량입니다.

## 일치성의 중요성

일치성은 추정량의 중요한 속성 중 하나로, 샘플 크기가 충분히 클 때 추정량이 실제 모수를 잘 추정할 수 있음을 보장합니다. 이는 특히 샘플 크기가 크지 않은 상황에서도 일치성을 가지는 추정량이 신뢰할 수 있는 추정을 제공할 가능성이 높다는 점에서 중요합니다.

일치추정량은 샘플 크기가 증가할수록 더욱 정확해지므로, 모델 선택이나 추정 과정에서 필수적으로 고려해야 하는 요소입니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
