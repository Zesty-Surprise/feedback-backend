from typing import Annotated
from app.models.permissions import PermissionChecker
from app.models.session import SessionUpdate
from app.repository.session import db_update_session_by_id

from fastapi import APIRouter, Depends, BackgroundTasks 
from fastapi.responses import HTMLResponse
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import get_current_user

from ..controllers.session import (
    cont_get_session_by_id,
    cont_update_session_by_id
)
from ..controllers.template import (
    cont_get_template_by_id
)
from ..controllers.email import (
    cont_get_html,
    cont_send_emails,
    cont_get_emails,
    cont_html_assemble
)

from ....models.user import User

router = APIRouter(tags=["Email"])
@router.get("/email/submit/{session_id}/{form_id}")
async def complete_form(
    session_id:str, 
    form_id:str, 
    db: AsyncIOMotorClient = Depends(get_database)
):
    session = await cont_get_session_by_id(session_id, db)
    template_id = session.template
    template = await cont_get_template_by_id(template_id, db)
    html = cont_get_html(template, session_id, form_id)
    
    return HTMLResponse(content=html, status_code=200)

@router.get("/email/{template_id}", response_class=HTMLResponse)
async def get_preview_template(
    template_id:str, 
    authorized: bool = Depends(PermissionChecker(required_permissions=["email:read"])),
    db: AsyncIOMotorClient = Depends(get_database)
):
    template = await cont_get_template_by_id(template_id,db)
    html = cont_html_assemble(template, "")
    return html

@router.get("/email/send/{session_id}", status_code=200)
async def get_send_email(
    background_tasks: BackgroundTasks, 
    session_id:str, 
    authorized: bool = Depends(PermissionChecker(required_permissions=["email:read"])),
    db: AsyncIOMotorClient = Depends(get_database)
):
    # 1. Get session information
    # 2. Retrieve template from session
    # 3. Generate HTML document from template
    # 4. Retrieve list of email address (i.e., destination) from session
    # 5. Retrieve object (or title) of email from session

    session = await cont_get_session_by_id(session_id, db)
    template_id = session.template
    template = await cont_get_template_by_id(template_id, db)
    emails = cont_get_emails(session, template)
    success = cont_send_emails(background_tasks, session.title , emails)

    session_update = SessionUpdate.model_construct(deployed=True)

    if success: 
        await cont_update_session_by_id(session_id, session_update, db)
        return {"message": "Successfully sent email(s)."}
    
    return {"message": "Failled to send email(s)."}


