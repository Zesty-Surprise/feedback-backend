from typing import Annotated

from fastapi import APIRouter, Depends
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....repository.session import db_create_session
from ..controllers.auth import get_current_user
from ....models.user import User
from ..controllers.template import (
    cont_create_template
)
from ....core.seed import session, template

router = APIRouter(tags=["Seeder"])

@router.post("/seed")
async def seed_database(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    t = await cont_create_template(template, db)
    session['template'] = str(t['_id'])
    seed = await db_create_session(session, db)
    return {"message":"Seeded Database"}