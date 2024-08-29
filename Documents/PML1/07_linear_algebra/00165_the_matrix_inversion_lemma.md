# 역행렬 보조정리 (Matrix Inversion Lemma)

**역행렬 보조정리**(Matrix Inversion Lemma)는 행렬 이론에서 매우 유용한 결과로, 주어진 행렬의 역행렬을 간단하게 계산하거나 업데이트할 수 있게 해줍니다. 이는 특히 선형 대수학, 확률론, 신호 처리, 통계학, 기계 학습 등 다양한 분야에서 중요한 역할을 합니다.

## 1. 역행렬 보조정리의 정의

역행렬 보조정리는 다음과 같은 형태의 행렬 $\mathbf{A}$의 역행렬을 효율적으로 계산하는 방법을 제공합니다. 

$$
\mathbf{A} = \mathbf{B} + \mathbf{U} \mathbf{C} \mathbf{V}^T
$$

여기서:
- $\mathbf{B}$는 $n \times n$ 행렬,
- $\mathbf{U}$와 $\mathbf{V}$는 각각 $n \times k$ 행렬,
- $\mathbf{C}$는 $k \times k$ 행렬입니다.

이때 $\mathbf{A}$의 역행렬은 다음과 같이 계산할 수 있습니다:

$$
\mathbf{A}^{-1} = \mathbf{B}^{-1} - \mathbf{B}^{-1} \mathbf{U} \left(\mathbf{C}^{-1} + \mathbf{V}^T \mathbf{B}^{-1} \mathbf{U}\right)^{-1} \mathbf{V}^T \mathbf{B}^{-1}
$$

이는 종종 **우드베리 행렬 항등식**(Woodbury matrix identity)이라고도 불리며, 효율적인 계산을 가능하게 합니다. 특히 $\mathbf{B}$의 역행렬이 이미 계산되어 있는 경우에 유용합니다.

## 2. 역행렬 보조정리의 응용

역행렬 보조정리는 다음과 같은 다양한 분야에서 응용될 수 있습니다:

### 2.1 칼만 필터 (Kalman Filter)
칼만 필터에서 상태 예측과 관측 업데이트 단계에서 역행렬 보조정리를 사용하여 계산 효율성을 높일 수 있습니다. 이는 특히 고차원 상태 공간에서 중요한 역할을 합니다.

### 2.2 가우시안 프로세스 (Gaussian Processes)
가우시안 프로세스에서 커널 행렬의 역행렬을 계산할 때, 새로운 데이터 포인트가 추가될 때마다 전체 역행렬을 다시 계산하지 않고, 효율적으로 업데이트할 수 있습니다.

### 2.3 최소자승문제 (Least Squares Problems)
역행렬 보조정리는 최소자승 문제에서 패러메터 업데이트를 효율적으로 수행하는 데에도 사용됩니다. 특히, 데이터가 점진적으로 들어올 때 사용되는 점진적 최소자승 알고리즘에서 유용합니다.

## 3. 수식의 유도

역행렬 보조정리의 유도는 행렬 분해와 블록 행렬의 역행렬 계산에 기초합니다. 다음은 기본적인 유도 과정입니다:

1. 우선, $\mathbf{A}$를 $\mathbf{B}$와 $\mathbf{U} \mathbf{C} \mathbf{V}^T$의 합으로 표현합니다.
2. $\mathbf{A}$의 역행렬을 구하기 위해 셔어 보수(Schur complement)와 블록 행렬의 역행렬 공식을 사용합니다.
3. 마지막으로, $\mathbf{B}^{-1}$과 다른 행렬 간의 관계를 이용하여 최종적인 역행렬을 얻습니다.

## 4. 중요한 성질

- **효율성**: 대규모 데이터나 고차원 문제에서 행렬의 역행렬을 효율적으로 계산할 수 있습니다.
- **적용 범위**: 다양한 통계적 기법과 알고리즘에서 핵심적으로 사용됩니다.
- **확장성**: 역행렬 보조정리는 다양한 형태의 행렬 계산에 적용될 수 있으며, 행렬 분해, 행렬 추정 및 최적화 문제 등에서도 활용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
