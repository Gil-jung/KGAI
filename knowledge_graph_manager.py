import requests
import json

class KnowledgeGraphManager:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def add_node(self, name, category, properties=None, markdown_content=""):
        url = f"{self.base_url}/nodes"
        data = {
            "name": name,
            "category": category,
            "properties": properties or {},
            "markdown_content": markdown_content
        }
        response = requests.post(url, json=data)
        return response.json() if response.status_code == 200 else None

    def update_node(self, node_id, name=None, category=None, properties=None, markdown_content=None):
        url = f"{self.base_url}/nodes/{node_id}"
        data = {}
        if name is not None:
            data["name"] = name
        if category is not None:
            data["category"] = category
        if properties is not None:
            data["properties"] = properties
        if markdown_content is not None:
            data["markdown_content"] = markdown_content
        response = requests.put(url, json=data)
        return response.json() if response.status_code == 200 else None

    def delete_node(self, node_id):
        url = f"{self.base_url}/nodes/{node_id}"
        response = requests.delete(url)
        return response.status_code == 200

    def add_edge(self, source_id, target_id, relationship_type):
        url = f"{self.base_url}/edges"
        data = {
            "source_id": source_id,
            "target_id": target_id,
            "relationship_type": relationship_type
        }
        response = requests.post(url, json=data)
        return response.json() if response.status_code == 200 else None

    def update_edge(self, edge_id, relationship_type):
        url = f"{self.base_url}/edges/{edge_id}"
        data = {"relationship_type": relationship_type}
        response = requests.put(url, json=data)
        return response.json() if response.status_code == 200 else None

    def delete_edge(self, edge_id):
        url = f"{self.base_url}/edges/{edge_id}"
        response = requests.delete(url)
        return response.status_code == 200

    def get_node(self, node_id):
        url = f"{self.base_url}/nodes/{node_id}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def search_nodes(self, query, category=None, limit=10):
        url = f"{self.base_url}/search"
        params = {"query": query, "limit": limit}
        if category:
            params["category"] = category
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()
            if not results:
                print(f"No results found for query: {query}")
            return results
        else:
            print(f"Error searching nodes: {response.status_code}")
            return None

    def get_node_edges(self, node_id):
        url = f"{self.base_url}/nodes/{node_id}/edges"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

def main():
    manager = KnowledgeGraphManager()
    new_node = True

    print(open("Documents/PML1/01_introduction/00019_the_relationship_between_ml_and_other_fields.md", "r", encoding="utf-8").read())

    # 노드삭제
    # nodes = [3, 4, 6, 7, 8, 9]
    # for node in nodes:
    #     manager.delete_node(node)
    #     print("노드 삭제:", node)

    # 노드에 연결된 엣지 삭제
    # edges = manager.get_node_edges(7)
    # print("엣지:", edges)
    # for edge in edges:
    #     manager.delete_edge(edge['id'])
    #     print("엣지 삭제:", edge['id'])

    # 머신러닝과 비지도학습 사이의 엣지 생성
    # source_id = manager.search_nodes("지도학습")[0]['id']
    # target_id = manager.search_nodes("회귀")[0]['id']
    # new_edge = manager.add_edge(source_id, target_id, "관련_작업")
    # print("새로운 엣지:", new_edge)



    if not new_node:
        # 노드 업데이트 예시
        updated_node = manager.update_node(
            new_node['id'],
            properties={"정의": "데이터로부터 학습하는 AI의 한 분야", "중요성": "높음"},
            markdown_content="# 머신러닝\n\n머신러닝은 인공지능의 한 분야로, 컴퓨터가 데이터로부터 학습하여 성능을 향상시키는 기술입니다.\n\n## 주요 알고리즘\n- 지도 학습\n- 비지도 학습\n- 강화 학습"
        )
        print("업데이트된 노드:", updated_node)

        # 엣지 추가 예시
        new_edge = manager.add_edge(1, new_node['id'], "관련_기술")
        print("새로운 엣지:", new_edge)

        # 노드 검색 예시
        search_results = manager.search_nodes("머신러닝")
        print("검색 결과:", search_results)

        # 노드 정보 조회
        node_info = manager.get_node(new_node['id'])
        print("노드 정보:", node_info)

        # 노드의 엣지 조회 예시
        node_edges = manager.get_node_edges(new_node['id'])
        print("노드의 엣지:", node_edges)

        # 노드 삭제 예시
        deleted = manager.delete_node(new_node['id'])
        print("노드 삭제 성공:", deleted)

if __name__ == "__main__":
    main()