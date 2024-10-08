# 연속 확률 변수를 위한 미분 엔트로피 (Differential Entropy)

## 개요

미분 엔트로피(Differential Entropy)는 연속 확률 변수를 위한 엔트로피의 개념입니다. 이산 확률 변수의 엔트로피와 유사하지만, 연속 확률 변수가 취할 수 있는 값이 무한하기 때문에 엔트로피의 정의에 미분을 사용하여 연속성을 반영합니다. 미분 엔트로피는 연속 확률 분포의 불확실성을 측정하는 데 사용되며, 정보 이론과 통계학에서 중요한 개념입니다.

## 1. **미분 엔트로피의 정의**

연속 확률 변수를 위한 미분 엔트로피 $H(X)$는 다음과 같이 정의됩니다:

$$
H(X) = - \int_{-\infty}^{\infty} p(x) \log p(x) \, dx
$$

여기서 $p(x)$는 연속 확률 변수 $X$의 확률 밀도 함수(PDF)입니다. 이 수식은 확률 밀도 함수 $p(x)$에 대한 정보의 평균적 불확실성을 측정합니다.

## 2. **이산 엔트로피와의 차이점**

이산 확률 변수의 엔트로피와 연속 확률 변수의 미분 엔트로피는 개념적으로 유사하지만, 다음과 같은 차이점이 있습니다:

- **범위**: 이산 확률 변수는 유한한 값의 집합을 가지지만, 연속 확률 변수는 무한한 연속체에 걸쳐 값을 가집니다.
- **적분 사용**: 이산 엔트로피는 합으로 계산되지만, 미분 엔트로피는 적분으로 계산됩니다.
- **단위**: 이산 엔트로피는 비트(bit) 또는 내트(nat) 단위로 측정되지만, 미분 엔트로피는 이러한 단위를 가지지 않습니다. 이는 미분 엔트로피가 절대적인 양이 아니라 상대적인 양으로 해석되기 때문입니다.

## 3. **미분 엔트로피의 해석**

미분 엔트로피는 확률 분포의 불확실성을 나타내지만, 이산 엔트로피와 달리 음수일 수 있습니다. 이는 미분 엔트로피가 절대적인 측정값이 아니며, 대신 확률 분포의 상대적인 정보량을 측정하는 데 사용된다는 점에서 유의미합니다.

예를 들어, 가우시안(정규) 분포 $N(\mu, \sigma^2)$의 미분 엔트로피는 다음과 같이 계산됩니다:

$$
H(X) = \frac{1}{2} \log(2 \pi e \sigma^2)
$$

여기서 $\sigma^2$는 분포의 분산입니다. 이 식은 분포의 불확실성이 분산 $\sigma^2$에 의해 증가한다는 것을 보여줍니다.

## 4. **미분 엔트로피의 한계**

미분 엔트로피는 연속 확률 분포의 정보량을 측정하는 데 유용하지만, 다음과 같은 한계가 있습니다:

- **비교 어려움**: 서로 다른 연속 확률 분포의 미분 엔트로피를 직접 비교하는 것은 의미가 없을 수 있습니다. 이는 미분 엔트로피가 특정 기준 없이 정의될 수 있기 때문입니다.
- **불변성 부족**: 미분 엔트로피는 비선형 변환에 대해 불변하지 않으므로, 특정 변환 후의 엔트로피 값은 해석이 어려울 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
