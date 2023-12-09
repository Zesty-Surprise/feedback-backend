from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection
from app.api.api_v1.api import router as api_router
from .core.config import secret_key

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://test.axelzublena.com",
    "https://amp.test.axelzublena.com",
    "https://front.test.axelzublena.com",
    "https://mail.google.com",
    "amp@gmail.dev",
]

@app.middleware("http")
async def amp_middelware(request: Request, call_next):
    response = await call_next(request)
    response.headers["AMP-Email-Allow-Sender"] = "*"
    response.headers['Access-Control-Expose-Headers'] = 'AMP-Access-Control-Allow-Source-Origin'
    response.headers['AMP-Access-Control-Allow-Source-Origin'] = "amp@gmail.dev"
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET, POST, OPTIONS, DELETE, PUT, UPDATE, HEAD"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return HTMLResponse('<body><a href="/api/login">Log In</a></body>')
