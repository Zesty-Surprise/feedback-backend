import logging
import os
from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db

async def connect_to_mongo():
    mongodb_url = os.environ.get('MONGODB_URL') or "mongodb://admin:password123@localhost:6000"
    db.client = AsyncIOMotorClient(mongodb_url)

async def close_mongo_connection():
    db.client.close()
