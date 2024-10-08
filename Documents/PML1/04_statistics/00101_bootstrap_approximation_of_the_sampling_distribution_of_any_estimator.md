# 임의 추정량의 표본 분포의 부트스트랩 근사

## 개요
부트스트랩(bootstrap) 방법은 통계적 추정에서 표본 분포를 근사하기 위한 강력한 방법입니다. 특히 임의의 추정량에 대해 부트스트랩을 활용하면, 실제 분포를 알 수 없거나 계산이 어려운 경우에도 표본 분포를 근사할 수 있습니다. 이 방법은 데이터로부터 반복적으로 재표집(resampling)하여 추정량의 분포를 추정하는 기법입니다.

## 부트스트랩 방법의 기본 아이디어
부트스트랩은 주어진 표본 데이터 $X = \{x_1, x_2, \ldots, x_n\}$에서 크기가 $n$인 새로운 표본을 반복적으로 추출하여, 그 표본에서 추정량을 계산하는 과정을 통해 이루어집니다. 이 과정에서 얻어진 추정량들의 분포가 원래 추정량의 표본 분포를 근사하게 됩니다.

1. 원본 데이터 $X$에서 크기가 $n$인 부트스트랩 표본 $X^*$을 무작위로 반복하여 생성합니다.
2. 각 부트스트랩 표본 $X^*$에 대해 관심 있는 추정량 $\hat{\theta}^*$를 계산합니다.
3. 이러한 $\hat{\theta}^*$를 충분히 많이 반복하여 얻은 분포가 원래 추정량 $\hat{\theta}$의 표본 분포에 대한 부트스트랩 근사입니다.

## 부트스트랩 분포의 수식 표현
추정량 $\hat{\theta}$의 부트스트랩 표본 분포는 다음과 같이 정의할 수 있습니다:

$$
\hat{\theta}^* = \hat{\theta}(X^*)
$$

여기서 $X^*$는 원본 데이터 $X$에서 부트스트랩에 의해 생성된 표본입니다. 이러한 $\hat{\theta}^*$의 분포는 추정량 $\hat{\theta}$의 원래 표본 분포를 근사합니다.

$$
\hat{F}_{\hat{\theta}}(t) = \frac{1}{B} \sum_{b=1}^{B} I(\hat{\theta}^*_b \leq t)
$$

여기서 $B$는 부트스트랩 표본의 수, $I$는 지시 함수입니다. 이로 인해 얻어진 누적 분포 함수 $\hat{F}_{\hat{\theta}}(t)$는 추정량 $\hat{\theta}$의 분포를 근사합니다.

## 부트스트랩의 장점과 한계
### 장점:
- **모수적 가정의 필요 없음**: 부트스트랩은 원본 데이터에서 직접 표본을 재추출하기 때문에, 특정 분포에 대한 가정을 하지 않아도 됩니다.
- **복잡한 추정량에 대한 적용 가능**: 평균과 같은 간단한 통계량 뿐만 아니라 복잡한 비선형 추정량에 대해서도 적용이 가능합니다.

### 한계:
- **컴퓨팅 비용**: 부트스트랩은 다수의 재표집과 추정을 필요로 하기 때문에, 계산 비용이 많이 들 수 있습니다.
- **작은 표본에서의 신뢰성 문제**: 원본 데이터의 표본 크기가 매우 작을 경우, 부트스트랩 근사 결과가 부정확할 수 있습니다.

## 결론
부트스트랩 방법은 임의 추정량의 표본 분포를 근사하는 강력한 도구입니다. 이 방법은 통계적 추정에서 널리 사용되며, 특히 데이터의 분포에 대한 사전 지식이 없거나 복잡한 추정량에 대해서도 적용이 가능합니다. 그러나 컴퓨팅 비용과 작은 표본에서의 신뢰성 문제는 부트스트랩의 적용에 있어서 고려해야 할 요소입니다.
