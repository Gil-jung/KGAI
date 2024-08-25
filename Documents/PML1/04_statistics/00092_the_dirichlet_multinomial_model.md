# 디리클레-다항 모델 (Dirichlet-Multinomial Model)

디리클레-다항 모델(Dirichlet-Multinomial Model)은 베이지안 확률론에서 다항 분포의 사전 분포로 디리클레 분포를 사용하는 모델입니다. 이 모델은 여러 범주 중에서 데이터를 관측할 때, 범주의 선택 확률이 불확실한 상황에서 유용합니다.

## 1. 디리클레 분포 (Dirichlet Distribution)

디리클레 분포는 다차원 일반화된 베타 분포로, 매개변수 $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \ldots, \alpha_K)$에 의해 정의됩니다. 디리클레 분포의 확률 밀도 함수는 다음과 같습니다:

$$
P(\boldsymbol{\theta} \mid \boldsymbol{\alpha}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{k=1}^K \theta_k^{\alpha_k - 1}
$$

여기서 $B(\boldsymbol{\alpha})$는 디리클레 정규화 상수로, 베타 함수의 다차원 확장입니다.

$$
B(\boldsymbol{\alpha}) = \frac{\prod_{k=1}^K \Gamma(\alpha_k)}{\Gamma\left(\sum_{k=1}^K \alpha_k\right)}
$$

디리클레 분포는 $\theta_k$가 각 범주 $k$에 속할 확률을 나타내는 확률 벡터 $\boldsymbol{\theta}$에 대한 분포입니다. $\boldsymbol{\alpha}$의 각 요소는 대응되는 범주에 대한 사전 정보로 해석됩니다.

## 2. 다항 분포 (Multinomial Distribution)

다항 분포는 이산 확률 분포로, 하나의 실험에서 $K$개의 가능한 결과 중 하나가 발생할 때 사용됩니다. 다항 분포의 확률 질량 함수는 다음과 같습니다:

$$
P(\boldsymbol{n} \mid \boldsymbol{\theta}, N) = \frac{N!}{n_1! n_2! \cdots n_K!} \prod_{k=1}^K \theta_k^{n_k}
$$

여기서 $N$은 총 실험 횟수, $n_k$는 범주 $k$가 관측된 횟수, $\theta_k$는 각 범주의 발생 확률을 나타냅니다.

## 3. 디리클레-다항 모델의 결합

디리클레-다항 모델은 사전 분포로 디리클레 분포를 사용하고, 관측된 데이터에 대해 다항 분포를 따르는 모델입니다. 주어진 사전 분포 $\boldsymbol{\theta} \sim \text{Dir}(\boldsymbol{\alpha})$와 관측 데이터 $\boldsymbol{n} \mid \boldsymbol{\theta} \sim \text{Mult}(\boldsymbol{\theta}, N)$에 대한 사후 분포는 다시 디리클레 분포가 됩니다.

### 사후 분포 (Posterior Distribution)

베이즈 정리에 따라, 사후 분포는 다음과 같이 계산됩니다:

$$
P(\boldsymbol{\theta} \mid \boldsymbol{n}, \boldsymbol{\alpha}) \propto P(\boldsymbol{n} \mid \boldsymbol{\theta}) P(\boldsymbol{\theta} \mid \boldsymbol{\alpha})
$$

이 결과로 얻어지는 사후 분포는 다시 디리클레 분포가 되며, 갱신된 모수 $\boldsymbol{\alpha'}$는 다음과 같이 계산됩니다:

$$
\alpha'_k = \alpha_k + n_k
$$

따라서, 사후 분포는 다음과 같습니다:

$$
P(\boldsymbol{\theta} \mid \boldsymbol{n}, \boldsymbol{\alpha}) = \text{Dir}(\boldsymbol{\theta} \mid \alpha_1 + n_1, \alpha_2 + n_2, \ldots, \alpha_K + n_K)
$$

이 모델을 통해, 관측 데이터가 추가될 때마다 사후 분포가 갱신되며, 범주 확률에 대한 불확실성이 점진적으로 감소합니다.

## 4. 디리클레-다항 모델의 응용

디리클레-다항 모델은 자연어 처리, 토픽 모델링, 문서 분류 등 다양한 분야에서 사용됩니다. 이 모델은 데이터가 제한된 상황에서도 다항 분포의 모수에 대한 사전 지식을 결합하여 더 강력한 예측을 가능하게 합니다.
