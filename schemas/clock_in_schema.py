from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ClockInCreate(BaseModel):
    email: EmailStr
    location: str

class ClockInUpdate(BaseModel):
    email: Optional[EmailStr]
    location: Optional[str]

class ClockInRequest(BaseModel):
    email: str
    location: str

class ClockInResponse(BaseModel):
    id: str
    email: str
    location: str
    insert_datetime: datetime

    class Config:
        json_schema_extra = {}  # Update from 'schema_extra' to 'json_schema_extra'
        from_attributes = True  # Update from 'orm_mode' to 'from_attributes'
