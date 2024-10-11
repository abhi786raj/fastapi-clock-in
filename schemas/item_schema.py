from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional
from bson import ObjectId

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Name of the person adding the item")
    email: EmailStr
    item_name: str = Field(..., min_length=1, max_length=100, description="Name of the item")
    quantity: int = Field(..., ge=1, description="Quantity of the item (must be positive)")
    expiry_date: date

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "item_name": "Apples",
                "quantity": 10,
                "expiry_date": "2024-12-01",
            }
        }

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr]
    item_name: Optional[str] = Field(None, min_length=1, max_length=100)
    quantity: Optional[int] = Field(None, ge=1)
    expiry_date: Optional[date]

class ItemResponse(BaseModel):
    id: str  # This should be defined as 'id'
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime

    class Config:
        # Use this if you want to handle BSON ObjectId correctly
        json_encoders = {
            ObjectId: lambda v: str(v)
        }
