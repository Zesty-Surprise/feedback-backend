from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId

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
    components:List[TemplateComponent]
    # html: str

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True

class TemplateCreate(BaseModel):
    name: str
    components:List[TemplateComponent]
    html: str

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
                # "html":""
            }
        }

class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    components:Optional[List[TemplateComponent]] = None
    # html: Optional[str] = None
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
                # "html":""
            }
        }
