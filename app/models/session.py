from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

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
    template: str

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
    template: str
    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    forms:List[SessionForm]

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_encoders = {PyObjectId: str}

class FeedbackSessionCreate(BaseModel):
    title: str
    destination: str
    enps: int
    form_count: int
    template: str
    date_created: datetime = Field(default_factory=datetime_now)
    date_updated: Optional[datetime] = None
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
                "template":"",
                "forms":[]
            }
        }

class FeedbackSessionUpdate(BaseModel):
    title: Optional[str] = None
    destination: Optional[str] = None
    enps: Optional[int] = None
    template: Optional[str] = None
    forms:List[SessionForm] = None
    date_created: Optional[datetime] = None
    date_updated: datetime = Field(default_factory=datetime_now)

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "destination": "*@ys.com",
                "enps": 0,
                "template":"",
                "forms":[]
            }
        }


