from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field

def datetime_now():
    return datetime.now(timezone.utc)

class User(BaseModel):
    username: str
    email: str
    password: str 
    date_created: datetime = Field(default_factory=datetime_now)
    date_updated: Optional[datetime] = None
    role: str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "username": "sample",
                "email": "sample@example.com",
                "password":"Password123!",
                "role":"admin or IT or Gifts..."
            }
        }

class ReadUser(BaseModel):
    username: str
    email: str
    date_created: datetime = Field(default_factory=datetime_now)
    date_updated: Optional[datetime] = None
    role: str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
