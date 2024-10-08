# 확률 (Probability)

## 1. 확률의 정의
확률은 어떤 사건이 발생할 가능성을 수치화한 것입니다. 일반적으로 0과 1 사이의 값으로 표현되며, 0은 사건이 발생하지 않을 확률이 전혀 없음을, 1은 사건이 확실히 발생할 것임을 의미합니다. 예를 들어, 동전을 던졌을 때 앞면이 나올 확률은 0.5입니다.

## 2. 확률의 기본 개념
확률은 여러 상황에서 다양하게 정의될 수 있지만, 기본적으로 다음과 같은 방식으로 계산됩니다:

- **단일 사건의 확률**: 단일 사건 A가 발생할 확률 P(A)는 사건 A가 발생하는 경우의 수를 전체 가능한 경우의 수로 나눈 값입니다.
  $$
  P(A) = \frac{\text{A가 발생하는 경우의 수}}{\text{전체 가능한 경우의 수}}
  $$

- **복합 사건의 확률**:
  - **독립 사건**: 두 사건이 서로 영향을 미치지 않는 경우, 두 사건 A와 B가 모두 발생할 확률은 각 사건의 확률을 곱한 값입니다.
    $$
    P(A \text{ and } B) = P(A) \times P(B)
    $$
  - **종속 사건**: 한 사건이 다른 사건에 영향을 미치는 경우, 조건부 확률을 사용하여 계산합니다. 사건 B가 발생했을 때 사건 A가 발생할 확률은 다음과 같이 계산됩니다.
    $$
    P(A|B) = \frac{P(A \cap B)}{P(B)}
    $$

## 3. 확률 분포 (Probability Distribution)
확률 분포는 주어진 확률 변수가 취할 수 있는 모든 값들과 그 값들이 발생할 확률을 나타내는 함수입니다. 확률 분포는 크게 **이산 확률 분포**와 **연속 확률 분포**로 나뉩니다.

- **이산 확률 분포**: 이산 확률 변수의 가능한 모든 결과에 대해 각각의 확률을 나타냅니다. 예를 들어, 주사위를 던질 때 나오는 각 숫자의 확률이 여기에 해당합니다.
  
- **연속 확률 분포**: 연속 확률 변수에 대해 정의되며, 특정 구간 내의 값들이 발생할 확률을 나타냅니다. 예를 들어, 사람의 키, 무게 등의 연속적인 데이터를 모델링할 때 사용됩니다.

## 4. 확률의 활용
확률은 다양한 분야에서 중요한 역할을 합니다. 특히 **기계 학습**에서 확률은 모델의 예측 성능을 평가하고, 미래의 사건이 발생할 가능성을 예측하는 데 사용됩니다. 예를 들어, Bayesian 기법은 사전 확률을 바탕으로 새로운 데이터에 따라 확률을 업데이트하는 방식으로 기계 학습에서 많이 활용됩니다.

## 5. 확률의 실제 예시
1. **독립 사건**: 동전 던지기와 주사위 굴리기의 결과는 독립적입니다. 동전이 앞면이 나올 확률은 0.5, 주사위에서 1이 나올 확률은 1/6입니다. 두 사건이 동시에 일어날 확률은 0.5 × 1/6 = 1/12입니다.
  
2. **조건부 확률**: 어떤 사람이 남자인 경우 그 사람이 키가 180cm 이상일 확률을 계산할 때, 남성 전체 인구 중에서 키가 180cm 이상인 사람의 비율을 사용하여 계산할 수 있습니다.

## 6. 확률의 중요성
확률 이론은 통계, 데이터 분석, 금융, 보험, 도박 등 여러 분야에서 핵심적인 역할을 합니다. 불확실한 상황에서 의사결정을 내리는 데 있어 확률적 접근은 매우 중요하며, 이는 예측, 리스크 관리, 최적화 등에서 필수적으로 사용됩니다.

