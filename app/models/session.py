from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId

class SessionForm(BaseModel):
    form_id: int
    completed: bool
    score: Optional[int] = None 
    department: Optional[str] = None

class FeedbackSessionShort(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    destination: str
    enps: int

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_encoders = {PyObjectId: str}

class FeedbackSession(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    destination: str
    enps: int
    forms:List[SessionForm]

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_encoders = {PyObjectId: str}
        json_schema_extra = {
           "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0,
                "form_count":1,
                "forms":[{
                    "form_id" : 0,
                    "completed":False,
                    "score":0,
                    "department":""
                }]
            }
        }

class FeedbackSessionCreate(BaseModel):
    title: str
    destination: str
    enps: int
    form_count: int
    forms:Optional[List[SessionForm]] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0,
                "form_count":1,
                "forms":[{
                    "form_id" : 0,
                    "completed":False,
                    "score":0,
                    "department":""
                }]
            }
        }

class FeedbackSessionUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    enps: Optional[int] = None
    forms:List[SessionForm] = None
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0,
                "form_count":1,
                "forms":[{
                    "form_id" : 0,
                    "completed":False,
                    "score":0,
                    "department":""
                }]
            }
        }


