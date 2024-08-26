# 정밀도-재현율 곡선 (Precision-Recall Curve)

## 개요

정밀도-재현율 곡선(Precision-Recall Curve, PR 곡선)은 이진 분류기의 성능을 평가하는 데 사용되는 도구 중 하나입니다. 특히 데이터가 불균형한 경우, 즉 한 클래스의 데이터 수가 다른 클래스보다 훨씬 많은 상황에서, PR 곡선은 ROC 곡선보다 더 유용할 수 있습니다. PR 곡선은 모델이 얼마나 정확하게 양성 클래스를 예측하고 탐지하는지를 시각화하는 데 중점을 둡니다.

## 용어 정의

- **정밀도 (Precision)**: 모델이 양성으로 예측한 샘플 중 실제로 양성인 샘플의 비율입니다.
  $$
  \text{Precision} = \frac{TP}{TP + FP}
  $$
  여기서 \( TP \)는 True Positive, \( FP \)는 False Positive입니다.

- **재현율 (Recall, True Positive Rate, TPR)**: 실제로 양성인 샘플 중에서 모델이 올바르게 양성으로 예측한 비율입니다.
  $$
  \text{Recall} = \frac{TP}{TP + FN}
  $$
  여기서 \( TP \)는 True Positive, \( FN \)은 False Negative입니다.

## PR 곡선의 구성

PR 곡선은 X축에 재현율(Recall), Y축에 정밀도(Precision)를 놓고, 모델의 임계값을 변화시키면서 그린 곡선입니다. PR 곡선은 다음과 같은 특성을 가지고 있습니다:

- **정밀도와 재현율의 트레이드오프**: 모델의 임계값을 낮추면 재현율이 증가하지만 정밀도가 감소할 수 있으며, 임계값을 높이면 정밀도는 증가하지만 재현율은 감소할 수 있습니다. PR 곡선은 이러한 트레이드오프를 시각적으로 보여줍니다.
  
- **곡선의 형태**: 데이터가 매우 불균형할 때, 높은 재현율을 유지하면서 정밀도를 높이기가 어려울 수 있습니다. 이 경우 PR 곡선이 왼쪽 상단에 가까울수록 좋은 성능을 나타냅니다.

## F1 Score

정밀도와 재현율 사이의 균형을 평가하기 위해 F1 스코어를 사용할 수 있습니다. F1 스코어는 정밀도와 재현율의 조화 평균(harmonic mean)으로 정의됩니다.
$$
\text{F1 Score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$
F1 스코어는 정밀도와 재현율이 비슷한 중요도를 가질 때 유용한 평가 지표입니다.

## PR 곡선과 ROC 곡선의 비교

PR 곡선과 ROC 곡선은 모두 이진 분류기의 성능을 평가하는 데 사용되지만, 그 적용 상황에 따라 장단점이 있습니다:

- **ROC 곡선**은 전체 클래스에 대해 균형 잡힌 데이터를 가정하며, 다양한 임계값에서의 모델 성능을 시각화합니다.
  
- **PR 곡선**은 불균형한 데이터에서 성능을 평가할 때 더 유용하며, 양성 클래스에 대한 예측의 정확성과 완전성을 강조합니다.

## 예시

예를 들어, 의료 진단에서 질병의 유무를 예측하는 모델이 있다고 가정해봅시다. 이때 질병이 있는 경우가 매우 드물다면, PR 곡선은 질병이 있는 환자를 얼마나 잘 탐지하면서도 건강한 사람들을 잘못 질병으로 진단하지 않는지를 평가하는 데 유용합니다.

## 결론

정밀도-재현율 곡선은 데이터가 불균형한 상황에서 이진 분류기의 성능을 평가하는 강력한 도구입니다. 정밀도와 재현율의 관계를 시각화함으로써 모델의 예측 능력을 보다 구체적으로 분석할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
