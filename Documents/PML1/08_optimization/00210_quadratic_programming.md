# 이차 프로그래밍 (Quadratic Programming)

**이차 프로그래밍**(Quadratic Programming, QP)은 최적화 문제의 한 형태로, 목적 함수가 이차 함수(quadratic function)로 표현되며, 제약 조건은 선형 제약 조건으로 주어지는 문제를 다룹니다. 이차 프로그래밍은 금융, 공학, 기계 학습 등 다양한 분야에서 자주 사용되며, 특히 서포트 벡터 머신(Support Vector Machine, SVM) 같은 문제에서 핵심적인 역할을 합니다.

## 1. 이차 프로그래밍의 정의

이차 프로그래밍 문제는 다음과 같은 형태로 정의됩니다:

$$
\text{최적화할 함수: } \min_x \; \frac{1}{2} x^T Q x + c^T x
$$

$$
\text{제약 조건: } A x \leq b
$$

$$
x \geq 0
$$

여기서,
- $x$는 변수 벡터,
- $Q$는 대칭 양의 준정부호(positive semi-definite)인 행렬,
- $c$는 선형 항의 계수 벡터,
- $A$는 제약 조건을 정의하는 행렬,
- $b$는 제약 조건의 상수 벡터입니다.

## 2. 이차 프로그래밍의 구성 요소

### 2.1. **목적 함수 (Objective Function)**

이차 프로그래밍의 목적 함수는 이차 항과 선형 항으로 구성됩니다. 이차 항은 다음과 같이 표현됩니다:

$$
\frac{1}{2} x^T Q x
$$

여기서 $Q$는 대칭 양의 준정부호 행렬로, 목적 함수의 곡률을 정의합니다. 선형 항은 다음과 같이 표현됩니다:

$$
c^T x = c_1 x_1 + c_2 x_2 + \cdots + c_n x_n
$$

### 2.2. **제약 조건 (Constraints)**

제약 조건은 변수들이 만족해야 하는 선형 부등식 또는 등식입니다. 제약 조건은 다음과 같은 형태로 표현됩니다:

$$
A x \leq b
$$

여기서 $A$는 제약 조건을 정의하는 행렬이고, $b$는 제약 조건의 상수 벡터입니다.

### 2.3. **비부정성 조건 (Non-negativity Constraints)**

이차 프로그래밍에서도 변수들이 음수 값을 가질 수 없도록 비부정성 조건을 추가합니다:

$$
x \geq 0
$$

## 3. 이차 프로그래밍의 해법

### 3.1. **KKT 조건 (Karush-Kuhn-Tucker Conditions)**

이차 프로그래밍 문제를 해결하는 주요 방법 중 하나는 **KKT 조건**을 활용하는 것입니다. KKT 조건은 최적해가 만족해야 하는 필요충분조건을 제공하며, 라그랑주 승수를 이용하여 문제를 해결합니다. 이는 특히 비선형 제약 조건을 포함하는 최적화 문제를 다룰 때 유용합니다.

### 3.2. **내부점법 (Interior Point Method)**

이차 프로그래밍에서 자주 사용되는 또 다른 방법은 **내부점법**입니다. 이 방법은 문제의 내부에서 최적해를 찾아가는 방식으로, 특히 대규모 문제를 해결할 때 계산 효율성이 높습니다.

### 3.3. **활성 집합법 (Active Set Method)**

활성 집합법은 이차 프로그래밍 문제에서 제약 조건의 일부를 활성화(active) 상태로 간주하고, 이를 기반으로 최적해를 찾는 방법입니다. 이 방법은 주로 작은 규모의 문제나 제약 조건이 상대적으로 적은 문제에서 사용됩니다.

## 4. 이차 프로그래밍의 응용

이차 프로그래밍은 다음과 같은 다양한 분야에서 응용됩니다:

- **서포트 벡터 머신 (Support Vector Machine, SVM)**: 이차 프로그래밍은 SVM에서 분류 경계를 최적화하는 데 사용됩니다.
- **포트폴리오 최적화**: 금융에서 자산 배분을 최적화하기 위해 사용됩니다. 이 경우 이차 프로그래밍은 위험(분산)과 수익(기대값)을 동시에 고려합니다.
- **제어 이론**: 제어 시스템에서 안정성을 보장하는 최적의 제어 신호를 찾기 위해 사용됩니다.
- **기계 학습**: 특정 학습 모델의 파라미터를 최적화하는 데 사용됩니다.

## 5. 이차 프로그래밍의 예제

다음은 이차 프로그래밍 문제의 간단한 예제입니다:

목표 함수: 

$$
\min_x \; \frac{1}{2} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}^T \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} -4 \\ -6 \end{bmatrix}^T \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

제약 조건:
$$
x_1 + x_2 \leq 1
$$

$$
x_1 \geq 0, \; x_2 \geq 0
$$

이 문제를 내부점법 또는 활성 집합법을 사용하여 해결할 수 있습니다.

## 6. 결론

이차 프로그래밍은 선형 프로그래밍에서 확장된 개념으로, 이차 함수의 최적화를 다룹니다. 목적 함수의 이차성 때문에 다양한 현실 세계의 문제를 보다 정확하게 모델링할 수 있으며, KKT 조건, 내부점법, 활성 집합법 등의 방법으로 효율적으로 해결할 수 있습니다. 이차 프로그래밍은 SVM, 포트폴리오 최적화, 제어 이론 등에서 중요한 역할을 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
