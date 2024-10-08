# 심슨의 역설

**심슨의 역설**(Simpson's Paradox)은 통계학에서 발생하는 역설로, 전체 데이터를 분석할 때 나타나는 경향이 하위 그룹을 따로 분석할 때는 반대 방향으로 나타나는 현상을 의미합니다. 이 역설은 데이터를 해석할 때, 특히 인과 관계를 추론할 때 매우 중요한 경고를 제공합니다.

## 심슨의 역설의 개요

심슨의 역설은 두 변수 간의 관계가 하위 그룹에서는 일정한 방향으로 나타나지만, 이 하위 그룹들을 합쳐서 분석할 때는 그 관계가 반대 방향으로 나타나는 현상을 말합니다. 이 역설은 데이터의 집합적 특성과 하위 그룹 간의 관계를 신중하게 고려하지 않으면 잘못된 결론을 도출할 수 있음을 보여줍니다.

### 예시: 대학 입학률

예를 들어, A 대학과 B 대학의 입학률을 비교할 때, 전체 데이터를 보면 A 대학이 B 대학보다 입학률이 더 높게 나타날 수 있습니다. 그러나 이 데이터를 남성과 여성으로 나누어 보면, 남성이나 여성 모두에서 B 대학의 입학률이 A 대학보다 높을 수 있습니다. 이런 경우 심슨의 역설이 발생한 것입니다.

### 수학적 설명

심슨의 역설은 다음과 같이 수학적으로 표현될 수 있습니다:

- $P(A|B) > P(A|\neg B)$ 이고, $P(A|C) > P(A|\neg C)$ 인 경우에도, 결합 확률 분포 $P(A|B \land C)$ 와 $P(A|\neg B \land \neg C)$ 에서는 역전이 발생할 수 있습니다.

이것은 곧 전체 데이터의 결합 분석과 하위 그룹별 분석에서 상반된 결과가 나올 수 있음을 의미합니다.

## 심슨의 역설의 원인

심슨의 역설이 발생하는 주된 이유는 **잠재적 공변량**(confounding variable) 또는 **제3의 변수**의 존재 때문입니다. 이러한 변수가 데이터를 집계하는 과정에서 그룹 간의 불균형을 야기할 수 있으며, 이는 전체 데이터와 하위 그룹 간의 결과 차이를 초래합니다.

## 심슨의 역설이 주는 교훈

1. **데이터의 집계 방법에 주의**: 심슨의 역설은 데이터를 해석할 때 하위 그룹의 특성을 고려하지 않으면 잘못된 결론에 이를 수 있음을 경고합니다.
  
2. **인과 관계의 신중한 추론**: 상관 관계나 단순 비교를 통해 인과 관계를 추론할 때, 이러한 역설이 발생할 가능성을 염두에 두어야 합니다.

3. **데이터 분할 분석의 중요성**: 심슨의 역설을 피하기 위해서는 전체 데이터를 분석하기 전에 하위 그룹별로 나누어 분석하는 것이 중요합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
