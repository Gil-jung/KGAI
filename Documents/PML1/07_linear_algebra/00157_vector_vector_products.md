# 벡터-벡터 곱

벡터-벡터 곱은 선형대수에서 벡터 간의 곱셈을 의미하며, 주로 내적(dot product)과 외적(cross product) 두 가지 형태로 나뉩니다. 이들은 벡터를 다루는 다양한 문제에서 중요한 역할을 합니다.

## 1. 내적 (Dot Product)

두 벡터의 내적은 두 벡터가 이루는 각도와 벡터의 크기에 기반한 곱셈 연산입니다. $n$차원 벡터 $\mathbf{a} = [a_1, a_2, \dots, a_n]$와 $\mathbf{b} = [b_1, b_2, \dots, b_n]$의 내적은 다음과 같이 정의됩니다:

$$
\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i
$$

내적의 결과는 스칼라 값이며, 기하학적으로 두 벡터 사이의 각도를 측정하는 데 사용됩니다.

### 내적의 특성
- $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$ (교환 법칙)
- $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$ (분배 법칙)
- $\mathbf{a} \cdot \mathbf{a} = \|\mathbf{a}\|^2$ (자기 내적은 벡터 크기의 제곱)

내적은 물리학에서 일의 계산, 신호처리에서 두 신호의 유사도 측정 등 다양한 응용에 사용됩니다.

## 2. 외적 (Cross Product)

외적은 주로 3차원 벡터에서 정의되며, 두 벡터 $\mathbf{a}$와 $\mathbf{b}$의 외적은 새로운 벡터 $\mathbf{c}$를 생성합니다. 이 새로운 벡터 $\mathbf{c}$는 $\mathbf{a}$와 $\mathbf{b}$ 모두에 수직인 벡터입니다.

벡터 $\mathbf{a} = [a_1, a_2, a_3]$와 $\mathbf{b} = [b_1, b_2, b_3]$의 외적은 다음과 같이 계산됩니다:

$$
\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = \left( a_2b_3 - a_3b_2 \right)\mathbf{i} - \left( a_1b_3 - a_3b_1 \right)\mathbf{j} + \left( a_1b_2 - a_2b_1 \right)\mathbf{k}
$$

외적의 결과는 벡터이며, 기하학적으로 두 벡터가 이루는 평행사변형의 면적과 관련이 있습니다.

### 외적의 특성
- $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$ (반교환 법칙)
- $\mathbf{a} \times \mathbf{b} = \mathbf{0}$ (두 벡터가 평행하면 외적은 0이 됩니다.)
- 외적은 3차원 공간에서만 정의됩니다.

외적은 주로 물리학에서 모멘트나 회전과 같은 벡터량을 계산하는 데 사용됩니다.

## 3. 응용

벡터-벡터 곱은 기하학적 해석뿐만 아니라, 다양한 과학 및 공학 분야에서 중요한 도구입니다. 내적은 벡터 간의 정렬 정도나 유사도를 측정하는 데 사용되며, 외적은 회전과 같은 물리적 현상을 모델링하는 데 유용합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
