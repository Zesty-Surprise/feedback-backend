from datetime import datetime, timezone
from ....repository.session import (
    db_get_session_by_id,
    db_update_session_by_id
)
from app.models.session import (
    SessionUpdate,
    SessionForm
)
from ....db.mongodb import AsyncIOMotorClient

async def cont_get_forms(id: str, db:AsyncIOMotorClient):
    session = await db_get_session_by_id(id, db)
    forms = session["forms"]
    return forms

async def cont_get_forms_by_id(form_id:int, session_id:str, db:AsyncIOMotorClient):
    session = await db_get_session_by_id(session_id, db)
    selected_form : SessionForm = {}
    for form in session["forms"]:
        if form["form_id"] == form_id:
            selected_form = form
    return selected_form

async def cont_update_forms_by_id(score: int, dep: str, form_id:int, session_id:str, db:AsyncIOMotorClient):
    form = await cont_get_forms_by_id(form_id, session_id, db)
    if form["completed"]:
        return
    forms = await cont_get_forms(session_id, db)
    update_form : SessionForm = {
            "form_id" : form_id,
            "completed":True,
            "score":score,
            "department":dep,
            "date_completed": datetime.now(timezone.utc)
    }
    for i, form in enumerate(forms):
        if form["form_id"] == form_id:
            forms[i] = update_form
    form_models = []
    for form in forms:
        form_models.append(SessionForm.model_construct(form_id=form["form_id"], completed=form["completed"], score=form["score"], department=form["department"], date_completed=form['date_completed']))
    session = SessionUpdate.model_construct(title=None, destination=None, enps=None, forms=form_models)
    update = await db_update_session_by_id(session_id, session, db)
    return update