from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection
from app.api.api_v1.api import router as api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins="ALLOWED_HOSTS_HERE",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message":"alive"}
