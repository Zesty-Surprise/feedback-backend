from fastapi import APIRouter, Depends, HTTPException

from app.repository.template import db_get_template_by_id
from ....db.mongodb import AsyncIOMotorClient, get_database
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

router = APIRouter(tags=["Template"])

@router.get("/templates")
async def get_all_templates(db: AsyncIOMotorClient = Depends(get_database)):
    templates = await cont_get_templates(db)
    return templates

@router.get("/templates/{id}", response_model=Template)
async def get_template(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    template = await cont_get_template_by_id(id, db)
    if template:
        return template
    raise HTTPException(404, f"template {id} not found")

@router.post("/templates", response_model=Template)
async def create_template(template: TemplateCreate, db: AsyncIOMotorClient = Depends(get_database)):
    template = await cont_create_template(template, db)
    if template:
        return template
    return HTTPException(404, f"template failed to create")

@router.put("/templates/{id}")
async def update_template(id: str, request: TemplateUpdate, db: AsyncIOMotorClient = Depends(get_database)):
    update = await cont_update_template_by_id(id, request, db)
    if update:
        return {"msg": f"updated template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")

@router.delete("/templates/{id}")
async def delete_template(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    delete = await cont_delete_template_by_id(id, db)
    if delete:
        return {"msg": f"deleted template with id:{id}"}
    raise HTTPException(404, f"template {id} not found")
