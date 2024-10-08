# 베르누이 분포와 이항 분포

## 1. 개요
**베르누이 분포(Bernoulli Distribution)**와 **이항 분포(Binomial Distribution)**는 모두 이산 확률 분포로, 성공/실패와 같은 두 가지 가능한 결과를 가지는 사건을 모델링하는 데 사용됩니다. 이 두 분포는 서로 밀접하게 연관되어 있으며, 베르누이 분포는 이항 분포의 특수한 경우입니다.

## 2. 베르누이 분포
### 정의
베르누이 분포는 성공 확률 $ p $와 실패 확률 $ 1-p $를 가지는 단일 시도의 결과를 모델링하는 확률 분포입니다. 베르누이 실험은 성공과 실패, 참과 거짓과 같이 두 가지 결과만을 가지는 실험을 말합니다.

### 확률 질량 함수 (PMF)
베르누이 분포의 확률 질량 함수는 다음과 같이 정의됩니다:
$$
P(X = x) = 
\begin{cases} 
p & \text{if } x = 1 \\
1 - p & \text{if } x = 0
\end{cases}
$$
여기서 $ X $는 베르누이 확률 변수이고, $ x $는 0(실패) 또는 1(성공)입니다.

### 기대값과 분산
- **기대값(평균)**: $ E(X) = p $
- **분산**: $ \text{Var}(X) = p(1-p) $

베르누이 분포는 단일 시도에 대한 확률 분포이므로, $ p = 0.5 $일 때는 완전히 무작위적인 결과를 나타냅니다.

## 3. 이항 분포
### 정의
이항 분포는 베르누이 실험을 $ n $번 반복한 결과를 모델링합니다. 이때 각 실험은 독립적이며 성공 확률 $ p $는 동일합니다. 이항 분포는 $ n $번의 시도 중 성공 횟수에 대한 확률 분포를 나타냅니다.

### 확률 질량 함수 (PMF)
이항 분포의 확률 질량 함수는 다음과 같이 정의됩니다:
$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$
여기서:
- $ \binom{n}{k} $는 이항 계수로, $ n $번 중 $ k $번 성공할 확률을 계산합니다.
- $ k $는 성공 횟수입니다.

### 기대값과 분산
- **기대값(평균)**: $ E(X) = np $
- **분산**: $ \text{Var}(X) = np(1-p) $

이항 분포는 베르누이 분포의 일반화된 형태로, 여러 번의 독립적인 베르누이 실험을 통해 성공 횟수를 계산하는데 사용됩니다.

## 4. 예제
### 베르누이 분포 예제
코인을 던져 앞면(성공)이 나올 확률이 0.5인 경우, 이 코인을 한 번 던지는 사건은 베르누이 분포를 따릅니다. 성공 확률 $ p $는 0.5입니다.

### 이항 분포 예제
동일한 코인을 10번 던졌을 때 앞면이 나올 횟수는 이항 분포를 따릅니다. 이 경우 $ n = 10 $, $ p = 0.5 $이며, 앞면이 5번 나올 확률을 구할 수 있습니다.

## 5. 베르누이 분포와 이항 분포의 관계
베르누이 분포는 단일 시도에 대한 확률 분포로, 이항 분포의 특수한 경우입니다. 이항 분포는 여러 번의 베르누이 시도를 종합한 결과로, $ n $이 1인 경우 이항 분포는 베르누이 분포와 동일해집니다.

## 6. 결론
베르누이 분포와 이항 분포는 이산 확률 분포 중 기본적이고 중요한 개념으로, 성공과 실패로 나뉘는 사건을 모델링하는 데 자주 사용됩니다. 이 분포들은 현실 세계의 다양한 상황을 수학적으로 표현하고 분석하는 데 유용한 도구를 제공합니다.
