from passlib.context import CryptContext
from ..models.user import  User
from ..core.config import database_name, user_collection_name
from ..db.mongodb import AsyncIOMotorClient, get_database


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

async def db_get_user_by_email(db:AsyncIOMotorClient, email:str)->User:
    user : User = await db[user_collection_name].find_one({"email": email})
    return user

async def db_get_user_by_username(db:AsyncIOMotorClient, username:str)->User:
    user : User = await db[user_collection_name].find_one({"username": username})
    return user

async def db_create_user(user: User, db):
    user["password"] = get_password_hash(user["password"])
    new_user = await db[user_collection_name].insert_one(user)
    return await db[user_collection_name].find_one({"_id": new_user.inserted_id})