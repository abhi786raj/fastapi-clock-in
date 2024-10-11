from fastapi import FastAPI
from routes.item_routes import router as item_router
from routes.clock_in_routes import router as clock_in_router
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = FastAPI(
    title="FastAPI CRUD Application",
    description="API for managing inventory items and user clock-in records.",
    version="1.0.0",
)

# Registering the routes with tags
app.include_router(item_router, prefix="/items", tags=["Items"])
app.include_router(clock_in_router, prefix="/clock-in", tags=["Clock-In Records"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the FastAPI CRUD Application"}
