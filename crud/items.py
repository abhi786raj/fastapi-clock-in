from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from dotenv import load_dotenv
import os
from datetime import datetime, date
from schemas.item_schema import ItemResponse

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Use AsyncIOMotorClient for async operations
client = AsyncIOMotorClient(MONGO_URI)
db = client["your_database_name"]  # Replace with your database name
items_collection = db["items"]

async def create_item(item: dict):
    # Convert expiry_date from date to datetime if necessary
    if isinstance(item['expiry_date'], date):
        item['expiry_date'] = datetime.combine(item['expiry_date'], datetime.min.time())
    
    insert_date = datetime.now()
    item['insert_date'] = insert_date

    result = await items_collection.insert_one(item)

    # Return only the inserted ID as a string
    return str(result.inserted_id)

async def get_item_by_id(item_id):
    item = await items_collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        return None
    item["_id"] = str(item["_id"])
    return item

async def update_item(item_id, item):
    result = await items_collection.update_one({"_id": ObjectId(item_id)}, {"$set": item})
    return result.modified_count > 0

async def delete_item(item_id):
    result = await items_collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0

async def filter_items(filters):
    query = {}
    if "email" in filters:
        query["email"] = filters["email"]
    if "expiry_date" in filters:
        query["expiry_date"] = {"$gt": filters["expiry_date"]}
    if "insert_date" in filters:
        query["insert_date"] = {"$gt": filters["insert_date"]}
    if "quantity" in filters:
        query["quantity"] = {"$gte": filters["quantity"]}
    
    items = []
    async for item in items_collection.find(query):
        item["_id"] = str(item["_id"])
        items.append(item)
    
    return items


async def count_items_by_email():
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}},
    ]
    result = await items_collection.aggregate(pipeline).to_list(length=None)  # Ensure async call
    return result
