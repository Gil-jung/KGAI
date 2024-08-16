```graph TD
    A[프론트엔드 - React] -->|API 요청| B[백엔드 - FastAPI]
    B -->|데이터 저장/조회| C[Neo4j 그래프 DB]
    B -->|문서 저장/조회| D[파일 시스템 - Markdown 문서]
    B -->|전문 검색| E[Elasticsearch]
    A -->|그래프 시각화| F[Cytoscape.js]
    A -->|마크다운 렌더링| G[React-Markdown]
    H[AI 모델 - 그래프 확장] -->|새로운 노드/관계 추가| B
    I[사용자] -->|상호작용| A
```