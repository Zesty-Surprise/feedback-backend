from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import database_name, testing_database_name

class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()

async def get_database() -> AsyncIOMotorClient:
    return db.client[database_name]

async def get_testing_database() -> AsyncIOMotorClient:
    return db.client[testing_database_name]