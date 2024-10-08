# 국소 대 전역 최적화

최적화 문제는 주어진 함수의 값을 최소화하거나 최대화하는 해를 찾는 과정입니다. 이러한 최적화 문제에서 해를 찾는 방식에는 국소 최적화(Local Optimization)와 전역 최적화(Global Optimization)라는 두 가지 주요 접근법이 있습니다. 이 두 접근법은 최적화 문제의 목표와 함수의 성질에 따라 선택됩니다.

## 1. 국소 최적화 (Local Optimization)

국소 최적화는 주어진 초기점 근처에서 함수의 국소 최소값 또는 최대값을 찾는 방법입니다. 즉, 함수의 도함수가 0이 되는 점을 찾아 그 점이 최소값인지 최대값인지를 분석합니다. 국소 최적화는 주로 미분 가능한 함수에 대해 작동하며, 다음과 같은 특징을 가집니다.

### 1.1 국소 최적화의 특징

- **빠른 수렴:** 국소 최적화 알고리즘은 일반적으로 빠르게 수렴합니다. 초기점에서 출발해 함수의 기울기를 따라 내려가면 비교적 빠르게 국소 최적해를 찾을 수 있습니다.
- **국소 해:** 국소 최적화는 국소적으로 최적화된 해를 찾습니다. 이는 반드시 전역 최적해일 필요는 없으며, 함수의 특정 구간에서만 최적임을 보장합니다.
- **알고리즘 예시:** 경사하강법(Gradient Descent), 뉴턴법(Newton's Method) 등이 대표적인 국소 최적화 알고리즘입니다.

### 1.2 국소 최적화의 한계

- **국소 해의 함정:** 국소 최적화는 전역 최적해를 보장하지 않습니다. 복잡한 함수의 경우 여러 개의 국소 최적점이 존재할 수 있으며, 이 중 일부는 전역 최적해가 아닐 수 있습니다.
- **초기값 의존성:** 결과는 초기값에 매우 민감할 수 있습니다. 잘못된 초기값을 선택하면 전역 최적해와 거리가 먼 국소 최적해에 수렴할 수 있습니다.

## 2. 전역 최적화 (Global Optimization)

전역 최적화는 함수의 전체 범위에서 최소값 또는 최대값을 찾는 방법입니다. 이 접근법은 국소 최적화와 달리 전역적인 관점에서 함수의 최적해를 찾기 위해 다양한 탐색 전략을 사용합니다.

### 2.1 전역 최적화의 특징

- **전역 해 보장:** 전역 최적화는 함수의 전체 정의역에서 최적의 값을 찾습니다. 따라서 찾은 해는 전역 최적해(global optimum)입니다.
- **복잡한 탐색:** 전역 최적화를 위해서는 다양한 초기값과 탐색 기법을 사용해야 하며, 이 과정에서 탐색이 복잡해질 수 있습니다.
- **알고리즘 예시:** 유전 알고리즘(Genetic Algorithm), 시뮬레이티드 어닐링(Simulated Annealing), 입자 군집 최적화(Particle Swarm Optimization) 등이 전역 최적화에 사용됩니다.

### 2.2 전역 최적화의 한계

- **계산 비용:** 전역 최적화 알고리즘은 국소 최적화 알고리즘에 비해 계산 비용이 높을 수 있습니다. 함수의 전체 정의역을 탐색해야 하기 때문에 더 많은 계산 자원이 필요합니다.
- **수렴 속도:** 전역 최적화는 국소 최적화에 비해 수렴 속도가 느릴 수 있습니다. 특히, 복잡한 함수의 경우 전역 최적해를 찾기 위한 탐색 과정이 길어질 수 있습니다.

## 3. 국소 최적화와 전역 최적화의 비교

국소 최적화와 전역 최적화는 각기 다른 목적과 특성을 가지며, 문제의 성격에 따라 적절한 방법을 선택해야 합니다.

| 특징                 | 국소 최적화             | 전역 최적화            |
|--------------------|----------------------|----------------------|
| 목적                 | 국소 해 찾기           | 전역 해 찾기           |
| 수렴 속도            | 빠름                    | 느림                    |
| 초기값 의존성         | 높음                    | 낮음                    |
| 계산 비용            | 낮음                    | 높음                    |
| 대표 알고리즘        | 경사하강법, 뉴턴법      | 유전 알고리즘, 시뮬레이티드 어닐링 |

## 4. 국소 최적화와 전역 최적화의 결합

실제 문제에서는 국소 최적화와 전역 최적화를 결합하여 사용하기도 합니다. 예를 들어, 전역 최적화 알고리즘을 사용하여 전체 공간을 탐색한 후, 국소 최적화 알고리즘을 적용하여 전역 최적해 주변에서 더 정확한 해를 찾는 방법이 있습니다. 이러한 접근법은 전역 최적화의 장점과 국소 최적화의 효율성을 결합하여 보다 신뢰할 수 있는 최적해를 찾는 데 유용합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
