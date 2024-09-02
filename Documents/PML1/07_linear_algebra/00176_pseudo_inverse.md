# 유사 역행렬 (Pseudo-Inverse)

## 개요
유사 역행렬(pseudo-inverse) 또는 무어-펜로즈 역행렬(Moore-Penrose inverse)은 주어진 행렬에 대해 존재할 수 있는 '일반화된 역행렬'입니다. 일반적인 역행렬은 정방 행렬(square matrix)에서만 정의되며, 모든 정방 행렬이 역행렬을 가지는 것은 아닙니다. 하지만 유사 역행렬은 비정방 행렬(non-square matrix)을 포함한 모든 행렬에 대해 정의되며, 행렬 방정식의 최소제곱해를 구하는 데 주로 사용됩니다.

## 정의
행렬 $A$에 대한 유사 역행렬 $A^+$는 다음 네 가지 조건을 만족하는 유일한 행렬입니다:

$$
AA^+A = A
$$
$$
A^+AA^+ = A^+
$$
$$
(AA^+)^T = AA^+
$$
$$
(A^+A)^T = A^+A
$$

이 네 가지 조건은 유사 역행렬이 원래 행렬의 역행렬과 비슷한 성질을 갖도록 보장합니다.

## 유사 역행렬의 계산

유사 역행렬 $A^+$는 다음과 같이 구할 수 있습니다:

1. 행렬 $A$가 가우스-조던 소거법(Gaussian elimination)을 통해 풀 수 있는 경우, 이를 통해 직접 계산할 수 있습니다.
2. $A$가 정방 행렬이고, $A^T A$가 가역적인 경우:
   $$
   A^+ = (A^T A)^{-1} A^T
   $$
3. $A$가 정방 행렬이고, $AA^T$가 가역적인 경우:
   $$
   A^+ = A^T (AA^T)^{-1}
   $$

4. 일반적으로, 특이값 분해(SVD)를 통해 유사 역행렬을 계산할 수 있습니다. 행렬 $A$를 다음과 같이 특이값 분해합니다:
   $$
   A = U \Sigma V^T
   $$
   여기서 $U$와 $V$는 직교 행렬이고, $\Sigma$는 대각 행렬입니다. 이때, $A^+$는 다음과 같이 구할 수 있습니다:
   $$
   A^+ = V \Sigma^+ U^T
   $$
   여기서 $\Sigma^+$는 $\Sigma$의 역행렬 대신 모든 비영 값의 역수로 이루어진 대각 행렬입니다.

## 주요 응용
유사 역행렬은 선형 회귀, 신호 처리, 기계 학습 등 여러 분야에서 널리 사용됩니다. 특히, 과적합(overfitting)을 방지하기 위해 유사 역행렬을 사용하여 해를 안정적으로 구할 수 있습니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
