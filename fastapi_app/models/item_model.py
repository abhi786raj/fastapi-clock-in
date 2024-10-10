from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["myDatabase"]  # Replace with your database name
items_collection = db["items"]

class ItemModel:
    @staticmethod
    def insert_item(item_data):
        result = items_collection.insert_one(item_data)
        return str(result.inserted_id)

    @staticmethod
    def find_item_by_id(item_id):
        item = items_collection.find_one({"_id": ObjectId(item_id)})
        return item

    @staticmethod
    def update_item(item_id, item_data):
        result = items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
        return result.modified_count > 0

    @staticmethod
    def delete_item(item_id):
        result = items_collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count > 0

    @staticmethod
    def find_items(query):
        items = list(items_collection.find(query))
        return items
