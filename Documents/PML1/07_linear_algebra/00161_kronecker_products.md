# 크로네커 곱 (Kronecker Product)

크로네커 곱(Kronecker Product)은 두 행렬 간의 연산으로, 주어진 두 행렬의 곱을 정의하는 특별한 형태의 행렬 연산입니다. 이 연산은 주로 텐서의 확장, 신호 처리, 및 고차원 데이터의 분석에서 사용됩니다.

## 1. 정의

두 행렬 $\mathbf{A}$와 $\mathbf{B}$가 각각 $m \times n$과 $p \times q$ 크기를 가진다고 할 때, 이들의 크로네커 곱 $\mathbf{A} \otimes \mathbf{B}$는 다음과 같이 정의됩니다:

$$
\mathbf{A} \otimes \mathbf{B} = \begin{bmatrix}
a_{11}\mathbf{B} & a_{12}\mathbf{B} & \dots & a_{1n}\mathbf{B} \\
a_{21}\mathbf{B} & a_{22}\mathbf{B} & \dots & a_{2n}\mathbf{B} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1}\mathbf{B} & a_{m2}\mathbf{B} & \dots & a_{mn}\mathbf{B}
\end{bmatrix}
$$

여기서 $a_{ij}$는 행렬 $\mathbf{A}$의 $(i,j)$ 위치의 요소이며, $\mathbf{B}$는 두 번째 행렬입니다. 결과 행렬의 크기는 $mp \times nq$가 됩니다.

## 2. 예제

두 행렬 $\mathbf{A}$와 $\mathbf{B}$가 다음과 같다고 가정합니다:

$$
\mathbf{A} = \begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}, \quad \mathbf{B} = \begin{bmatrix}
0 & 5 \\
6 & 7
\end{bmatrix}
$$

이때, $\mathbf{A} \otimes \mathbf{B}$는 다음과 같이 계산됩니다:

$$
\mathbf{A} \otimes \mathbf{B} = \begin{bmatrix}
1 \times \mathbf{B} & 2 \times \mathbf{B} \\
3 \times \mathbf{B} & 4 \times \mathbf{B}
\end{bmatrix} = \begin{bmatrix}
0 & 5 & 0 & 10 \\
6 & 7 & 12 & 14 \\
0 & 15 & 0 & 20 \\
18 & 21 & 24 & 28
\end{bmatrix}
$$

결과 행렬의 크기는 $4 \times 4$가 됩니다.

## 3. 성질

크로네커 곱은 다음과 같은 중요한 성질을 가지고 있습니다:

- **결합 법칙**: 크로네커 곱은 결합 법칙을 따릅니다. 즉, $(\mathbf{A} \otimes \mathbf{B}) \otimes \mathbf{C} = \mathbf{A} \otimes (\mathbf{B} \otimes \mathbf{C})$.
- **분배 법칙**: 크로네커 곱은 행렬 덧셈에 대해 분배 법칙을 만족합니다. 즉, $\mathbf{A} \otimes (\mathbf{B} + \mathbf{C}) = \mathbf{A} \otimes \mathbf{B} + \mathbf{A} \otimes \mathbf{C}$.
- **역행렬**: 만약 $\mathbf{A}$와 $\mathbf{B}$가 모두 정방행렬이고, 각각 역행렬 $\mathbf{A}^{-1}$와 $\mathbf{B}^{-1}$을 가질 경우, 크로네커 곱의 역행렬은 다음과 같이 주어집니다: $(\mathbf{A} \otimes \mathbf{B})^{-1} = \mathbf{A}^{-1} \otimes \mathbf{B}^{-1}$.
- **행렬식**: 두 정방행렬 $\mathbf{A}$와 $\mathbf{B}$에 대해, 크로네커 곱의 행렬식은 다음과 같이 주어집니다: $\text{det}(\mathbf{A} \otimes \mathbf{B}) = (\text{det}(\mathbf{A}))^p \times (\text{det}(\mathbf{B}))^m$, 여기서 $\mathbf{A}$는 $m \times m$ 행렬, $\mathbf{B}$는 $p \times p$ 행렬입니다.

## 4. 응용

크로네커 곱은 다양한 응용 분야에서 사용됩니다. 예를 들어, 텐서 네트워크, 신호 처리, 이미지 처리 및 시스템 식별 분야에서 중요한 역할을 합니다. 특히, 고차원 시스템의 표현 및 분석에서 매우 유용합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
