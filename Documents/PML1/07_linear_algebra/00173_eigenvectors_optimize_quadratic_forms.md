# 고유벡터는 이차 형식을 최적화한다

## 개요

이차 형식(Quadratic Form)은 벡터와 행렬을 사용해 정의되며, 다음과 같은 형태로 나타납니다:

$$
Q(\mathbf{x}) = \mathbf{x}^\top \mathbf{A} \mathbf{x}
$$

여기서 $\mathbf{x}$는 벡터, $\mathbf{A}$는 대칭 행렬입니다. 고유벡터와 고유값의 개념은 이차 형식을 최적화하는 데 중요한 역할을 합니다. 특히, 고유벡터는 이차 형식이 최대 또는 최소값을 가질 때의 방향을 나타냅니다.

## 고유값 분해와 이차 형식

행렬 $\mathbf{A}$가 대칭 행렬일 경우, 고유값 분해(Eigenvalue Decomposition, EVD)를 통해 다음과 같이 표현될 수 있습니다:

$$
\mathbf{A} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^\top
$$

여기서 $\mathbf{Q}$는 $\mathbf{A}$의 고유벡터들로 이루어진 직교 행렬, $\mathbf{\Lambda}$는 $\mathbf{A}$의 고유값들로 이루어진 대각 행렬입니다.

## 이차 형식의 최적화

이차 형식 $Q(\mathbf{x}) = \mathbf{x}^\top \mathbf{A} \mathbf{x}$를 최대화 또는 최소화하는 문제를 생각해봅시다. 벡터 $\mathbf{x}$는 단위 벡터($\|\mathbf{x}\| = 1$)로 가정합니다.

### 최대화 문제

이차 형식 $Q(\mathbf{x})$를 최대화하기 위해, $\mathbf{x}$를 고유벡터 $\mathbf{q}_1$로 설정하면 됩니다. 여기서 $\mathbf{q}_1$은 $\mathbf{A}$의 최대 고유값 $\lambda_1$에 대응하는 고유벡터입니다. 이 경우, 이차 형식의 값은 최대 고유값 $\lambda_1$이 됩니다:

$$
\max_{\mathbf{x}^\top \mathbf{x} = 1} Q(\mathbf{x}) = \lambda_1
$$

### 최소화 문제

반대로, 이차 형식을 최소화하려면 $\mathbf{x}$를 최소 고유값 $\lambda_n$에 대응하는 고유벡터 $\mathbf{q}_n$로 설정합니다. 이때, 이차 형식의 값은 최소 고유값 $\lambda_n$이 됩니다:

$$
\min_{\mathbf{x}^\top \mathbf{x} = 1} Q(\mathbf{x}) = \lambda_n
$$

## 고유벡터의 역할

고유벡터는 이차 형식을 최적화할 때 중요한 역할을 합니다. 이차 형식을 최대화하는 경우, 벡터 $\mathbf{x}$는 행렬 $\mathbf{A}$의 최대 고유값에 대응하는 고유벡터의 방향으로 설정됩니다. 마찬가지로, 최소화를 원할 경우에는 최소 고유값에 대응하는 고유벡터의 방향으로 설정됩니다.

## 결론

고유벡터는 이차 형식의 최적화 문제에서 중요한 도구로 작용하며, 고유값에 의해 이차 형식의 극값이 결정됩니다. 이 개념은 선형 대수학에서 뿐만 아니라, 머신 러닝과 통계학의 여러 응용에서도 널리 사용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
