# 다중 클래스 로지스틱 회귀 (Multinomial Logistic Regression)

## 개요
다중 클래스 로지스틱 회귀는 종속 변수가 3개 이상의 범주를 가질 때 사용되는 회귀 기법입니다. 이는 이항 로지스틱 회귀를 확장한 형태로, 각 클래스에 속할 확률을 계산하여 가장 높은 확률을 가진 클래스를 예측합니다. 다중 클래스 로지스틱 회귀는 다중 클래스 분류 문제에서 널리 사용됩니다.

## 모델 설명
다중 클래스 로지스틱 회귀에서는 주어진 입력 벡터 \( \mathbf{x} \)에 대해 각 클래스 \( k \)에 속할 확률 \( P(y = k | \mathbf{x}) \)를 다음과 같이 모델링합니다:

\[
P(y = k | \mathbf{x}) = \frac{e^{\mathbf{w}_k^T \mathbf{x} + b_k}}{\sum_{j=1}^{K} e^{\mathbf{w}_j^T \mathbf{x} + b_j}}
\]

여기서:
- \( \mathbf{w}_k \)는 클래스 \( k \)에 대한 가중치 벡터입니다.
- \( b_k \)는 클래스 \( k \)에 대한 바이어스(절편)입니다.
- \( K \)는 클래스의 총 개수입니다.

이 수식은 소프트맥스 함수와 밀접하게 관련되어 있으며, 각 클래스의 선형 결합을 지수 함수로 변환한 후, 그 합으로 나누어 각 클래스에 속할 확률을 계산합니다.

## 학습 과정
모델 파라미터 \( \mathbf{w}_k \)와 \( b_k \)는 최대 가능도 추정을 통해 학습됩니다. 즉, 주어진 학습 데이터에 대해 실제 클래스 \( y \)가 관찰될 확률을 최대화하는 방향으로 모델을 최적화합니다. 이 과정에서 크로스 엔트로피 손실 함수가 자주 사용됩니다.

## 특징 및 장점
- **확률적 예측**: 각 클래스에 대한 확률을 제공하여 불확실성을 정량화할 수 있습니다.
- **직관적 해석**: 각 클래스에 속할 확률이 계산되므로 결과를 해석하기 쉽습니다.
- **일반화 가능**: 적절한 정규화를 통해 과적합을 방지하고 모델의 일반화 성능을 향상시킬 수 있습니다.

## 활용 사례
- **문자 인식**: 이미지에서 문자나 숫자를 인식하는 문제에서 자주 사용됩니다.
- **문서 분류**: 문서가 여러 카테고리 중 하나에 속하는지 예측하는 데 활용됩니다.
- **의료 진단**: 환자의 데이터를 기반으로 여러 질병 중 하나를 진단하는 문제에서도 사용됩니다.

## 구현 예시
다음은 Python의 `scikit-learn` 라이브러리를 사용하여 다중 클래스 로지스틱 회귀를 구현하는 간단한 예시입니다:

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X = iris.data
y = iris.target

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 다중 클래스 로지스틱 회귀 모델 학습
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
model.fit(X_train, y_train)

# 예측 및 정확도 평가
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'모델 정확도: {accuracy * 100:.2f}%')
```

## 참고 문헌
- **Scikit-Learn Documentation**: 다중 클래스 로지스틱 회귀 구현에 대한 자세한 설명과 예제.
- **Machine Learning Books**: 머신러닝 이론과 로지스틱 회귀에 관한 상세한 설명을 제공하는 다양한 책들.