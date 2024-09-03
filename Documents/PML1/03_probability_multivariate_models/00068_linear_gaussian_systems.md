# 선형 가우스 체계 (Linear Gaussian Systems)

**선형 가우스 체계(Linear Gaussian Systems)**는 선형 회귀 및 확률적 모델링에서 중요한 역할을 하는 통계 모델로, 관측된 데이터와 숨겨진 변수 간의 관계가 선형적이며, 데이터의 조건부 분포가 가우시안(정규) 분포를 따르는 시스템을 의미합니다. 이 체계는 많은 기계 학습 알고리즘에서 기본 구성 요소로 사용되며, 특히 베이즈 추론과 같은 확률적 접근 방식에서 자주 등장합니다.

## 1. 선형 가우스 모델의 정의

선형 가우스 모델은 주어진 입력 변수 $\mathbf{X}$와 출력 변수 $\mathbf{Y}$ 간의 관계를 다음과 같이 정의합니다:

$$
\mathbf{Y} = \mathbf{W}^T \mathbf{X} + \mathbf{\epsilon}
$$

여기서:

- $\mathbf{X}$: 입력 벡터
- $\mathbf{W}$: 가중치 벡터
- $\mathbf{\epsilon}$: 가우시안 잡음(정규 분포를 따르는 잡음)으로, $\mathbf{\epsilon} \sim \mathcal{N}(0, \sigma^2)$

이 모델에서 $\mathbf{Y}$는 $\mathbf{X}$에 선형적으로 의존하며, 가우시안 잡음 $\mathbf{\epsilon}$이 추가되어 실제 관측된 출력 $\mathbf{Y}$를 형성합니다.

## 2. 선형 가우스 모델의 특징

### 2.1 선형성

선형 가우스 모델의 주요 가정은 출력 $\mathbf{Y}$가 입력 $\mathbf{X}$에 대해 선형적인 관계를 가진다는 것입니다. 이 관계는 $\mathbf{W}$라는 가중치 벡터에 의해 조정됩니다. 즉, 각 입력 변수에 대해 일정한 가중치를 적용하여 출력 변수를 예측합니다.

### 2.2 가우스 잡음

가우스 잡음 $\mathbf{\epsilon}$은 모델의 불확실성을 표현합니다. 이는 관측된 데이터가 입력 변수만으로 완벽히 설명되지 않고, 일부 랜덤한 잡음이 존재함을 나타냅니다. 이 잡음은 평균이 0이고, 분산이 $\sigma^2$인 정규 분포를 따릅니다.

### 2.3 조건부 분포

선형 가우스 모델에서, 출력 $\mathbf{Y}$의 조건부 분포는 가우시안 분포가 됩니다:

$$
\mathbf{Y} \mid \mathbf{X} \sim \mathcal{N}(\mathbf{W}^T \mathbf{X}, \sigma^2)
$$

즉, 주어진 입력 $\mathbf{X}$에 대해 출력 $\mathbf{Y}$는 평균이 $\mathbf{W}^T \mathbf{X}$이고, 분산이 $\sigma^2$인 정규 분포를 따릅니다.

## 3. 선형 가우스 체계의 응용

### 3.1 선형 회귀

선형 회귀 분석은 선형 가우스 모델의 대표적인 응용 사례입니다. 주어진 데이터 포인트들의 관계를 설명하는 직선(또는 평면)을 찾는 것이 목표이며, 이는 주어진 데이터에서 최적의 가중치 벡터 $\mathbf{W}$를 찾는 과정으로 설명됩니다.

### 3.2 베이지안 선형 회귀

베이지안 선형 회귀에서는 가중치 벡터 $\mathbf{W}$에 대해 사전 분포(prior distribution)를 설정하고, 관측된 데이터에 따라 사후 분포(posterior distribution)를 계산합니다. 이 접근법은 모델의 불확실성을 더 명확하게 표현할 수 있게 해줍니다.

### 3.3 칼만 필터

칼만 필터는 선형 가우스 모델을 기반으로 한 알고리즘으로, 시간에 따라 변하는 시스템의 상태를 추정하는 데 사용됩니다. 특히 제어 시스템, 로봇 공학, 금융 등에서 상태 추정 및 예측을 위해 널리 사용됩니다.

## 4. 선형 가우스 모델의 매개변수 추정

선형 가우스 모델의 매개변수, 즉 가중치 벡터 $\mathbf{W}$와 잡음의 분산 $\sigma^2$는 주어진 데이터로부터 최대우도추정법(Maximum Likelihood Estimation, MLE)을 통해 추정할 수 있습니다.

### 4.1 가중치 벡터 $\mathbf{W}$의 최대우도추정

최대우도추정법을 사용하여 $\mathbf{W}$를 추정하는 과정은 다음과 같이 전개됩니다:

$$
\hat{\mathbf{W}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}
$$

여기서 $\mathbf{X}$는 입력 데이터의 행렬, $\mathbf{Y}$는 출력 데이터의 벡터를 나타냅니다. 이 식은 선형 회귀 분석에서 사용하는 일반적인 형태입니다.

### 4.2 잡음 분산 $\sigma^2$의 최대우도추정

잡음 분산 $\sigma^2$는 다음과 같이 추정됩니다:

$$
\hat{\sigma}^2 = \frac{1}{N} \sum_{i=1}^{N} (y_i - \mathbf{W}^T \mathbf{x}_i)^2
$$

여기서 $N$은 데이터 포인트의 개수를 나타냅니다.

## 5. 결론

선형 가우스 체계는 입력 변수와 출력 변수 간의 관계를 선형적으로 모델링하며, 데이터의 조건부 분포가 가우시안 분포를 따르는 중요한 통계 모델입니다. 이는 선형 회귀, 베이지안 추론, 칼만 필터 등 다양한 기계 학습 및 데이터 분석 기법에서 핵심적인 역할을 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
