# 확률 변수의 변환

## 개요
확률 변수의 변환은 주어진 확률 변수에 대해 새로운 함수적 관계를 정의하여 다른 확률 변수를 생성하는 과정입니다. 이 과정은 통계학, 확률론, 머신러닝 등 다양한 분야에서 자주 활용됩니다. 변환된 확률 변수의 분포는 원래의 확률 변수의 분포와 변환 함수의 형태에 따라 결정됩니다.

## 확률 변수 변환의 수학적 정의

### 1. 단일 확률 변수 변환
주어진 확률 변수 \( X \)와 함수 \( g(X) \)에 대해, 새로운 확률 변수 \( Y = g(X) \)가 정의됩니다. 이때, \( Y \)의 확률 밀도 함수 \( f_Y(y) \)는 다음과 같이 계산됩니다:

\[
f_Y(y) = f_X(x) \left| \frac{dx}{dy} \right|
\]

여기서 \( x \)는 \( g(X) = y \)를 만족하는 \( X \)의 값이며, \( f_X(x) \)는 원래 확률 변수 \( X \)의 확률 밀도 함수입니다.

### 2. 다변량 확률 변수 변환
다변량 확률 변수 \( \mathbf{X} = (X_1, X_2, \ldots, X_n) \)의 경우, 함수 \( \mathbf{Y} = g(\mathbf{X}) \)에 의해 변환된 확률 변수 \( \mathbf{Y} = (Y_1, Y_2, \ldots, Y_m) \)의 확률 밀도 함수는 다음과 같이 계산됩니다:

\[
f_\mathbf{Y}(\mathbf{y}) = f_\mathbf{X}(\mathbf{x}) \left| \det \left( \frac{\partial \mathbf{x}}{\partial \mathbf{y}} \right) \right|
\]

여기서 \( \frac{\partial \mathbf{x}}{\partial \mathbf{y}} \)는 자코비안 행렬(Jacobian matrix)입니다.

## 확률 변수 변환의 활용

### 1. 정규화(Normalization)
정규화는 데이터를 일정한 범위로 변환하여 계산의 안정성을 확보하는 과정입니다. 예를 들어, 표준 정규 분포로 변환하기 위해서는 평균을 0으로, 분산을 1로 변환하는 작업이 필요합니다.

### 2. 로그 변환(Log Transformation)
로그 변환은 데이터의 분포가 비대칭일 때, 이를 더 대칭적인 분포로 변환하기 위해 사용됩니다. 이는 특히 지수적으로 증가하는 데이터를 선형적인 관계로 변환할 때 유용합니다.

### 3. 비선형 변환
비선형 변환은 데이터를 복잡한 비선형 함수로 변환하여 특정 패턴이나 특성을 강조하거나 분석하는 데 사용됩니다. 머신러닝에서 활성화 함수(예: 시그모이드 함수)는 입력 데이터를 비선형 변환하는 중요한 예입니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
