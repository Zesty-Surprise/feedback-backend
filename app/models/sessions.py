from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId

class FeedbackSession(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    destination: str
    enps: int

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_encoders = {PyObjectId: str}
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0
            }
        }

class FeedbackSessionCreate(BaseModel):
    title: str
    destination: str
    enps: int

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0
            }
        }

class FeedbackSessionUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    enps: Optional[int] = None
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0
            }
        }


