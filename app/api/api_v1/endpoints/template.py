from typing import Annotated
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import get_current_active_user

from ....repository.template import (
    db_get_templates,
    db_create_template,
    db_get_template_by_id,
    db_update_template_by_id,
    db_delete_template_by_id
)
from app.models.template import (
    Template,
    TemplateCreate,
    TemplateUpdate
)
from ....models.user import User

from ....core.amp import build_html

router = APIRouter(tags=["Template"])

@router.get("/templates")
async def get_all_templates(    
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    templates = await db_get_templates(db)
    return templates

@router.get("/templates/{id}", response_model=Template)
async def get_template(
    id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    template = await db_get_template_by_id(id, db)
    if template:
        return template
    raise HTTPException(404, f"template {id} not found")

@router.post("/templates", response_model=Template)
async def create_template(
    template: TemplateCreate, 
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):    
    # Controller
    template = jsonable_encoder(template)
    template = await db_create_template(template, db)
    #---

    if template:
        return template
    return HTTPException(404, f"template failed to create")

@router.put("/templates/{id}")
async def update_template(
    id: str,
    request: TemplateUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    # Controller
    request = {k: v for k, v in request.model_dump().items() if v is not None}
    update = await db_update_template_by_id(id, request, db)
    #---
    if update:
        return {"msg": f"updated template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")

@router.delete("/templates/{id}")
async def delete_template(
    id: str,
    current_user: Annotated[User, Depends(get_current_active_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    delete = await db_delete_template_by_id(id, db)
    if delete:
        return {"msg": f"deleted template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")
