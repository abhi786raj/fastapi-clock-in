from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["myDatabase"]  # Replace with your database name
clock_in_collection = db["clock_in_records"]

class ClockInModel:
    @staticmethod
    def insert_clock_in(clock_in_data):
        clock_in_data["insert_datetime"] = datetime.utcnow()
        result = clock_in_collection.insert_one(clock_in_data)
        return str(result.inserted_id)

    @staticmethod
    def find_clock_in_by_id(clock_in_id):
        clock_in = clock_in_collection.find_one({"_id": ObjectId(clock_in_id)})
        if clock_in:
            # Convert ObjectId to string for the response
            clock_in['id'] = str(clock_in.pop('_id'))  # Rename '_id' to 'id'
        return clock_in

    @staticmethod
    def update_clock_in(clock_in_id, clock_in_data):
        result = clock_in_collection.update_one({"_id": ObjectId(clock_in_id)}, {"$set": clock_in_data})
        return result.modified_count > 0

    @staticmethod
    def delete_clock_in(clock_in_id):
        result = clock_in_collection.delete_one({"_id": ObjectId(clock_in_id)})
        return result.deleted_count > 0

    @staticmethod
    def find_clock_ins(query):
        clock_ins = list(clock_in_collection.find(query))
        for clock_in in clock_ins:
            clock_in['id'] = str(clock_in.pop('_id'))  # Rename '_id' to 'id'
        return clock_ins
