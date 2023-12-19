from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.models.permissions import PermissionChecker
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import get_current_user

from ..controllers.session import (
    cont_get_sessions,
    cont_get_session_by_id,
    cont_create_session,
    cont_update_session_by_id,
    cont_delete_session_by_id,
)

from app.models.session import (
    SessionCreate, 
    SessionUpdate
)

router = APIRouter(tags=["Sessions"])

@router.get("/sessions")
async def get_all_sessions(
    authorized: any = Depends(PermissionChecker(required_permissions=["sessions:read"])),
    db: AsyncIOMotorClient = Depends(get_database), 
    dep: str = None, 
    short: bool = None
):  
    if authorized['filter'] != None:
        sessions = await cont_get_sessions(db, authorized["filter"], short)
    else:
        sessions = await cont_get_sessions(db, dep, short)
    return sessions

@router.get("/sessions/{id}")
async def get_session(
    id: str, 
    authorized: bool = Depends(PermissionChecker(required_permissions=["sessions:read"])),
    db: AsyncIOMotorClient = Depends(get_database), 
    dep: str = None, 
    short: bool = None
):  
    if authorized['filter'] != None:
        session = await cont_get_session_by_id(id, db, authorized["filter"], short)
    else:
        session = await cont_get_session_by_id(id, db, dep, short)

    if session:
        return session
    raise HTTPException(404, f"sessions {id} not found")

@router.post("/sessions", response_model=SessionCreate)
async def add_session(
    session: SessionCreate,    
    authorized: bool = Depends(PermissionChecker(required_permissions=["sessions:write"])),
    db: AsyncIOMotorClient = Depends(get_database)
):
    session = await cont_create_session(session, db)  
    if session:
        return session
    return HTTPException(404, f"session failed to create")

@router.put("/sessions/{id}", response_model=SessionUpdate)
async def update_session(
    id: str, 
    request: SessionUpdate, 
    authorized: bool = Depends(PermissionChecker(required_permissions=["sessions:write"])),
    db: AsyncIOMotorClient = Depends(get_database)
):
    update =  await cont_update_session_by_id(id, request, db)
    if update:
        return {"msg":f"updated session with id:{id}"}
    raise HTTPException(404, f"sessions {id} not found")
 
@router.delete("/sessions/{id}")
async def delete_session(
    id: str, 
    authorized: bool = Depends(PermissionChecker(required_permissions=["sessions:write"])),
    db: AsyncIOMotorClient = Depends(get_database)
):
    delete = await cont_delete_session_by_id(id, db)
    if delete:
        return {"msg":f"deleted session with id:{id}"}
    raise HTTPException(404, f"session {id} not found")
