from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import get_current_user
from ..controllers.template import (
    cont_get_templates,
    cont_create_template,
    cont_get_template_by_id,
    cont_update_template_by_id,
    cont_delete_template_by_id
)
from app.models.template import (
    Template,
    TemplateCreate,
    TemplateUpdate
)
from ....models.user import User

router = APIRouter(tags=["Template"])

@router.get("/templates")
async def get_all_templates(
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    templates = await cont_get_templates(db)
    return templates

@router.get("/templates/{id}", response_model=Template)
async def get_template(
    id: str, 
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    template = await cont_get_template_by_id(id, db)
    if template:
        return template
    raise HTTPException(404, f"template {id} not found")

@router.post("/templates", response_model=Template)
async def create_template(
    template: TemplateCreate, 
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    template = await cont_create_template(template, db)
    if template:
        return template
    return HTTPException(404, f"template failed to create")

@router.put("/templates/{id}")
async def update_template(
    id: str, 
    request: TemplateUpdate, 
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    update = await cont_update_template_by_id(id, request, db)
    if update:
        return {"msg": f"updated template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")

@router.delete("/templates/{id}")
async def delete_template(
    id: str, 
    current_user: Annotated[User, Depends(get_current_user)],
    db: AsyncIOMotorClient = Depends(get_database)
):
    delete = await cont_delete_template_by_id(id, db)
    if delete:
        return {"msg": f"deleted template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")
