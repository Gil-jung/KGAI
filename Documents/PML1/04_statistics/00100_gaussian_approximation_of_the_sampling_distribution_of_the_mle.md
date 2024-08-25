# MLE의 표본 분포의 가우스 근사

## 개요
최대우도추정(MLE, Maximum Likelihood Estimation)은 주어진 데이터에 가장 잘 맞는 모수 값을 추정하는 방법입니다. MLE는 많은 통계적 학습에서 중요한 역할을 하며, MLE로 추정한 모수의 표본 분포는 가우스(정규) 분포로 근사될 수 있습니다. 이러한 근사는 특히 대규모 표본에 대해 유용합니다. 

## MLE의 표본 분포
MLE로 추정한 모수의 표본 분포는 많은 상황에서 가우스 분포로 근사될 수 있습니다. 이 근사는 중심극한정리(Central Limit Theorem)와 관련이 있으며, 표본 크기가 충분히 크다면 MLE의 표본 분포는 정규 분포에 가까워집니다.

MLE $\hat{\theta}$의 표본 분포는 다음과 같이 표현됩니다:

$$
\hat{\theta} \sim N(\theta, I(\theta)^{-1})
$$

여기서 $\theta$는 진짜 모수 값, $I(\theta)$는 피셔 정보 행렬(Fisher Information Matrix)입니다.

## 피셔 정보 행렬
피셔 정보 행렬은 모수 $\theta$에 대한 정보의 양을 측정하는 방법으로, 주어진 데이터가 특정 모수 값에 대해 얼마나 잘 설명되는지를 나타냅니다. 피셔 정보 행렬 $I(\theta)$는 다음과 같이 정의됩니다:

$$
I(\theta) = -E\left[\frac{\partial^2 \log L(\theta)}{\partial \theta^2}\right]
$$

여기서 $L(\theta)$는 우도 함수(likelihood function)입니다. 피셔 정보 행렬의 역행렬 $I(\theta)^{-1}$은 MLE의 분산을 나타내며, 이 값은 MLE 추정치가 가지는 불확실성을 표현합니다.

## 가우스 근사의 의미
가우스 근사란 MLE의 표본 분포가 정규 분포로 근사된다는 의미입니다. 이는 다음과 같은 성질을 가지는 정규 분포로 근사할 수 있음을 의미합니다:

$$
\hat{\theta} \sim N(\theta, \frac{1}{nI(\theta)})
$$

여기서 $n$은 표본 크기입니다. 표본 크기가 증가함에 따라 MLE의 분포는 더 정밀한 근사치를 제공하게 됩니다. 이는 MLE가 일치성과 효율성을 가지는 추정량임을 보여주는 중요한 결과입니다.

## 활용 및 한계
가우스 근사는 표본 크기가 충분히 큰 경우 유용하지만, 작은 표본에서는 이 근사가 부정확할 수 있습니다. 특히, 데이터가 왜곡되었거나 이상치가 많을 경우에는 주의가 필요합니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
