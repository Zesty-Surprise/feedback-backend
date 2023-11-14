from datetime import datetime,  timezone
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class TemplateComponent(BaseModel):
    type: str 
    custom_text: str
    default_text: str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True

class Template(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str
    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    components:List[TemplateComponent]

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True

class TemplateCreate(BaseModel):
    name: str
    components:List[TemplateComponent]
    date_created: datetime = Field(default_factory=datetime_now)
    date_updated: Optional[datetime] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True
        json_schema_extra = {
           "example": {
                "name": "survey",
                "components" : [
                    {
                        "type":"enps-component",
                        "default_text":"Fill in the score!",
                        "custom_text":""
                    },
                    {
                        "type":"department-component",
                        "default_text":"Select your department!",
                        "custom_text":""
                    },
                    {
                        "type":"written-component",
                        "default_text":"Additional feedback?",
                        "custom_text":""
                    }
                ]
            }
        }

class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    components:Optional[List[TemplateComponent]] = None
    date_created: Optional[datetime] = None
    date_updated: datetime = Field(default_factory=datetime_now)
    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True
        json_schema_extra = {
           "example": {
                "name": "survey",
                "components" : [
                    {
                        "type":"enps-component",
                        "default_text":"Fill in the score!",
                        "custom_text":""
                    },
                    {
                        "type":"department-component",
                        "default_text":"Select your department!",
                        "custom_text":""
                    },
                    {
                        "type":"written-component",
                        "default_text":"Additional feedback?",
                        "custom_text":""
                    }
                ]
            }
        }
