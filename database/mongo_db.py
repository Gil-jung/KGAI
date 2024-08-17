import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()

class MongoDatabase:
    def __init__(self):
        uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB_NAME")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db.markdown_documents

    def create_document(self, node_id, content):
        document = {
            "node_id": node_id,
            "content": content
        }
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def get_document(self, node_id):
        document = self.collection.find_one({"node_id": node_id})
        if document:
            document['_id'] = str(document['_id'])
        return document

    def update_document(self, node_id, content):
        result = self.collection.update_one(
            {"node_id": node_id},
            {"$set": {"content": content}}
        )
        return result.modified_count

    def delete_document(self, node_id):
        result = self.collection.delete_one({"node_id": node_id})
        return result.deleted_count

# MongoDB 데이터베이스 인스턴스 생성
mongo_db = MongoDatabase()


if __name__ == "__main__":
    try:
        # 간단한 쿼리 실행
        result = mongo_db.collection.find_one()
        print("MongoDB Atlas 연결 성공!")
        print("첫 번째 문서:", result)
    except Exception as e:
        print(f"MongoDB Atlas 연결 실패: {e}")