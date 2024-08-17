import requests
import json
import os
import shutil

def read_markdown_file(filename):
    with open(os.path.join('docs', filename), 'r', encoding='utf-8') as file:
        return file.read()

def add_data():
    url = "http://localhost:8000/add_data"
    headers = {"Content-Type": "application/json"}
    
    try:
        with open('docs/nodes.json', 'r', encoding='utf-8') as file:
            nodes_data = json.load(file)
        
        for node in nodes_data:
            markdown_content = read_markdown_file(node['markdown_file'])
            node['markdown_content'] = markdown_content
        
        response = requests.post(url, json=nodes_data, headers=headers)
        response.raise_for_status()
        
        print("Data added successfully!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error adding data: {e}")
        return False
    except json.JSONDecodeError:
        print("Error reading nodes.json file")
        return False
    except IOError:
        print("Error reading markdown files")
        return False

def cleanup_files(nodes_data):
    # nodes.json 파일 삭제
    os.remove('docs/nodes.json')
    print("Removed nodes.json")

    # 각 노드의 Markdown 파일 삭제
    for node in nodes_data:
        markdown_file = os.path.join('docs', node['markdown_file'])
        if os.path.exists(markdown_file):
            os.remove(markdown_file)
            print(f"Removed {node['markdown_file']}")

    print("Cleanup completed.")

if __name__ == "__main__":
    # nodes.json 파일 읽기
    with open('docs/nodes.json', 'r', encoding='utf-8') as file:
        nodes_data = json.load(file)

    # 데이터 추가 시도
    if add_data():
        # 성공적으로 추가되었다면 파일들 삭제
        cleanup_files(nodes_data)
    else:
        print("Data addition failed. Files were not deleted.")