# 행렬-벡터 곱

행렬-벡터 곱(matrix-vector multiplication)은 선형대수에서 매우 중요한 연산으로, 행렬과 벡터의 곱을 통해 선형 변환을 표현할 수 있습니다. 이 연산은 기하학적 변환, 시스템의 상태 변화, 머신러닝 모델의 계산 등 다양한 분야에서 활용됩니다.

## 1. 행렬-벡터 곱의 정의

행렬 $\mathbf{A}$가 크기 $m \times n$이고, 벡터 $\mathbf{x}$가 크기 $n \times 1$인 경우, 행렬 $\mathbf{A}$와 벡터 $\mathbf{x}$의 곱 $\mathbf{y}$는 크기 $m \times 1$인 벡터가 됩니다. 수식으로 표현하면 다음과 같습니다:

$$
\mathbf{y} = \mathbf{A} \mathbf{x}
$$

여기서, $\mathbf{y}$의 각 원소 $y_i$는 행렬 $\mathbf{A}$의 $i$번째 행과 벡터 $\mathbf{x}$의 내적으로 계산됩니다:

$$
y_i = \sum_{j=1}^{n} A_{ij} x_j
$$

이 연산은 행렬 $\mathbf{A}$의 각 행이 벡터 $\mathbf{x}$에 대해 얼마나 기여하는지를 나타내며, 결과적으로 벡터 $\mathbf{y}$는 $\mathbf{x}$의 선형 변환된 결과입니다.

## 2. 기하학적 해석

행렬-벡터 곱은 벡터 공간에서의 선형 변환을 나타냅니다. 예를 들어, 2차원 공간에서 회전 행렬 $\mathbf{R}$과 벡터 $\mathbf{x}$의 곱은 벡터 $\mathbf{x}$를 회전시키는 결과를 가져옵니다:

$$
\mathbf{R} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
$$

$$
\mathbf{y} = \mathbf{R} \mathbf{x}
$$

이와 같이 행렬-벡터 곱은 벡터를 특정 방식으로 변환하는 도구로 사용되며, 이를 통해 벡터의 크기 변화, 방향 회전, 반사, 확대/축소 등을 표현할 수 있습니다.

## 3. 응용 분야

- **기하학적 변환:** 컴퓨터 그래픽스에서 객체의 이동, 회전, 크기 조정 등을 행렬-벡터 곱으로 표현할 수 있습니다.
- **시스템 이론:** 동적 시스템의 상태 변화는 행렬-벡터 곱으로 모델링되며, 상태 공간 표현에서 시스템의 진화를 나타냅니다.
- **머신러닝:** 선형 회귀, 신경망의 가중치 계산 등에서 행렬-벡터 곱이 핵심 역할을 합니다. 예를 들어, 신경망의 각 층에서 입력 벡터와 가중치 행렬의 곱으로 다음 층의 활성화 값이 계산됩니다.

## 4. 행렬-벡터 곱의 특성

- **선형성:** 행렬-벡터 곱은 선형 변환으로, 두 벡터의 합에 대한 행렬의 곱은 각각의 행렬-벡터 곱의 합과 동일합니다:
  
  $$
  \mathbf{A}(\mathbf{x} + \mathbf{y}) = \mathbf{A}\mathbf{x} + \mathbf{A}\mathbf{y}
  $$

- **연관성:** 행렬-벡터 곱은 행렬의 곱과도 연관됩니다. 두 행렬 $\mathbf{A}$와 $\mathbf{B}$의 곱이 벡터 $\mathbf{x}$에 곱해질 때, 다음과 같이 계산됩니다:
  
  $$
  (\mathbf{A}\mathbf{B})\mathbf{x} = \mathbf{A}(\mathbf{B}\mathbf{x})
  $$

이러한 특성들은 행렬-벡터 곱이 복잡한 선형 변환을 단순화하는 데 유용함을 나타냅니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
