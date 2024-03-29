from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Request

import re

from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import get_current_user
from ....models.user import User

from ..controllers.forms import (
    # cont_get_forms,
    # cont_get_forms_by_id,
    cont_update_forms_by_id
)

from ....models.session import FormCustomComponent

router = APIRouter(tags=["Forms"])

@router.get("/file/{session_id}/{form_id}")
async def complete_form(
    request: Request, 
    session_id:str, 
    form_id:str, 
    score: int = Query(..., description="A required fixed parameter"), 
    dep: str = Query(..., description="A required fixed parameter"), 
    db: AsyncIOMotorClient = Depends(get_database),
):

    custom = []
    for key in request.query_params:
        k = str(key)
        if "custom" in k:
            match  = re.search(r'\d+', str(k))
            id = int(match.group()) if match else None
            comp = FormCustomComponent.model_construct(id=id, custom=request.query_params[k])
            custom.append(comp)

    update = await cont_update_forms_by_id(score, dep, form_id, session_id, db, custom)
    if update:
        return {"msg":f"updated form with id:{form_id} from session:{session_id} "}
    raise HTTPException(404, f"form {id} not found")
