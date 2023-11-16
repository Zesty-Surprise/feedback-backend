from ..db.mongodb import AsyncIOMotorClient
from ..models.session import FeedbackSessionCreate, FeedbackSessionUpdate, FeedbackSessionDatabase, FeedbackSession
from ..core.config import database_name, session_collection_name

from typing import List
from bson import ObjectId

async def db_get_sessions(db: AsyncIOMotorClient) -> List[FeedbackSessionDatabase]:
    sessions : List[FeedbackSessionDatabase] = []
    session_docs = db[database_name][session_collection_name].find()
    async for session in session_docs:
        sessions.append(FeedbackSessionDatabase(**session))
    return sessions

async def db_create_session(session: FeedbackSessionCreate, db):
    new_session = await db[database_name][session_collection_name].insert_one(session)
    return await db[database_name][session_collection_name].find_one({"_id": new_session.inserted_id})

async def db_get_session_by_id(id:str, db: AsyncIOMotorClient)->FeedbackSessionDatabase:
    session : FeedbackSessionDatabase = await db[database_name][session_collection_name].find_one({"_id": ObjectId(id)})
    return session

async def db_update_session_by_id(id:str, req: FeedbackSessionUpdate, db:AsyncIOMotorClient):
    request = {k: v for k, v in req.model_dump().items() if v is not None}
    update = await db[database_name][session_collection_name].update_one({"_id": ObjectId(id)}, {"$set": request})
    if update:
        return True
    return False

async def db_delete_sessions_by_id(id: str, db:AsyncIOMotorClient) -> bool:
    delete = await db[database_name][session_collection_name].delete_one({"_id": ObjectId(id)})
    if delete.deleted_count:
        return True
    return False