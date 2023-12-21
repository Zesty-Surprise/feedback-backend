import os
from fastapi import Depends
from fastapi.testclient import TestClient
from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from app.main import app
from app.db.mongodb_utils import db
from app.db.mongodb import get_database, get_testing_database
from app.api.api_v1.controllers.auth import get_current_user
from app.models.user import User


async def get_testing_user_for_test() -> User:
    # Return a mock user for testing purposes
    return User(username="test_user", email="test@example.com", password="Password123!")

client = TestClient(app)

@pytest.fixture(scope="function")
def set_db():
    mongodb_url = os.environ.get('MONGODB_URL')
    db.client = AsyncIOMotorClient(mongodb_url)
    return db.client

app.dependency_overrides[get_database] = get_testing_database
app.dependency_overrides[get_current_user] = get_testing_user_for_test

def test_post_user(set_db):
    data = {"email": "admin@example.com","password": "Password123!","username": "admin"}
    response = client.post("/api/users", json=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "admin@example.com"
    assert response.json()["username"] == "admin"

################ Sessions ####################
session_id = None

def test_post_session(set_db):
    data = {
            "emails": [
                "bobpanda.bp@gmail.com"
            ],
            "form_count": 1,
            "forms": [],
            "template": "",
            "title": "Sample eNPS Survey",
            "deployed": False
           }
    response = client.post("/api/sessions", json=data)
    global session_id
    session_id = response.json()["_id"]
    assert response.status_code == 200
    assert response.json()["title"] == "Sample eNPS Survey"

def test_get_sessions(set_db):
    response = client.get("/api/sessions")
    assert response.status_code == 200

def test_get_session_by_id(set_db):
    global session_id
    response = client.get(f"/api/sessions/{session_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Sample eNPS Survey"

def test_update_session(set_db):
    data = {
            "emails": [
                "bobpanda.bp@gmail.com"
            ],
            "forms": [],
            "template": "",
            "title": "Sample eNPS Survey"
           }
    global session_id
    response = client.put(f"/api/sessions/{session_id}", json=data)
    assert response.status_code == 200
    assert response.json()["msg"] == f"updated session with id:{session_id}"

def test_delete_session(set_db):
    global session_id
    response = client.delete(f"/api/sessions/{session_id}")
    assert response.status_code == 200

################ Templates ####################
template_id = None

def test_post_template(set_db):
    data = {
            "components": [
                {
                "custom_text": "Fill in the score!",
                "id": 0,
                "type": "enps-component"
                },
                {
                "custom_text": "Fill in the Department!",
                "id": 1,
                "type": "department-component"
                },
                {
                "custom_text": "Other questions?",
                "id": 2,
                "type": "custom-component"
                }
            ],
            "name": "survey"
           } 
    response = client.post("/api/templates", json=data)
    global template_id
    template_id = response.json()["_id"]
    assert response.status_code == 200
    assert response.json()["name"] == "survey"

def test_get_templates(set_db):
    response = client.get("/api/templates")
    assert response.status_code == 200

def test_get_template_by_id(set_db):
    global template_id
    response = client.get(f"/api/templates/{template_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "survey"

def test_update_template(set_db):
    data = {
            "components": [
                {
                "custom_text": "Fill in the score!",
                "id": 0,
                "type": "enps-component"
                },
                {
                "custom_text": "Fill in the Department!",
                "id": 1,
                "type": "department-component"
                },
                {
                "custom_text": "Other questions?",
                "id": 2,
                "type": "custom-component"
                }
            ],
            "name": "survey"
           }
    global template_id
    response = client.put(f"/api/templates/{template_id}", json=data)
    assert response.status_code == 200
    assert response.json()["msg"] == f"updated template with id:{template_id}"

def test_delete_template(set_db):
    global template_id
    response = client.delete(f"/api/templates/{template_id}")
    assert response.status_code == 200