## 전진 KL 대 후진 KL

KL 발산(Kullback-Leibler Divergence)은 두 확률 분포 간의 차이를 측정하는 비대칭적인 지표입니다. 이 비대칭성으로 인해 전진 KL 발산(Forward KL Divergence)과 후진 KL 발산(Reverse KL Divergence)이라는 두 가지 주요 변형이 존재합니다.

### 전진 KL 발산 (Forward KL Divergence)

전진 KL 발산은 주어진 실제 분포 $P(x)$와 모델 분포 $Q(x)$ 간의 차이를 측정합니다. 이 발산은 다음과 같이 정의됩니다:

$$
D_{KL}(P || Q) = \sum_{x} P(x) \log \frac{P(x)}{Q(x)}
$$

여기서 $P(x)$는 참 확률 분포, $Q(x)$는 모델 분포입니다. 전진 KL 발산은 $Q(x)$가 $P(x)$와 얼마나 다른지를 평가하며, 주로 데이터가 주어진 상황에서 모델을 평가할 때 사용됩니다. 이 방법은 모델이 데이터의 모든 부분을 잘 설명하도록 유도하기 때문에 아웃라이어에 민감할 수 있습니다.

### 후진 KL 발산 (Reverse KL Divergence)

후진 KL 발산은 $Q(x)$와 $P(x)$의 차이를 측정하는 방식으로 정의됩니다:

$$
D_{KL}(Q || P) = \sum_{x} Q(x) \log \frac{Q(x)}{P(x)}
$$

후진 KL 발산은 주로 모델 $Q(x)$를 고정하고, 주어진 데이터 분포 $P(x)$를 맞추는 상황에서 사용됩니다. 이 경우, 모델은 자신이 잘 설명할 수 있는 부분에 집중하게 되며, 데이터의 일부를 무시할 수 있습니다. 따라서, 후진 KL 발산은 모드 콜랩스(mode collapse) 문제를 일으킬 수 있습니다.

### 차이점과 활용

전진 KL 발산은 모델이 데이터 분포를 포괄적으로 커버하도록 유도하므로 데이터의 모든 측면을 잘 설명하도록 하지만, 이로 인해 아웃라이어에 민감해질 수 있습니다. 반면, 후진 KL 발산은 모델이 자신이 잘 설명할 수 있는 부분에만 집중하도록 유도하므로, 데이터의 일부 모드를 놓칠 수 있습니다.

이러한 차이로 인해, 전진 KL 발산은 주로 밀도 추정(density estimation)과 같은 상황에서 사용되며, 후진 KL 발산은 변분 추론(variational inference)과 같은 상황에서 자주 사용됩니다.

### 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
