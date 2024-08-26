# 효과 크기에 대한 사후 추론 및 베이즈 유의도 검정

## 개요
효과 크기(effect size)는 두 그룹 간의 차이나 상관 관계의 강도를 나타내는 지표로, 통계적 검정의 결과가 실질적으로 얼마나 중요한지를 평가하는 데 사용됩니다. 베이즈 접근법에서는 효과 크기에 대한 사후 추론(posterior inference)을 통해 불확실성을 포함한 효과 크기의 분포를 추정할 수 있으며, 베이즈 유의도 검정(Bayesian Significance Testing)을 사용하여 가설 검정 문제를 해결할 수 있습니다.

## 효과 크기에 대한 사후 추론

베이즈 통계학에서 효과 크기에 대한 사후 추론은 데이터와 사전 정보(prior information)를 결합하여 효과 크기 분포의 사후 분포(posterior distribution)를 추정하는 과정입니다. 사후 분포는 베이즈 정리(Bayes' Theorem)를 통해 다음과 같이 계산됩니다:

$$
p(\theta \mid \text{data}) = \frac{p(\text{data} \mid \theta) p(\theta)}{p(\text{data})}
$$

여기서 \( \theta \)는 효과 크기를 나타내는 파라미터이며, \( p(\text{data} \mid \theta) \)는 데이터에 대한 우도(likelihood), \( p(\theta) \)는 사전 분포(prior distribution), \( p(\text{data}) \)는 데이터의 주변 분포(marginal distribution)입니다.

효과 크기에 대한 사후 분포는 특정 효과 크기 값이 주어진 데이터에서 얼마나 가능성이 있는지를 나타내며, 이는 불확실성을 포함하여 효과 크기를 추정하는 데 중요한 정보를 제공합니다. 예를 들어, 효과 크기의 신뢰 구간 대신 사후 분포를 사용하여 더 직접적인 추론을 할 수 있습니다.

## 베이즈 유의도 검정

베이즈 유의도 검정은 전통적인 빈도주의 통계에서의 p-value 대신 사용되는 베이즈적 방법입니다. 베이즈 유의도 검정은 특정 가설이 데이터에 의해 얼마나 지지되는지를 사후 확률로 표현합니다.

가령, \( H_0 \)와 \( H_1 \)이라는 두 가설이 있다고 가정하면, 베이즈 접근법에서는 사전 확률(prior probability)과 데이터에 기반한 우도를 결합하여 각각의 가설에 대한 사후 확률을 계산합니다:

$$
\text{Posterior Odds} = \frac{p(H_1 \mid \text{data})}{p(H_0 \mid \text{data})} = \frac{p(\text{data} \mid H_1) p(H_1)}{p(\text{data} \mid H_0) p(H_0)}
$$

이 때, 베이즈 요인(Bayes Factor)은 두 가설 간의 상대적 지지를 나타내며, 이는 다음과 같이 정의됩니다:

$$
\text{Bayes Factor} = \frac{p(\text{data} \mid H_1)}{p(\text{data} \mid H_0)}
$$

베이즈 요인이 1보다 크다면 \( H_1 \) 가설이 \( H_0 \)보다 더 데이터에 의해 지지됨을 의미하고, 1보다 작다면 그 반대입니다. 이 방법은 효과 크기뿐만 아니라 모델 비교나 가설 검정에도 널리 사용됩니다.

## 효과 크기와 베이즈 유의도 검정의 중요성

전통적인 빈도주의 접근법에서 p-value는 특정 임계값(예: 0.05)을 기준으로 통계적 유의성을 판단합니다. 그러나 이 방식은 연구자가 설정한 임의의 기준에 따라 결과를 해석하는 데 한계가 있을 수 있습니다. 반면에, 베이즈적 접근법은 데이터에 대한 확률적 해석을 제공하여 결과를 더 유연하고 직관적으로 해석할 수 있도록 합니다.

베이즈 접근법을 통해 효과 크기에 대한 사후 분포를 추정하면, 연구 결과의 불확실성을 반영한 보다 정교한 결론을 도출할 수 있습니다. 또한, 베이즈 유의도 검정을 통해 단순히 유의성을 판단하는 것이 아니라 가설의 상대적 지지를 평가할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
