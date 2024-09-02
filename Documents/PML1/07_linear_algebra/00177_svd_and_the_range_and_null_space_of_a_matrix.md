# 행렬의 SVD와 치역 및 영공간

행렬의 특이값 분해(Singular Value Decomposition, SVD)는 임의의 행렬을 세 개의 다른 행렬의 곱으로 분해하는 기법입니다. 이를 통해 행렬의 다양한 성질을 분석할 수 있습니다. 특히, 치역(image)과 영공간(null space)을 이해하는 데 매우 유용합니다.

## SVD 정의

임의의 $m \times n$ 행렬 $A$에 대해, SVD는 다음과 같이 표현됩니다:

$$
A = U \Sigma V^T
$$

여기서,
- $U$: $m \times m$ 직교 행렬 (행렬 $A$의 좌특이벡터들로 구성)
- $\Sigma$: $m \times n$ 직사각형 대각 행렬 (특이값이 대각 원소로 존재)
- $V$: $n \times n$ 직교 행렬 (행렬 $A$의 우특이벡터들로 구성)

이때, $\Sigma$의 대각 원소가 행렬 $A$의 특이값(singular value)입니다. 이 값들은 $A$의 선형 변환에 대한 크기 조절을 나타냅니다.

## 치역과 영공간

### 치역 (Image)

행렬 $A$의 치역은 $A$에 의해 매핑되는 모든 벡터의 집합입니다. SVD를 통해 $A$의 치역은 행렬 $U$의 열벡터 중 특이값이 0이 아닌 벡터들로 구성된 부분 공간입니다. 즉, 치역은 $U$에 의해 생성된 벡터 공간에서의 하위 공간입니다.

$$
\text{Im}(A) = \text{span}\{ \mathbf{u}_i : \sigma_i \neq 0 \}
$$

여기서 $\sigma_i$는 $\Sigma$의 대각 원소, 즉 특이값입니다.

### 영공간 (Null Space)

행렬 $A$의 영공간은 $A$에 의해 영벡터로 매핑되는 모든 벡터들의 집합입니다. SVD를 통해 $A$의 영공간은 행렬 $V$의 열벡터 중 특이값이 0인 벡터들로 구성된 부분 공간입니다.

$$
\text{Null}(A) = \text{span}\{ \mathbf{v}_i : \sigma_i = 0 \}
$$

여기서 $\mathbf{v}_i$는 $V$의 열벡터입니다.

## SVD를 통한 치역과 영공간의 해석

SVD를 이용하면, 행렬의 선형 변환이 어떻게 이루어지는지 시각적으로 이해할 수 있습니다. 
- $U$는 입력 공간의 벡터들을 회전시키고,
- $\Sigma$는 벡터의 크기를 조절하며,
- $V^T$는 변환된 벡터를 다시 회전시킵니다.

이 과정을 통해 어떤 벡터가 치역에 포함되고, 어떤 벡터가 영공간에 포함되는지 알 수 있습니다.

## 참고 문헌

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Murphy, K. P. (2022). *Probabilistic Machine Learning: An Introduction*. MIT Press.
- Murphy, K. P. (2023). *Probabilistic Machine Learning: Advanced Topics*. MIT Press.
