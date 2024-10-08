# 벡터와 행렬의 노름

**노름(Norm)**은 벡터 또는 행렬의 크기 또는 길이를 측정하는 방법으로, 수학과 공학에서 중요한 역할을 합니다. 노름은 벡터 공간에서 정의된 거리 개념을 일반화하며, 데이터 분석, 최적화 문제, 기계 학습 등의 여러 분야에서 널리 사용됩니다.

## 벡터의 노름

벡터의 노름은 벡터의 크기 또는 길이를 측정하는 함수입니다. 벡터 $x \in \mathbb{R}^n$에 대해, 노름은 다음 세 가지 조건을 만족하는 함수 $\| \cdot \| : \mathbb{R}^n \rightarrow \mathbb{R}$입니다:

1. **비음성 조건**: $\|x\| \geq 0$이며, $\|x\| = 0$인 경우 $x = 0$입니다.
2. **삼각 부등식**: $\|x + y\| \leq \|x\| + \|y\|$입니다.
3. **동질성**: 모든 실수 $\alpha$에 대해 $\|\alpha x\| = |\alpha| \cdot \|x\|$입니다.

### 1. $L^p$ 노름

가장 일반적인 벡터 노름은 $L^p$ 노름입니다. $p$가 1 이상인 실수일 때, $L^p$ 노름은 다음과 같이 정의됩니다:

$$
\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{\frac{1}{p}}
$$

특별히 자주 사용되는 $L^p$ 노름은 다음과 같습니다:

- **$L^1$ 노름**: 

$$
\|x\|_1 = \sum_{i=1}^n |x_i|
$$

  이는 벡터 요소들의 절대값의 합으로, 절대값 합 노름이라고도 불립니다.

- **$L^2$ 노름**: 

$$
\|x\|_2 = \left( \sum_{i=1}^n x_i^2 \right)^{\frac{1}{2}}
$$

  이는 유클리드 노름 또는 이차 노름이라고 하며, 벡터의 길이를 나타냅니다.

- **$L^\infty$ 노름**: 

$$
\|x\|_\infty = \max_i |x_i|
$$

  이는 벡터 요소 중 절대값이 가장 큰 값입니다.

### 2. 제곱 합 노름 (Frobenius 노름)

제곱 합 노름(Frobenius 노름)은 행렬의 크기를 측정하는 방법 중 하나입니다. 이는 행렬의 모든 요소의 제곱합에 대한 제곱근으로 정의됩니다. 행렬 $A \in \mathbb{R}^{m \times n}$에 대해, Frobenius 노름은 다음과 같습니다:

$$
\|A\|_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2}
$$

이는 $L^2$ 노름을 벡터에 적용한 결과와 유사하게, 행렬의 각 요소를 하나의 벡터 요소로 간주하여 계산된 노름입니다.

## 행렬의 노름

행렬 노름은 벡터 노름을 확장한 개념으로, 행렬의 크기를 측정합니다. 주어진 행렬 $A \in \mathbb{R}^{m \times n}$에 대해 행렬 노름은 다음 세 가지 조건을 만족해야 합니다:

1. **비음성 조건**: $\|A\| \geq 0$이며, $\|A\| = 0$인 경우 $A = 0$입니다.
2. **삼각 부등식**: $\|A + B\| \leq \|A\| + \|B\|$입니다.
3. **동질성**: 모든 실수 $\alpha$에 대해 $\|\alpha A\| = |\alpha| \cdot \|A\|$입니다.

### 1. $L^p$ 유도 노름

행렬의 $L^p$ 노름은 벡터의 $L^p$ 노름을 바탕으로 정의됩니다. 특히 자주 사용되는 행렬 노름은 $L^2$ 유도 노름(Spectral 노름)입니다. 이는 행렬 $A$에 대해 다음과 같이 정의됩니다:

$$
\|A\|_2 = \sigma_{\text{max}}(A)
$$

여기서 $\sigma_{\text{max}}(A)$는 행렬 $A$의 최대 특이값입니다.

### 2. 행렬 최대 노름

행렬 최대 노름(Matrix max norm)은 행렬의 각 요소 중 절대값이 가장 큰 값을 나타내며, 다음과 같이 정의됩니다:

$$
\|A\|_{\infty} = \max_{i,j} |a_{ij}|
$$

## 노름의 응용

벡터와 행렬의 노름은 다음과 같은 다양한 분야에서 중요하게 사용됩니다:

- **최적화 문제**: 목적 함수나 제약 조건으로 사용되는 경우가 많습니다.
- **데이터 분석**: 데이터의 크기나 분포를 측정하는 데 사용됩니다.
- **기계 학습**: 손실 함수 또는 규제 항으로 활용됩니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
