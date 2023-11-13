from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.core.objectID import PyObjectId

class Template(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True

class TemplateCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True
        json_schema_extra = {
           "example": {
                "name": "survey",
            }
        }

class TemplateUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        json_encoders = {PyObjectId: str}
        arbitrary_types_allowed=True
