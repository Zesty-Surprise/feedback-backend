from fastapi import APIRouter, Depends, HTTPException

from ....db.mongodb import AsyncIOMotorClient, get_database

from ..controllers.session import (
    cont_get_sessions,
    cont_get_session_by_id,
    cont_create_session,
    cont_update_session_by_id,
    cont_delete_session_by_id,
)

from app.models.session import (
    FeedbackSession, 
    FeedbackSessionCreate, 
    FeedbackSessionUpdate,
)

router = APIRouter(tags=["Sessions"])

@router.get("/sessions")
async def get_all_sessions(db: AsyncIOMotorClient = Depends(get_database)):
    sessions = await cont_get_sessions(db)
    return sessions

@router.get("/sessions/{id}", response_model=FeedbackSession)
async def get_session(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    session = await cont_get_session_by_id(id, db)
    if session:
        return session
    raise HTTPException(404, f"sessions {id} not found")

@router.post("/sessions", response_model=FeedbackSessionCreate)
async def add_session(session: FeedbackSessionCreate, db: AsyncIOMotorClient = Depends(get_database)):
    session = await cont_create_session(session, db)    
    if session:
        return session
    return HTTPException(404, f"session failed to create")

@router.put("/sessions/{id}")
# @router.put("/sessions/{id}", response_model=FeedbackSessionUpdate)
async def update_session(id: str, request: FeedbackSessionUpdate, db: AsyncIOMotorClient = Depends(get_database)):
    update =  await cont_update_session_by_id(id, request, db)
    if update:
        return {"msg":f"updated session with id:{id}"}
    raise HTTPException(404, f"sessions {id} not found")
 
@router.delete("/sessions/{id}")
async def delete_session(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    delete = await cont_delete_session_by_id(id, db)
    if delete:
        return {"msg":f"deleted session with id:{id}"}
    raise HTTPException(404, f"session {id} not found")
