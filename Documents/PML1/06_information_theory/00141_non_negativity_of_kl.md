# KL의 비음성

## 개요

KL 발산(Kullback-Leibler Divergence)은 두 확률 분포 간의 차이를 측정하는 지표로, 정보 이론에서 중요한 역할을 합니다. KL 발산은 언제나 비음성(non-negativity)을 유지하며, 이 특성은 매우 중요한 이론적 의미를 가집니다. KL 발산의 비음성은 Jensen's inequality(옌센 부등식)에 의해 증명될 수 있으며, 이는 KL 발산이 두 분포가 동일할 때에만 0이 된다는 것을 보장합니다.

## 1. **KL 발산의 정의**

KL 발산은 두 확률 분포 $P$와 $Q$가 주어졌을 때, $P$가 $Q$로부터 얼마나 다른지를 다음과 같이 정의합니다:

$$
D_{KL}(P \parallel Q) = \int_{-\infty}^{\infty} p(x) \log \left(\frac{p(x)}{q(x)}\right) dx
$$

이 수식에서 $p(x)$는 참 분포 $P$의 확률 밀도 함수(PDF)이고, $q(x)$는 근사 분포 $Q$의 확률 밀도 함수입니다.

## 2. **비음성의 의미**

KL 발산의 비음성은 다음과 같은 중요한 의미를 가집니다:

- **불확실성의 차이**: KL 발산은 $Q$가 $P$를 얼마나 잘 설명하는지를 나타내며, 이 값이 0 이상이라는 것은 $Q$가 $P$를 완벽하게 설명하지 않는 한 항상 일정한 정보 손실이 있다는 것을 의미합니다.
- **동일 분포에서의 0**: KL 발산이 0이 되는 유일한 경우는 $P$와 $Q$가 완전히 동일한 분포일 때입니다. 이때, $P(x) = Q(x)$이므로 $\log(1) = 0$이 되어 전체 발산 값이 0이 됩니다.

## 3. **Jensen's Inequality를 통한 증명**

KL 발산의 비음성은 Jensen's Inequality에 의해 증명될 수 있습니다. Jensen's Inequality는 다음과 같이 표현됩니다:

$$
\mathbb{E}[\log(f(x))] \leq \log(\mathbb{E}[f(x)])
$$

여기서 $f(x) = \frac{p(x)}{q(x)}$로 설정하면, KL 발산의 비음성이 성립됩니다. 구체적으로,

$$
\int_{-\infty}^{\infty} p(x) \log \left(\frac{p(x)}{q(x)}\right) dx \geq 0
$$

이는 KL 발산이 항상 0 이상임을 보장하며, 이는 $P$와 $Q$가 동일할 때만 발산 값이 0이 된다는 것을 의미합니다.

## 4. **비음성의 실용적 중요성**

KL 발산의 비음성 특성은 실제 응용에서 다음과 같은 중요한 역할을 합니다:

- **모델 평가**: KL 발산이 0보다 크다는 것은 근사 분포 $Q$가 참 분포 $P$에 대해 어느 정도 정보 손실을 포함하고 있음을 의미하므로, 이를 통해 모델의 성능을 평가할 수 있습니다.
- **정보 손실 측정**: 비음성은 두 분포 간의 정보 손실을 양수로 보장함으로써, 정보 이론에서 신뢰할 수 있는 손실 측정을 가능하게 합니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
