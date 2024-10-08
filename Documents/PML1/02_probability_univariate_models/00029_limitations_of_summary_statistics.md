# 요약 통계량의 한계

## 1. 개요
요약 통계량은 데이터의 전반적인 특성을 간단히 나타내기 위해 자주 사용됩니다. 대표적인 요약 통계량으로는 평균, 중앙값, 표준편차 등이 있으며, 이는 데이터의 분포, 중심경향, 변동성을 설명하는 데 사용됩니다. 하지만 요약 통계량은 데이터의 복잡한 특성을 모두 포착하지 못하며, 이에 따라 특정 상황에서는 한계를 가질 수 있습니다.

## 2. 주요 요약 통계량
- **평균(Mean)**: 데이터의 중심 경향을 나타내는 대표적인 값입니다. 하지만 평균은 극단값에 민감하여, 이상치(outlier)가 있는 경우 데이터의 진정한 중심을 왜곡할 수 있습니다.
  
- **중앙값(Median)**: 데이터의 중앙값으로, 이상치에 덜 민감합니다. 하지만 데이터의 분포를 충분히 설명하지 못할 수 있습니다.

- **표준편차(Standard Deviation)**: 데이터의 변동성을 나타내는 값으로, 평균과 마찬가지로 이상치에 민감합니다.

## 3. 요약 통계량의 한계

### 3.1 데이터 분포의 왜곡
요약 통계량은 데이터를 압축해서 표현하기 때문에, 데이터의 전체적인 분포를 왜곡할 수 있습니다. 예를 들어, 평균만을 고려할 경우 데이터가 어느 방향으로 치우쳐 있는지 알 수 없고, 비대칭 분포(왜도)가 존재할 경우에도 요약 통계량만으로 이를 파악하기 어렵습니다.

### 3.2 극단값에 대한 민감성
평균과 표준편차와 같은 요약 통계량은 이상치에 매우 민감합니다. 하나의 극단적인 데이터 포인트가 전체 데이터의 요약 통계량을 크게 변동시킬 수 있으며, 이는 데이터의 진정한 특성을 왜곡할 수 있습니다.

### 3.3 데이터 구조의 간과
요약 통계량은 데이터의 전체 구조와 패턴을 놓치기 쉽습니다. 예를 들어, 두 개의 데이터 집합이 같은 평균과 표준편차를 가질 수 있지만, 그 분포 형태는 완전히 다를 수 있습니다. 이러한 경우, 요약 통계량은 데이터의 복잡한 구조를 충분히 설명하지 못합니다.

### 3.4 정보 손실
데이터를 단순화하는 과정에서 많은 정보가 손실됩니다. 요약 통계량은 데이터의 중요한 세부 정보를 잃게 만듭니다. 이로 인해 특정 상황에서 결정을 내릴 때 충분한 근거를 제공하지 못할 수 있습니다.

## 4. 보완 방법
- **시각화**: 데이터의 분포를 더 잘 이해하기 위해 히스토그램, 박스플롯, 분산도 등을 활용해 데이터의 전체적인 패턴을 시각화할 수 있습니다.
- **다양한 통계량 사용**: 평균뿐만 아니라 중앙값, 최빈값, 사분위수 등 다양한 요약 통계량을 함께 고려하여 데이터의 전반적인 특성을 파악해야 합니다.
- **이상치 처리**: 이상치를 탐지하고 적절히 처리함으로써 요약 통계량의 신뢰성을 높일 수 있습니다.

## 5. 결론
요약 통계량은 데이터 분석에서 유용한 도구이지만, 그 한계를 인식하고 적절한 보완 방법을 사용하는 것이 중요합니다. 이를 통해 데이터의 복잡성을 충분히 이해하고 보다 정확한 결정을 내릴 수 있습니다.
