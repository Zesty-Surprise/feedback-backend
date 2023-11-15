from fastapi.encoders import jsonable_encoder
from typing import List
from ....repository.session import (
    db_get_session_by_id,
    db_get_sessions,
    db_create_session,
    db_delete_sessions_by_id,
    db_update_session_by_id
)
from app.models.session import (
    FeedbackSession,
    FeedbackSessionShort,
    FeedbackSessionCreate, 
    FeedbackSessionUpdate,
    SessionForm
)
from ....db.mongodb import AsyncIOMotorClient

async def cont_get_sessions(db: AsyncIOMotorClient):
    sessions = await db_get_sessions(db)
    return sessions

async def cont_create_session(session: FeedbackSessionCreate, db: AsyncIOMotorClient):
    session = jsonable_encoder(session)
    session["forms"] = []
    for i in range(0, session["form_count"]):
        new_form : SessionForm = {
            "form_id" : i,
            "completed":False,
            "score":None,
            "department":None,
            "date_completed":None
        }
        session["forms"].append(new_form)
    session = await db_create_session(session, db)
    return session

async def cont_get_session_by_id(id: str, db: AsyncIOMotorClient, dep: str = None, short: bool = None):
    session = await db_get_session_by_id(id, db)
    if dep:
        session['forms'] = [form for form in session['forms'] if form['department'] == dep]
    session = FeedbackSession.model_validate(session)
    if short:
        session = FeedbackSessionShort.model_validate(session)
        return session
    return session    

async def cont_update_session_by_id(id: str, request: FeedbackSessionUpdate, db: AsyncIOMotorClient):
    update =  await db_update_session_by_id(id, request, db)
    return update

async def cont_delete_session_by_id(id: str, db:AsyncIOMotorClient):
    delete = await db_delete_sessions_by_id(id, db)
    return delete