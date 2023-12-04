import logging
from typing import Annotated
from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Depends, HTTPException, Request, status, Query
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from ....core.config import  google_client_id, google_client_secret, secret_key
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import authenticate_user, get_current_user, cont_create_user, create_token, valid_email_from_db

from ....models.token import Token
from ....models.user import User

router = APIRouter(tags=["Auth"])

# Configuration data
config_data = {'GOOGLE_CLIENT_ID': google_client_id, 'GOOGLE_CLIENT_SECRET': google_client_secret}

# Create an instance of the OAuth class
oauth = OAuth()

# Register the Google OAuth provider
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
    client_id=config_data['GOOGLE_CLIENT_ID'],
    client_secret=config_data['GOOGLE_CLIENT_SECRET'],
)

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)

@router.post("/users", response_model=User)
async def add_user(user: User, db: AsyncIOMotorClient = Depends(get_database)):
    user = await cont_create_user(user, db)    
    if user:
        return user
    return HTTPException(404, f"user failed to create")

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncIOMotorClient = Depends(get_database), 
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_token(user["username"])
    return {"access_token": access_token, "token_type": "bearer"}

# Google Authentication
@router.get('/login')
async def google_login(request: Request):
    google = oauth.create_client('google')
    redirect_uri = "http://localhost:5173/auth/google_login"
    return await google.authorize_redirect(request, redirect_uri)

@router.get('/token', name="token")
async def google_auth(request: Request, db: AsyncIOMotorClient = Depends(get_database)):
    google = oauth.create_client('google')
    try:
        access_token = await google.authorize_access_token(request)
    except OAuthError as e:
        logging.error(f"OAuthError: {e}")
        raise CREDENTIALS_EXCEPTION
    user_data = access_token['userinfo']
    if await valid_email_from_db(user_data["email"], db):
        return {"access_token": create_token(user_data["email"]), "token_type": "bearer"}
    raise CREDENTIALS_EXCEPTION
