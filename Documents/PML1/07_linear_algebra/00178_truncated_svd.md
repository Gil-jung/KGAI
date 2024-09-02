# 절단된 SVD (Truncated Singular Value Decomposition)

**절단된 SVD**는 고차원 행렬의 차원을 줄이는 데 자주 사용되는 기법입니다. 기본적으로 SVD(Singular Value Decomposition)는 임의의 행렬 $A$를 세 개의 행렬 $U$, $\Sigma$, $V^T$의 곱으로 분해하는 방법입니다. 이를 수식으로 표현하면 다음과 같습니다.

$$
A = U \Sigma V^T
$$

여기서,
- $A$는 $m \times n$ 차원의 원본 행렬,
- $U$는 $m \times m$ 차원의 직교 행렬,
- $\Sigma$는 $m \times n$ 차원의 대각 행렬,
- $V^T$는 $n \times n$ 차원의 직교 행렬입니다.

대각 행렬 $\Sigma$는 특이값(singular values)이라고 불리는 값들이 대각선에 배치되어 있으며, 이 특이값들은 원본 행렬 $A$의 중요한 정보들을 담고 있습니다.

## 절단된 SVD의 정의

절단된 SVD는 이러한 SVD 분해에서 가장 중요한 몇 개의 특이값과 이에 대응하는 벡터들만을 남겨두고 나머지를 버리는 방법입니다. 이를 통해 차원 축소가 가능하며, 노이즈가 포함된 데이터의 경우 중요한 정보만을 남길 수 있습니다.

예를 들어, $k$개의 주요 특이값과 대응하는 벡터들만을 남기고 나머지를 버리면, 절단된 SVD는 다음과 같이 표현됩니다.

$$
A_k = U_k \Sigma_k V_k^T
$$

여기서,
- $U_k$는 $m \times k$ 차원의 직교 행렬,
- $\Sigma_k$는 $k \times k$ 차원의 대각 행렬,
- $V_k^T$는 $k \times n$ 차원의 직교 행렬입니다.

즉, 원래의 SVD와 달리 절단된 SVD에서는 주요 성분 $k$만을 선택하여 원래 행렬 $A$를 근사하는 것입니다.

## 절단된 SVD의 응용

절단된 SVD는 데이터 압축, 잡음 제거, 추천 시스템, 이미지 처리 등 다양한 분야에서 사용됩니다. 특히, 행렬의 차원을 효과적으로 줄이면서도 중요한 정보를 유지할 수 있기 때문에, 고차원 데이터 분석에 매우 유용합니다.

### 1. 차원 축소
차원이 높은 데이터(예: 문서의 단어-문서 행렬)를 절단된 SVD로 축소하여 계산의 복잡도를 낮출 수 있습니다.

### 2. 노이즈 제거
원본 데이터에서 노이즈가 포함된 부분은 일반적으로 작은 특이값에 대응하므로, 이를 제거하고 중요한 정보만을 유지할 수 있습니다.

### 3. 추천 시스템
사용자-아이템 행렬에서 절단된 SVD를 적용하면, 사용자의 선호도를 기반으로 새로운 추천을 생성할 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
