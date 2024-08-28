# 상호 정보 (Mutual Information)

**상호 정보(Mutual Information, MI)**는 두 확률 변수 간의 의존성을 측정하는 정보 이론적 개념입니다. 상호 정보는 두 변수 간에 공유되는 정보의 양을 나타내며, 한 변수를 알았을 때 다른 변수에 대한 불확실성이 얼마나 줄어드는지를 나타냅니다.

## 정의

상호 정보는 두 확률 변수 $X$와 $Y$에 대해 다음과 같이 정의됩니다:

$$
I(X; Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log \frac{p(x, y)}{p(x) p(y)}
$$

여기서:

- $p(x, y)$는 $X$와 $Y$의 **결합 확률 분포**,
- $p(x)$와 $p(y)$는 각각 $X$와 $Y$의 **주변 확률 분포**를 나타냅니다.

상호 정보는 다음과 같은 방식으로 해석할 수 있습니다:

- $I(X; Y)$가 **0**이면, $X$와 $Y$가 서로 독립임을 의미합니다. 즉, $X$에 대한 정보는 $Y$에 대해 아무런 정보를 제공하지 않습니다.
- $I(X; Y)$의 값이 클수록 $X$와 $Y$ 간의 의존성이 큽니다.

## 엔트로피와의 관계

상호 정보는 엔트로피와 밀접한 관련이 있습니다. 엔트로피 $H(X)$는 변수 $X$의 불확실성을 나타내는 반면, 상호 정보 $I(X; Y)$는 $X$와 $Y$ 간의 상호 의존성을 나타냅니다. 상호 정보는 다음과 같은 세 가지 표현으로 나타낼 수 있습니다:

1. **엔트로피의 합과 결합 엔트로피의 차이**로 표현:
   
   $$
   I(X; Y) = H(X) + H(Y) - H(X, Y)
   $$

2. **조건부 엔트로피의 차이**로 표현:

   $$
   I(X; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X)
   $$

3. **KL 발산을 통한 표현**:
   
   $$
   I(X; Y) = D_{KL}(p(x, y) \parallel p(x)p(y))
   $$

이 표현들은 각각 상호 정보가 $X$와 $Y$ 간의 정보 공유를 어떻게 측정하는지를 다양한 관점에서 설명해 줍니다.

## 응용

상호 정보는 통계적 모델링, 변수 선택, 그리고 신호 처리 등 다양한 분야에서 사용됩니다. 예를 들어, 피처 선택에서 상호 정보는 각 피처가 타겟 변수와 얼마나 관련이 있는지를 평가하는 데 유용하게 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
