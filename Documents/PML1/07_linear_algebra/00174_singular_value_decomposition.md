# 특잇값 분해(SVD)

특잇값 분해(Singular Value Decomposition, SVD)는 임의의 실수 또는 복소수 행렬을 세 개의 특수 행렬의 곱으로 표현하는 강력한 행렬 분해 기법입니다. SVD는 데이터 분석, 신호 처리, 머신러닝 등 다양한 분야에서 널리 사용됩니다.

## 1. SVD의 정의

특잇값 분해는 다음과 같이 정의됩니다:

$$
\mathbf{A} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T
$$

여기서:
- $\mathbf{A}$: $m \times n$ 크기의 임의의 행렬
- $\mathbf{U}$: $m \times m$ 크기의 직교 행렬로, $\mathbf{A} \mathbf{A}^T$의 고유벡터들로 구성됨
- $\mathbf{\Sigma}$: $m \times n$ 크기의 대각 행렬로, $\mathbf{A}$의 특잇값들(즉, $\mathbf{A} \mathbf{A}^T$ 또는 $\mathbf{A}^T \mathbf{A}$의 고유값들의 제곱근)로 구성됨
- $\mathbf{V}^T$: $n \times n$ 크기의 직교 행렬로, $\mathbf{A}^T \mathbf{A}$의 고유벡터들로 구성됨

## 2. SVD의 주요 성질

- **특잇값**: $\mathbf{\Sigma}$ 행렬의 대각 원소는 $\mathbf{A}$의 특잇값이며, 이러한 특잇값은 항상 비음수(non-negative)입니다.
- **차원 축소**: SVD는 고차원 데이터에서 가장 중요한 정보만을 추출하여 데이터의 차원을 줄일 수 있습니다. 이는 주성분 분석(PCA)과 밀접한 관련이 있습니다.
- **노이즈 제거**: SVD를 사용하면 데이터에서 노이즈를 제거하고, 신호 대 잡음비를 향상시킬 수 있습니다.
- **가장 낮은 계수 근사**: 주어진 행렬 $\mathbf{A}$를 SVD를 통해 근사할 때, 가장 낮은 계수(rank)의 근사 행렬을 찾는 데 유용합니다.

## 3. SVD의 응용

- **차원 축소**: 고차원 데이터의 차원을 효과적으로 줄이기 위해 SVD가 자주 사용됩니다. 예를 들어, 이미지 처리에서 차원을 줄여 압축하거나, 텍스트 데이터에서 LSA(Latent Semantic Analysis)와 같은 방법에 활용됩니다.
- **추천 시스템**: 사용자-아이템 행렬에서 SVD를 사용하여 잠재 요인 모델을 구축하고, 이를 기반으로 추천을 수행할 수 있습니다.
- **신호 처리**: 잡음이 섞인 신호를 SVD로 분해하여 신호와 잡음을 분리하는 데 활용됩니다.

SVD는 선형 대수학의 핵심 개념 중 하나로, 다양한 실세계 문제를 해결하는 데 매우 중요한 도구로 사용되고 있습니다. 이러한 특성 때문에 SVD는 데이터 과학, 통계, 머신러닝에서 매우 중요한 역할을 하고 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
