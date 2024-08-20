# 이산 확률 변수 (Discrete Random Variable)

## 개요
이산 확률 변수는 확률론과 통계학에서 매우 중요한 개념으로, 이산적인 값들을 가지는 확률 변수를 의미합니다. 이산 확률 변수는 유한하거나 셀 수 있는 무한개의 값을 가질 수 있으며, 각 값에 특정 확률이 할당됩니다.

## 정의
이산 확률 변수는 **이산적인 값**을 가지며, 주로 자연수나 정수와 같이 명확하게 구분되는 값을 가집니다. 이 변수는 무작위 실험의 결과를 수치적으로 표현하며, 그 결과는 확률 질량 함수(PMF: Probability Mass Function)로 설명됩니다.

예를 들어, 주사위를 던졌을 때 나오는 눈의 수는 1에서 6까지의 정수 값 중 하나입니다. 이 경우 주사위의 눈의 수는 이산 확률 변수입니다.

## 특징
- **유한한 또는 무한한 값의 집합**: 이산 확률 변수는 유한한 값의 집합(예: 주사위 결과)이나 셀 수 있는 무한한 값의 집합(예: 특정 사건이 발생하는 횟수)을 가질 수 있습니다.
- **확률 질량 함수 (PMF)**: 이산 확률 변수의 각 값에 대해 그 값이 나타날 확률을 정의하는 함수입니다. PMF는 각 값에 확률을 할당하며, 이 확률들의 합은 항상 1이 됩니다.

## 예시
### 주사위 던지기
주사위를 한 번 던졌을 때 나올 수 있는 결과를 나타내는 이산 확률 변수 \(X\)를 생각해 봅시다. 이 경우 \(X\)는 1에서 6까지의 값 중 하나를 가질 수 있으며, 각 값에 대한 확률은 다음과 같이 나타낼 수 있습니다:
- \( P(X = 1) = \frac{1}{6} \)
- \( P(X = 2) = \frac{1}{6} \)
- \( P(X = 3) = \frac{1}{6} \)
- \( P(X = 4) = \frac{1}{6} \)
- \( P(X = 5) = \frac{1}{6} \)
- \( P(X = 6) = \frac{1}{6} \)

이 경우 \(X\)는 1부터 6까지의 값을 가질 수 있는 이산 확률 변수이며, 각 값이 나올 확률은 동일하게 \( \frac{1}{6} \)입니다.

### 동전 던지기
동전 던지기에서 앞면이 나오면 1, 뒷면이 나오면 0으로 정의한 확률 변수 \(Y\)를 생각해 봅시다. 이 경우 \(Y\)는 0과 1의 값을 가질 수 있으며, 각 값에 대한 확률은 다음과 같이 나타낼 수 있습니다:
- \( P(Y = 0) = 0.5 \)
- \( P(Y = 1) = 0.5 \)

## 확률 질량 함수 (PMF)
확률 질량 함수는 이산 확률 변수의 값에 해당하는 확률을 나타내는 함수입니다. 예를 들어, 주사위를 던지는 경우 PMF는 다음과 같이 정의될 수 있습니다:
- \( P(X = x) = \frac{1}{6} \) for \( x = 1, 2, 3, 4, 5, 6 \)

PMF의 주요 성질은 다음과 같습니다:
- 모든 값에 대한 확률은 0 이상입니다.
- 모든 가능한 값에 대한 확률의 합은 1입니다.

## 기대값과 분산
이산 확률 변수의 **기대값**(Expected Value)은 그 변수의 평균적인 결과를 의미하며, **분산**(Variance)은 결과가 얼마나 퍼져 있는지를 나타냅니다. 기대값은 다음과 같이 계산됩니다:

\[
E(X) = \sum_{x} x \cdot P(X = x)
\]

분산은 다음과 같이 계산됩니다:

\[
Var(X) = \sum_{x} (x - E(X))^2 \cdot P(X = x)
\]

## 결론
이산 확률 변수는 실생활의 다양한 상황에서 발생하는 사건의 확률을 분석하는 데 중요한 도구입니다. 이 개념을 이해함으로써 우리는 다양한 확률적 현상을 보다 명확하게 설명하고 예측할 수 있습니다.

## 참고문헌
- [StatTrek, Discrete Random Variables](https://stattrek.com/probability-distributions/discrete-distributions.aspx)
- [Khan Academy, Discrete and Continuous Random Variables](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-stats/v/discrete-and-continuous-random-variables)
- [Wikipedia, Discrete Random Variable](https://en.wikipedia.org/wiki/Random_variable#Discrete_random_variable)
