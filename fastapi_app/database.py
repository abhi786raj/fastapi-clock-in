import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB URI and connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["myDatabase"]

# Collections
items_collection = db["items"]
clock_in_collection = db["clock_in_records"]
