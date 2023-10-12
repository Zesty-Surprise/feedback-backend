import logging

from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db

async def connect_to_mongo():
    db.client = AsyncIOMotorClient("mongodb://admin:password123@localhost:6000")

async def close_mongo_connection():
    db.client.close()
