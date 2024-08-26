# ROC 곡선 (Receiver Operating Characteristic Curve)

## 개요

ROC 곡선(Receiver Operating Characteristic Curve)은 이진 분류기의 성능을 평가하는 데 사용되는 그래프입니다. 이 곡선은 다양한 임계값(threshold)에 대한 분류기의 민감도(Sensitivity)와 특이도(Specificity) 사이의 관계를 시각화합니다. ROC 곡선은 의료 진단, 신호 탐지 이론, 머신러닝 등의 다양한 분야에서 널리 사용됩니다.

## 용어 정의

- **민감도 (Sensitivity, True Positive Rate, TPR)**: 실제로 양성인 샘플 중에서 모델이 올바르게 양성으로 예측한 비율입니다.
  $$
  \text{TPR} = \frac{TP}{TP + FN}
  $$
  여기서 \( TP \)는 True Positive, \( FN \)은 False Negative입니다.

- **특이도 (Specificity, True Negative Rate, TNR)**: 실제로 음성인 샘플 중에서 모델이 올바르게 음성으로 예측한 비율입니다.
  $$
  \text{TNR} = \frac{TN}{TN + FP}
  $$
  여기서 \( TN \)은 True Negative, \( FP \)는 False Positive입니다.

- **1 - 특이도 (False Positive Rate, FPR)**: 실제로 음성인 샘플 중에서 모델이 잘못 양성으로 예측한 비율입니다.
  $$
  \text{FPR} = \frac{FP}{FP + TN}
  $$

## ROC 곡선의 구성

ROC 곡선은 X축에 False Positive Rate (FPR), Y축에 True Positive Rate (TPR)을 놓고, 분류기의 임계값을 조정하면서 그린 곡선입니다. 이 곡선은 다음과 같은 특성을 가집니다:

- **완벽한 분류기**는 (0, 1) 점을 지나며, 이 경우 FPR이 0이고 TPR이 1입니다. 이 점은 완벽한 분류기의 이상적인 성능을 나타냅니다.
- **무작위 분류기**는 대각선에 위치한 ROC 곡선을 가지며, 이는 모델이 무작위로 예측하고 있음을 나타냅니다.
- **우수한 분류기**는 ROC 곡선이 대각선 위에 위치하며, 곡선이 좌상단에 가까울수록 더 우수한 성능을 나타냅니다.

## AUC (Area Under the Curve)

AUC(Area Under the Curve)는 ROC 곡선 아래의 면적을 의미하며, 분류기의 전반적인 성능을 평가하는 지표로 사용됩니다. AUC 값은 0과 1 사이의 값을 가지며, 다음과 같은 의미를 가집니다:

- AUC = 1: 완벽한 분류기
- AUC = 0.5: 무작위 분류기
- AUC < 0.5: 모델이 데이터를 잘못 분류하고 있음

## 예시

예를 들어, 의료 진단에서 ROC 곡선을 통해 모델의 민감도와 특이도를 평가할 수 있습니다. 높은 민감도를 가진 모델은 질병이 있는 환자를 잘 탐지하지만, 특이도가 낮으면 건강한 사람들을 질병으로 잘못 예측할 수 있습니다. 반대로, 높은 특이도를 가진 모델은 건강한 사람들을 잘 예측하지만, 민감도가 낮으면 질병이 있는 환자를 놓칠 수 있습니다.

## 결론

ROC 곡선과 AUC는 이진 분류기의 성능을 평가하는 데 있어 중요한 도구입니다. ROC 곡선을 통해 분류기의 임계값에 따른 민감도와 특이도의 변화를 시각적으로 분석할 수 있으며, AUC를 통해 모델의 전반적인 성능을 수치화할 수 있습니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
