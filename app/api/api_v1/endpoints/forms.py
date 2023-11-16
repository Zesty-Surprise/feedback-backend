from fastapi import APIRouter, Depends, HTTPException

from ....db.mongodb import AsyncIOMotorClient, get_database

from ..controllers.forms import (
    cont_get_forms,
    cont_get_forms_by_id,
    cont_update_forms_by_id
)

router = APIRouter(tags=["Forms"])

# NOT SURE IF WE NEED THIS
# @router.get("/forms")
# async def get_all_forms_by_session(session_id:str, db: AsyncIOMotorClient = Depends(get_database)):
#     forms = await cont_get_forms(session_id, db)
#     return forms

# NOT SURE IF WE NEED THIS
# @router.get("/forms/{form_id}")
# async def get_form_by_id(form_id:int, session_id:str, db: AsyncIOMotorClient = Depends(get_database)):
#     form = await cont_get_forms_by_id(form_id, session_id, db)
#     return form

@router.get("/file/{form_id}")
async def complete_form(session_id:str, score: int, dep: str, form_id:int, db: AsyncIOMotorClient = Depends(get_database)):
    update = await cont_update_forms_by_id(score, dep, form_id, session_id, db)
    if update:
        return {"msg":f"updated form with id:{form_id} from session:{session_id} "}
    raise HTTPException(404, f"form {id} not found")