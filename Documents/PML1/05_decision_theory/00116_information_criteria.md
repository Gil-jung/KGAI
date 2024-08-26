# 정보 기준 (Information Criteria)

## 개요
정보 기준(Information Criteria)은 통계 모델을 비교하고 선택하는 데 사용되는 방법론으로, 주어진 데이터에 대해 모델의 적합성과 복잡성을 균형 있게 평가합니다. 정보 기준은 주로 최대우도 추정(Maximum Likelihood Estimation, MLE)과 함께 사용되며, 모델이 얼마나 데이터를 잘 설명하는지를 평가하는 동시에 모델의 복잡성에 대한 벌점을 부과합니다. 대표적인 정보 기준으로는 **Akaike 정보 기준(AIC)**, **Bayesian 정보 기준(BIC)**, **Deviance Information Criterion(DIC)** 등이 있습니다.

## Akaike 정보 기준 (AIC)

Akaike 정보 기준(AIC)은 주어진 데이터에 대해 모델의 적합도와 모델의 복잡성을 함께 고려하는 방법입니다. AIC는 다음과 같이 정의됩니다:

$$
\text{AIC} = 2k - 2\ln(\hat{L})
$$

여기서 \( k \)는 모델의 자유도, 즉 추정된 파라미터의 수를 나타내고, \( \hat{L} \)는 최대우도 추정값입니다. AIC는 모델의 적합도가 높을수록, 즉 최대우도 추정값 \( \hat{L} \)이 클수록 낮아지며, 모델이 복잡할수록(즉, \( k \)가 클수록) 높아집니다. 따라서, AIC는 모델이 데이터에 잘 맞으면서도 불필요하게 복잡하지 않은 모델을 선택하는 데 도움을 줍니다.

## Bayesian 정보 기준 (BIC)

Bayesian 정보 기준(BIC)는 AIC와 유사하지만, 베이즈 접근법에 기반한 모델 선택 기준입니다. BIC는 다음과 같이 정의됩니다:

$$
\text{BIC} = \ln(n)k - 2\ln(\hat{L})
$$

여기서 \( n \)은 데이터의 샘플 수, \( k \)는 모델 파라미터의 수, \( \hat{L} \)는 최대우도 추정값입니다. BIC는 모델 복잡성에 대한 벌점을 AIC보다 더 강하게 부과하는 경향이 있습니다. 특히, 데이터 샘플 수 \( n \)이 증가할수록 BIC의 벌점 항이 커지므로, 복잡한 모델보다는 단순한 모델을 선호하게 됩니다.

## Deviance Information Criterion (DIC)

DIC는 Bayesian 모델에서 사용되는 정보 기준으로, 모델의 적합도와 복잡성을 동시에 평가합니다. DIC는 다음과 같이 정의됩니다:

$$
\text{DIC} = \overline{D(\theta)} + p_D
$$

여기서 \( \overline{D(\theta)} \)는 파라미터 \( \theta \)의 기대 deviance, \( p_D \)는 모델의 효과적 파라미터 수를 의미하는 deviance에 대한 복잡도 벌점입니다. DIC는 베이지안 접근법에서 파라미터에 대한 불확실성을 반영하여, 모델의 적합도를 평가합니다.

## 정보 기준의 비교 및 사용

AIC, BIC, DIC 모두 모델의 적합성과 복잡성을 동시에 고려하는 방법이지만, 각 기준은 모델의 복잡성에 대한 벌점 부과 방식이 다르므로, 서로 다른 상황에서 더 적합한 기준이 될 수 있습니다. 일반적으로 AIC는 비교적 작은 샘플 크기에서 잘 작동하며, BIC는 큰 샘플 크기에서 복잡성을 더 엄격하게 통제하려는 경우에 유리합니다. DIC는 베이지안 접근법을 사용한 모델 선택에서 활용됩니다.

### 모델 선택의 예시

모델 선택 문제에서 AIC와 BIC를 활용할 수 있습니다. 예를 들어, 두 모델 \( M_1 \)과 \( M_2 \)가 있다고 가정할 때, AIC와 BIC를 계산하여 값이 더 낮은 모델을 선택하게 됩니다. 각 정보 기준은 모델의 설명력과 복잡성 간의 균형을 맞추기 때문에, 최종적으로 일반화 성능이 우수한 모델을 선택하는 데 도움을 줍니다.

## 결론

정보 기준은 모델의 적합성과 복잡성을 고려하여 최적의 모델을 선택하는 데 중요한 도구입니다. AIC, BIC, DIC 등의 정보 기준은 각각의 모델 선택 기준에 따라 다른 모델을 선호할 수 있으며, 데이터의 특성과 모델의 목적에 맞게 적절한 기준을 선택하는 것이 중요합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
