from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.session import (
    cont_get_session_by_id
)
from ....repository.template import (
    db_get_template_by_id
)
from ....core.amp import build_html

router = APIRouter(tags=["Email"])
@router.get("/submit", response_class=HTMLResponse)
async def get_submit_view(form_id:int, session_id:str,  db: AsyncIOMotorClient = Depends(get_database)):

    session = await cont_get_session_by_id(session_id, db)
    template_id = session.template
    template = await db_get_template_by_id(template_id, db)
    url = str(form_id) + "?session_id=" + str(session_id)
    html = build_html(template['components'], url)
    
    return html