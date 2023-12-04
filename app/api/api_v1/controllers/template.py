from fastapi.encoders import jsonable_encoder
from fastapi import Depends
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....repository.template import (
    db_get_templates,
    db_create_template,
    db_get_template_by_id,
    db_update_template_by_id,
    db_delete_template_by_id
)
from app.models.template import (
    TemplateCreate,
    TemplateUpdate
)

async def cont_get_templates(db: AsyncIOMotorClient = Depends(get_database)):
    templates = await db_get_templates(db)
    return templates

async def cont_get_template_by_id(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    template = await db_get_template_by_id(id, db)
    return template

async def cont_create_template(template: TemplateCreate, db: AsyncIOMotorClient = Depends(get_database)):
    template = jsonable_encoder(template)
    template = await db_create_template(template, db)
    return template

async def cont_update_template_by_id(id: str, request: TemplateUpdate, db: AsyncIOMotorClient = Depends(get_database)):
    
    ''' python 
    # Set line filters out key-value pairs from the dictionary 
    # returned by 'request.model_dump()' where the value (v) is not None.
    # This action is to make sure that changes are only applied to changed fields of the data.
    '''
    request = {k: v for k, v in request.model_dump().items() if v is not None}
    
    update = await db_update_template_by_id(id, request, db)
    return update

async def cont_delete_template_by_id(id: str, db: AsyncIOMotorClient = Depends(get_database)):
    delete = await db_delete_template_by_id(id, db)
    return delete