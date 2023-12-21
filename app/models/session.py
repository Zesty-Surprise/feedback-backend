from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel, Field, computed_field
from functools import cached_property
from app.core.objectID import PyObjectId

def datetime_now():
    return datetime.now(timezone.utc)

class FormCustomComponent(BaseModel):
    id: int
    custom: str

class SessionForm(BaseModel):
    form_id: str
    completed: bool
    score: Optional[int] = None 
    department: Optional[str] = None
    date_completed: Optional[datetime] = None
    custom: Optional[List[FormCustomComponent]] = None

class Session(BaseModel):
    id: PyObjectId = Field(alias="_id")
    title: str
    date_created: Optional[datetime] = None
    date_updated: Optional[datetime] = None
    emails: List[str]
    template: str
    form_count:int
    forms:Optional[List[SessionForm]] = None
    deployed: bool
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_encoders = {PyObjectId: str}

class SessionShort(Session):
    participants: int
    completed:int
    promoters:int
    passive:int
    demoter:int
    score:float

class SessionDatabase(Session):
    forms:List[SessionForm]
    
class SessionLong(Session):
    forms:List[SessionForm]

    @computed_field(return_type=int)
    @cached_property
    def participants(self):
        return len(self.emails)

    @computed_field(return_type=int)
    @cached_property
    def completed(self):
        count=0
        for form in self.forms:
            if form.completed:
                count += 1
        return count
    
    @computed_field(return_type=int)
    @cached_property
    def promoters(self):
        count=0
        for form in self.forms:
            if form.completed:
                if form.score > 8:
                    count+=1
        return count

    @computed_field(return_type=int)
    @cached_property
    def passive(self):
        count=0
        for form in self.forms:
            if form.completed:
                if 6 < form.score < 9:
                    count+=1
        return count
    
    @computed_field(return_type=int)
    @cached_property
    def demoter(self):
        count=0
        for form in self.forms:
            if form.completed:
                if form.score < 7:
                    count+=1
        return count
    
    # Reason, you cant divide with zero
    @computed_field(return_type=float)
    def score(self):
        score = 0.0
        if self.completed > 0:
            score = ((self.promoters-self.demoter)/self.completed)*100
        return score
        

class SessionCreate(BaseModel):
    title: str
    emails: List[str]
    form_count: int
    template: str
    form_count:int
    date_created: datetime = Field(default_factory=datetime_now)
    date_updated: Optional[datetime] = None
    forms:Optional[List[SessionForm]] = None
    deployed: bool
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "emails": ["bobpanda.bp@gmail.com"],
                "form_count":1,
                "template":"",
                "forms":[],
                "deployed": False
            }
        }

class SessionUpdate(BaseModel):

    title: Optional[str] = None
    emails: Optional[List[str]] = None
    template: Optional[str] = None
    forms: List[SessionForm] = None
    date_updated: datetime = Field(default_factory=datetime_now)
    deployed: Optional[bool] = None

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed=True
        json_schema_extra = {
            "example": {
                "title": "Sample eNPS Survey",
                "emails": ["bobpanda.bp@gmail.com"],
                "template":"",
                "forms":[]
            }
        }


