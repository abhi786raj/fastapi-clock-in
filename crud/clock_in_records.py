from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client["myDatabase"]  # Replace with your database name
clock_in_collection = db["clock_in_records"]

async def create_clock_in(clock_in_data: dict):
    clock_in_data['insert_datetime'] = datetime.utcnow()  # Add insert_datetime
    result = await clock_in_collection.insert_one(clock_in_data)
    
    # Create a new dictionary to return with the correct ObjectId
    return {
        "id": str(result.inserted_id),  # Convert ObjectId to string
        **clock_in_data  # Return the modified data
    }

async def get_clock_in_by_id(clock_in_id: str):
    clock_in = await clock_in_collection.find_one({"_id": ObjectId(clock_in_id)})
    if not clock_in:
        return None
    
    # Convert the MongoDB ObjectId to string and set it as 'id'
    return {
        "id": str(clock_in["_id"]),  # Convert ObjectId to string
        "email": clock_in["email"],
        "location": clock_in["location"],
        "insert_datetime": clock_in["insert_datetime"],
    }

async def update_clock_in(clock_in_id: str, clock_in: dict):
    result = await clock_in_collection.update_one({"_id": ObjectId(clock_in_id)}, {"$set": clock_in})
    return result.modified_count > 0

async def delete_clock_in(clock_in_id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(clock_in_id)})
    return result.deleted_count > 0

async def filter_clock_ins(filters: dict):
    query = {}
    if "email" in filters:
        query["email"] = filters["email"]
    if "location" in filters:
        query["location"] = filters["location"]
    if "insert_datetime" in filters:
        # Assuming you want to filter by exact match or a condition
        query["insert_datetime"] = {"$gt": filters["insert_datetime"]}  # Change this logic if needed

    clock_ins = []
    async for clock_in in clock_in_collection.find(query):
        clock_in["_id"] = str(clock_in["_id"])  # Convert ObjectId to string
        clock_ins.append(clock_in)
    return clock_ins
