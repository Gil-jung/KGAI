# 감마 분포 (Gamma Distribution)

## 개요
감마 분포는 연속 확률 분포 중 하나로, 양의 실수 영역에서 정의되며, 대기 시간 모델링과 같은 다양한 응용 분야에서 널리 사용됩니다. 감마 분포는 두 개의 모수인 형태 모수(shape parameter) $ k $와 척도 모수(scale parameter) $ \theta $에 의해 정의됩니다. 이 분포는 지수 분포(Exponential distribution)의 일반화로 간주되며, 포아송 과정에서 사건 간의 대기 시간을 모델링하는 데 사용됩니다.

## 수학적 정의
감마 분포의 확률 밀도 함수(PDF)는 다음과 같이 정의됩니다:

$$
f(x|k, \theta) = \frac{x^{k-1} e^{-x/\theta}}{\theta^k \Gamma(k)}, \quad x > 0
$$

여기서:
- $ k > 0 $는 형태 모수(shape parameter) 또는 "차수"라고도 불립니다.
- $ \theta > 0 $는 척도 모수(scale parameter)입니다.
- $ \Gamma(k) $는 감마 함수로, $ \Gamma(k) = \int_0^\infty t^{k-1} e^{-t} dt $로 정의됩니다.

## 감마 분포의 특성
- **평균**: 감마 분포의 평균은 $ k\theta $입니다.
- **분산**: 감마 분포의 분산은 $ k\theta^2 $입니다.
- **지수 분포와의 관계**: $ k = 1 $일 때, 감마 분포는 지수 분포와 동일합니다. 이 경우, 감마 분포는 단일 사건까지의 대기 시간을 모델링하는 데 사용됩니다.
- **합의 성질**: 두 개의 독립적인 감마 분포가 동일한 척도 모수를 가질 때, 이들의 합은 또 다른 감마 분포를 따릅니다. 이는 감마 분포가 여러 대기 시간의 합을 모델링하는 데 유용함을 의미합니다.

## 감마 분포의 응용
- **대기 시간 모델링**: 감마 분포는 특정 사건이 발생하기까지의 대기 시간이나 수명을 모델링하는 데 사용됩니다. 예를 들어, 전자 부품의 수명 분석이나 통신 시스템에서의 대기 시간 분석에 사용됩니다.
- **베이지안 통계**: 감마 분포는 베이지안 추론에서 포아송 분포의 사전 분포로 자주 사용됩니다.
- **신뢰 구간**: 감마 분포는 신뢰 구간을 설정하는 데 활용되며, 특히 비율이나 대기 시간과 관련된 문제에 적용됩니다.

## 감마 분포의 시각화
감마 분포는 형태 모수 $ k $와 척도 모수 $ \theta $의 값에 따라 다양한 형태를 취합니다. $ k $의 값이 커질수록 분포의 대칭성이 높아지며, $ \theta $의 값이 커질수록 분포가 더 넓게 퍼집니다.

## 참고 문헌
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
