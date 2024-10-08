# 베타 분포 (Beta Distribution)

## 개요
베타 분포는 연속 확률 분포 중 하나로, 주로 베이지안 통계에서 확률이나 비율의 사전 분포로 사용됩니다. 이 분포는 0과 1 사이의 값을 가지며, 두 매개변수 $ \alpha $와 $ \beta $에 의해 형태가 결정됩니다. 이러한 특성으로 인해 베타 분포는 성공 확률의 분포를 모델링할 때 매우 유용합니다.

## 수학적 정의
베타 분포의 확률 밀도 함수(PDF)는 다음과 같이 정의됩니다:

$$
f(x|\alpha, \beta) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{B(\alpha, \beta)}, \quad 0 \leq x \leq 1
$$

여기서:
- $ \alpha > 0 $ 및 $ \beta > 0 $는 형태 모수(shape parameters)입니다.
- $ B(\alpha, \beta) $는 베타 함수로, 다음과 같이 정의됩니다:
  
  $$
  B(\alpha, \beta) = \int_0^1 t^{\alpha-1} (1-t)^{\beta-1} dt
  $$

이 함수는 $ \alpha $와 $ \beta $의 값에 따라 다양한 형태의 분포를 가지며, 이로 인해 다양한 상황에 적합한 모델링이 가능합니다.

## 베타 분포의 특징
- **유연성**: $ \alpha $와 $ \beta $ 매개변수를 조정함으로써 베타 분포는 다양한 형태를 취할 수 있습니다. 예를 들어, $ \alpha = \beta = 1 $일 때는 균등 분포(Uniform distribution)와 동일해집니다.
- **사전 분포(Prior Distribution)**: 베이지안 추론에서 베타 분포는 이항 분포의 성공 확률에 대한 사전 분포로 자주 사용됩니다.
- **확률 밀도 함수의 해석**: $ \alpha - 1 $과 $ \beta - 1 $는 각각 성공과 실패의 횟수와 관련된 모수로 해석될 수 있으며, 이는 데이터에 대한 사전 지식을 반영합니다.

## 응용
베타 분포는 주로 다음과 같은 분야에서 사용됩니다:
1. **베이지안 통계**: 베타 분포는 이항 분포의 사전 분포로 사용되며, 예측 모델의 성공 확률에 대한 불확실성을 모델링하는 데 매우 유용합니다.
2. **머신러닝**: 분류 문제에서 클래스 확률을 모델링할 때 사용될 수 있으며, 샘플링 기반 알고리즘의 성능을 평가하는 데도 사용됩니다.
3. **신뢰 구간의 설정**: 베타 분포는 확률 변수가 특정 구간 내에 있을 확률을 계산하는 데 유용하며, 특히 비율의 신뢰 구간을 추정하는 데 사용됩니다.

## 베타 분포의 시각화
베타 분포는 $ \alpha $와 $ \beta $의 값에 따라 다양한 형태를 가지며, 특정한 경우에 따라 대칭적이거나 비대칭적일 수 있습니다. 예를 들어:
- $ \alpha = \beta $일 경우, 베타 분포는 대칭적입니다.
- $ \alpha > \beta $일 경우, 분포는 1에 치우칩니다.
- $ \alpha < \beta $일 경우, 분포는 0에 치우칩니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
