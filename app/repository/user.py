from passlib.context import CryptContext
from ..models.user import  User, ReadUser
from ..core.config import database_name, user_collection_name
from ..db.mongodb import AsyncIOMotorClient, get_database


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_admin_user(db:AsyncIOMotorClient):
    admin_user = {
        "email": "admin@example.com",
        "password": "Password123!",
        "role": "admin",
        "username": "admin"
    }
    await db_create_user(admin_user, db)


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

async def db_get_all_users(db:AsyncIOMotorClient):
    users: list[ReadUser] = []
    user_docs = db[user_collection_name].find()
    async for session in user_docs:
        u = ReadUser(**session)
        if u.role != "admin":
            users.append(u)
    return users

async def db_delete_user(email:str, db: AsyncIOMotorClient):
    delete = await db[user_collection_name].delete_one({"email": email})
    if delete.deleted_count:
        return True
    return False
