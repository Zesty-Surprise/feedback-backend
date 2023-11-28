from fastapi import APIRouter, Depends, BackgroundTasks 
from fastapi.responses import HTMLResponse
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.session import (
    cont_get_session_by_id
)
from ....repository.template import (
    db_get_template_by_id
)
from ..controllers.email import (
    cont_get_html,
    cont_send_email
)

router = APIRouter(tags=["Email"])
@router.get("/email/submit/{session_id}/{form_id}")
async def complete_form(session_id:str, form_id:int, db: AsyncIOMotorClient = Depends(get_database)):
    session = await cont_get_session_by_id(session_id, db)
    template_id = session.template
    template = await db_get_template_by_id(template_id, db)
    html = cont_get_html(template, session_id, form_id)
    
    return HTMLResponse(content=html, status_code=200)

@router.get("/email/send", status_code=200)
async def get_send_email(background_tasks: BackgroundTasks, session_id:str, form_id:int, db: AsyncIOMotorClient = Depends(get_database)):
    # 1. Get session information
    # 2. Retrieve template from session
    # 3. Generate HTML document from template
    # 4. Retrieve list of email address (i.e., destination) from session
    # 5. Retrieve object (or title) of email from session
    #    Currently "*@ysp.com" so doesn't work. When fixed, use session.destination

    session = await cont_get_session_by_id(session_id, db)
    template_id = session.template
    template = await db_get_template_by_id(template_id, db)

    success = cont_send_email(background_tasks, "TEST - Feedback form", ["bobpanda.bp@gmail.com"], template, session_id, form_id)

    if success: 
        return {"message": "Successfully sent email(s)."}
    
    return {"message": "Failled to send email(s)."}


