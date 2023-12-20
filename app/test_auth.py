import os
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import json
import pytest
from app.main import app
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection, db
from app.db.mongodb import get_database, get_testing_database

# client = TestClient(app)
# mongo_client = MongoClient('mongodb://localhost:27017/')
# db = mongo_client["testing"]

# app.dependency_overrides[get_database] = get_testing_database

client = TestClient(app)
mongodb_url = os.environ.get('MONGODB_URL')
db.client = AsyncIOMotorClient(mongodb_url)

app.dependency_overrides[get_database] = get_testing_database

def test_post_user():
    data = {"email": "admin@example.com","password": "Password123!","username": "admin"}
    response = client.post("/api/users", json=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "admin@example.com"
    assert response.json()["username"] == "admin"

def test_authenticate_user():
    # test_data = {"username": "admin@example.com", "password": "Password123!", "grant_type": "", "client_id": "", "client_secret": ""}
    test_email = "admin@example.com"
    test_password = "Password123!"
    test_data = {
        "grant_type": "",
        "username": test_email,
        "password": test_password,
        "client_id": "",
        "client_secret": "",
    }
    
    response = client.post("/api/token", data=test_data)
    assert response.status_code == 200


# def test_get_templates_no_params():
#     response = client.get("api/templates")
#     assert response.status_code == 200
