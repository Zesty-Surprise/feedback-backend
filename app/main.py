from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection
from app.api.api_v1.api import router as api_router
from .core.config import secret_key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins="ALLOWED_HOSTS_HERE",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return HTMLResponse('<body><a href="/api/login">Log In</a></body>')
