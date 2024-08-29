# 거듭제곱법 (Power Method)

거듭제곱법(Power Method)은 주어진 행렬의 가장 큰 절댓값을 갖는 고윳값과 이에 대응하는 고유 벡터를 구하는 데 사용되는 반복 알고리즘입니다. 이 방법은 대규모 행렬의 고윳값 문제를 해결하는 데 유용하며, 행렬의 지배적인 고윳값에 대해 집중적으로 수렴하는 특성을 가지고 있습니다.

## 알고리즘 개요

거듭제곱법은 초기 벡터를 시작으로 행렬과 벡터의 곱을 반복하여 점차적으로 주어진 행렬의 최대 고윳값과 그 고윳값에 대응하는 고유 벡터를 찾아갑니다. 이 방법은 특히 대규모 스펙트럼을 갖는 행렬에 대해 효율적입니다.

### 절차

1. **초기화**:
   초기 벡터 $x_0$를 설정합니다. 이 벡터는 임의의 비영 벡터로 시작할 수 있지만, 행렬의 최대 고윳값에 수렴하기 위해서는 초기 벡터가 행렬의 주된 고유 벡터와 유사한 방향을 가지는 것이 바람직합니다.

2. **반복 과정**:
   다음의 반복 과정을 통해 고유 벡터와 고윳값을 구합니다:
   $$ x_{k+1} = \frac{Ax_k}{\|Ax_k\|} $$
   여기서 $A$는 주어진 행렬, $x_k$는 $k$번째 반복에서의 벡터, $\|\cdot\|$은 벡터의 노름을 의미합니다.

3. **수렴 판정**:
   $x_{k+1}$이 $x_k$에 대해 충분히 수렴하면, 반복을 중지하고 $x_{k+1}$이 주된 고유 벡터가 됩니다. 이때의 고윳값 $\lambda$는 다음과 같이 계산할 수 있습니다:
   $$ \lambda_k = \frac{x_k^T A x_k}{x_k^T x_k} $$

### 수렴 조건

거듭제곱법이 성공적으로 수렴하기 위해서는 다음과 같은 조건이 필요합니다:

- 행렬 $A$는 고윳값 $\lambda_1$이 존재하며, 이 고윳값은 다른 고윳값들보다 절댓값이 크다고 가정합니다: $|\lambda_1| > |\lambda_2| \geq |\lambda_3| \geq \cdots \geq |\lambda_n|$.
- 초기 벡터 $x_0$는 $\lambda_1$에 대응하는 고유 벡터와 수렴하는 방향 성분을 가져야 합니다.

### 응용 및 한계

거듭제곱법은 대규모 행렬에서 주된 고윳값과 고유 벡터를 찾는 데 매우 효율적이지만, 다음과 같은 한계점이 있습니다:

- 만약 행렬 $A$의 고윳값들이 서로 매우 근접해 있는 경우, 수렴 속도가 느려질 수 있습니다.
- 거듭제곱법은 최대 고윳값에만 집중하기 때문에, 다른 고윳값을 구하려면 다른 방법을 사용해야 합니다.

### 예제

예를 들어, 2x2 행렬 $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$에 대해 거듭제곱법을 적용하면, 초기 벡터를 $x_0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$로 설정한 후 다음과 같이 계산할 수 있습니다:

1. 첫 번째 반복:
   $$ x_1 = \frac{A x_0}{\|A x_0\|} = \frac{\begin{pmatrix} 3 \\ 3 \end{pmatrix}}{\sqrt{18}} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

2. 두 번째 반복:
   $$ x_2 = \frac{A x_1}{\|A x_1\|} = \frac{\begin{pmatrix} 3 \\ 3 \end{pmatrix}}{\sqrt{18}} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} $$

이와 같이 반복이 계속되며 벡터 $x$는 $\frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix}$에 수렴하게 되고, 이 벡터는 행렬 $A$의 최대 고윳값 $3$에 대응하는 고유 벡터입니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
