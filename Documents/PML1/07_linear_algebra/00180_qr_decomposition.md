# QR 분해 (QR Decomposition)

**QR 분해**는 임의의 행렬을 두 개의 행렬, 즉 직교 행렬(Orthogonal matrix) $Q$와 상삼각 행렬(Upper triangular matrix) $R$로 분해하는 방법입니다. 이 방법은 선형대수학에서 중요한 역할을 하며, 특히 선형 방정식의 해를 구하거나 행렬의 고유값 문제를 해결하는 데 자주 사용됩니다. QR 분해는 SVD(Singular Value Decomposition)와 유사한 응용을 가지며, 계산 효율성을 높이는 데 유용합니다.

## QR 분해의 정의

QR 분해는 다음과 같이 표현됩니다. 주어진 $m \times n$ 행렬 $A$를 $Q$와 $R$로 분해하면:

$$
A = QR
$$

여기서,
- $Q$는 $m \times m$ 크기의 직교 행렬로, 열 벡터들이 서로 직교하며 크기가 1인 단위 벡터로 구성됩니다.
- $R$은 $m \times n$ 크기의 상삼각 행렬로, 대각선 위의 원소들은 0이 아니며, 그 아래의 원소들은 0입니다.

QR 분해는 모든 직사각형 행렬에 대해 적용 가능하며, $m \geq n$인 경우 $A$를 완전히 분해할 수 있습니다.

## QR 분해의 계산 방법

QR 분해를 계산하는 방법에는 여러 가지가 있으며, 대표적인 방법으로는 그램-슈미트(Gram-Schmidt) 정규화, 하우스홀더 변환(Householder transformation), 그리고 기븐스 회전(Givens rotation)이 있습니다.

### 1. 그램-슈미트 정규화 (Gram-Schmidt Process)
그램-슈미트 정규화는 행렬 $A$의 열 벡터들을 직교화하여 $Q$를 구한 뒤, $R$을 계산하는 방법입니다. 이 방법은 직관적이지만, 수치적으로 불안정할 수 있습니다.

### 2. 하우스홀더 변환 (Householder Transformation)
하우스홀더 변환은 대각 요소를 축으로 하여 반사하는 방법으로, 더 안정적이고 효율적인 QR 분해 방법입니다.

### 3. 기븐스 회전 (Givens Rotation)
기븐스 회전은 특정 행렬 요소를 0으로 만들기 위해 2차원 회전을 사용하는 방법입니다. 이 방법은 희소 행렬에서 효율적으로 사용됩니다.

## QR 분해의 응용

QR 분해는 다양한 응용 분야에서 중요한 역할을 합니다. 그 중 일부는 다음과 같습니다:

### 1. 선형 방정식 풀이
QR 분해는 연립방정식 $Ax = b$의 해를 구하는 데 사용됩니다. QR 분해를 이용하면 $Ax = b$를 $QRx = b$로 변환하고, $y = Rx$를 이용해 쉽게 풀이할 수 있습니다.

### 2. 최소자승법 (Least Squares)
QR 분해는 최소자승 문제를 푸는 데 사용됩니다. 데이터 점들에 가장 잘 맞는 직선을 찾는 문제에서 QR 분해를 이용하여 효율적으로 계산할 수 있습니다.

### 3. 고유값 문제
QR 분해는 행렬의 고유값을 계산하는 QR 알고리즘의 핵심 단계로, 대규모 행렬의 고유값을 계산하는 데 사용됩니다.

## QR 분해의 특성

QR 분해는 다음과 같은 특성을 가집니다:
- **유일성**: $A$가 정칙 행렬일 경우, QR 분해는 유일합니다. 즉, $Q$와 $R$은 고유하게 결정됩니다.
- **안정성**: 하우스홀더 변환과 기븐스 회전은 수치적으로 안정적이며, 큰 스케일의 문제에서도 신뢰할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
