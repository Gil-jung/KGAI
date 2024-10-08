# 무상관은 독립을 뜻하지 않는다

확률 이론과 통계학에서, 두 확률 변수 간의 **무상관**(uncorrelated) 관계와 **독립**(independence) 관계는 다르게 해석됩니다. 무상관이란 두 변수 사이의 선형적 상관 관계가 없음을 의미하지만, 이는 반드시 두 변수가 독립적이라는 것을 의미하지 않습니다.

## 무상관의 정의

두 확률 변수 $X$와 $Y$가 **무상관**이라는 것은 다음 조건을 만족한다는 의미입니다:

$$
\text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] = 0
$$

여기서 $\text{Cov}(X, Y)$는 $X$와 $Y$의 공분산을 의미하며, 공분산이 0이면 두 변수 간의 선형적 관계가 없다는 것을 뜻합니다. 그러나 공분산이 0이라고 해서 두 변수가 독립적이라는 보장은 없습니다.

## 독립의 정의

두 확률 변수 $X$와 $Y$가 **독립**이라는 것은 $X$와 $Y$의 결합 분포가 각 변수의 개별 분포의 곱으로 표현된다는 것을 의미합니다:

$$
P(X = x, Y = y) = P(X = x)P(Y = y)
$$

독립적인 변수는 하나의 변수의 값이 다른 변수의 분포에 영향을 미치지 않음을 의미합니다.

## 무상관과 독립의 관계

- **독립 ⇒ 무상관**: 두 확률 변수가 독립적이면 항상 무상관입니다. 이는 두 변수 사이에 어떠한 형태의 관계도 없기 때문에 공분산이 0이 된다는 것을 의미합니다.
  
- **무상관 ≠ 독립**: 무상관인 두 변수는 선형적 관계가 없음을 의미할 뿐, 비선형적 관계는 존재할 수 있습니다. 즉, 비선형 관계가 존재하는 경우 두 변수는 여전히 무상관일 수 있지만 독립적이지 않을 수 있습니다.

### 예시

두 확률 변수 $X$와 $Y$가 다음과 같이 정의되어 있다고 가정합시다:
$$
Y = X^2
$$

이 경우, $X$와 $Y$의 공분산은 0일 수 있지만 $Y$는 여전히 $X$에 의존적이기 때문에 이 두 변수는 독립적이지 않습니다.

## 결론

무상관은 독립을 의미하지 않으며, 이는 특히 비선형 관계를 갖는 경우 두 변수 간의 상호작용을 이해할 때 중요합니다. 무상관 관계는 단지 선형 관계가 없음을 나타낼 뿐, 두 변수가 독립적이라는 강한 의미를 내포하지는 않습니다. 따라서 확률 변수 간의 관계를 정확히 파악하기 위해서는 무상관과 독립의 차이를 명확히 이해하고 분석해야 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
