# 행렬-행렬 곱

행렬-행렬 곱(matrix-matrix multiplication)은 선형대수에서 두 행렬 간의 곱을 계산하는 중요한 연산입니다. 이 연산은 수학적, 기하학적, 그리고 컴퓨터 과학적인 다양한 응용에서 핵심적인 역할을 합니다.

## 1. 행렬-행렬 곱의 정의

두 행렬 $\mathbf{A}$와 $\mathbf{B}$의 곱 $\mathbf{C}$는 $\mathbf{A}$의 열의 개수와 $\mathbf{B}$의 행의 개수가 동일할 때 정의됩니다. 즉, $\mathbf{A}$가 크기 $m \times n$이고, $\mathbf{B}$가 크기 $n \times p$라면, 곱 $\mathbf{C} = \mathbf{A}\mathbf{B}$는 크기 $m \times p$의 행렬입니다. 수식으로 표현하면 다음과 같습니다:

$$
\mathbf{C} = \mathbf{A} \mathbf{B}
$$

여기서, $\mathbf{C}$의 각 원소 $C_{ij}$는 $\mathbf{A}$의 $i$번째 행과 $\mathbf{B}$의 $j$번째 열의 내적으로 계산됩니다:

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

## 2. 기하학적 해석

행렬-행렬 곱은 선형 변환을 조합하는 역할을 합니다. 예를 들어, 행렬 $\mathbf{A}$와 $\mathbf{B}$가 각각 다른 선형 변환을 나타낸다면, 이 둘을 곱한 행렬 $\mathbf{C}$는 이 두 변환을 순차적으로 수행하는 결과를 나타냅니다.

특히, 행렬-행렬 곱을 통해 연속된 변환을 한 번에 표현할 수 있습니다. 이는 컴퓨터 그래픽스에서 물체의 변환, 물리 시스템에서 상태의 변화, 신경망에서 가중치 업데이트 등 다양한 분야에서 중요한 역할을 합니다.

## 3. 행렬-행렬 곱의 성질

- **비교환성:** 행렬 곱은 일반적으로 교환법칙을 따르지 않습니다. 즉, $\mathbf{A}\mathbf{B} \neq \mathbf{B}\mathbf{A}$인 경우가 대부분입니다.
  
- **결합성:** 행렬 곱은 결합법칙을 따릅니다. 즉, 세 행렬 $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$에 대해 다음이 성립합니다:

  $$
  (\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C})
  $$

- **분배성:** 행렬 곱은 덧셈에 대해 분배법칙을 따릅니다. 즉, 다음이 성립합니다:

  $$
  \mathbf{A}(\mathbf{B} + \mathbf{C}) = \mathbf{A}\mathbf{B} + \mathbf{A}\mathbf{C}
  $$

  $$
  (\mathbf{A} + \mathbf{B})\mathbf{C} = \mathbf{A}\mathbf{C} + \mathbf{B}\mathbf{C}
  $$

## 4. 응용 분야

- **컴퓨터 그래픽스:** 행렬-행렬 곱은 물체의 회전, 이동, 확대/축소 등 복합적인 변환을 표현하는 데 사용됩니다.
- **기계 학습:** 신경망에서 여러 층의 가중치 행렬들을 곱하여 입력을 변환하는 데 사용됩니다.
- **물리 시스템:** 상태 공간 모델에서 시스템의 동적 변화를 표현하는 데 사용됩니다.

## 5. 효율적인 계산

행렬-행렬 곱의 계산은 복잡도가 $O(m \times n \times p)$로, 큰 행렬의 경우 계산 비용이 매우 높을 수 있습니다. 따라서, 병렬 처리, 분산 컴퓨팅, 최적화 알고리즘 등이 실제 응용에서 중요한 역할을 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
