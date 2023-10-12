from fastapi import APIRouter, Depends, HTTPException

from ....repository.session import (
    db_get_session_by_id,
    db_get_sessions,
    db_create_session,
    db_delete_sessions_by_id,
    db_update_session_by_id
)
from ....db.mongodb import AsyncIOMotorClient, get_database
from app.models.sessions import FeedbackSession, FeedbackSessionCreate, FeedbackSessionUpdate

router = APIRouter(tags=["Sessions"])

@router.get("/sessions")
async def get_sessions(db: AsyncIOMotorClient = Depends(get_database)):
    sessions = await db_get_sessions(db)
    return sessions

@router.get("/sessions/{id}", response_model=FeedbackSession)
async def get_session(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    session = await db_get_session_by_id(id, db)
    if session:
        return session
    raise HTTPException(404, f"sessions {id} not found")

@router.post("/sessions", response_model=FeedbackSession)
async def add_session(session: FeedbackSessionCreate, db: AsyncIOMotorClient = Depends(get_database)):
    session = await db_create_session(session, db)
    if session:
        return session
    return HTTPException(404, f"session failed to create not")

@router.put("/sessions/{id}", response_model=FeedbackSessionUpdate)
async def update_session(id: str, request: FeedbackSessionUpdate, db: AsyncIOMotorClient = Depends(get_database)):
    update =  await db_update_session_by_id(id, request, db)
    if update:
        return {"msg":f"updated session with id:{id}"}
    raise HTTPException(404, f"sessions {id} not found")

@router.delete("/sessions/{id}")
async def delete_session(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    delete = await db_delete_sessions_by_id(id, db)
    if delete:
        return {"msg":f"deleted session with id:{id}"}
    raise HTTPException(404, f"session {id} not found")