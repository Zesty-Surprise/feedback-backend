from ..db.mongodb import AsyncIOMotorClient
from ..models.template import Template, TemplateCreate, TemplateUpdate
from ..core.config import database_name, template_collection_name

from typing import List
from bson import ObjectId

async def db_get_templates(db: AsyncIOMotorClient) -> List[Template]:
    templates : List[Template] = []
    templates_docs = db[database_name][template_collection_name].find()
    async for session in templates_docs:
        templates.append(Template(**session))
    return templates

async def db_create_template(template: TemplateCreate, db):
    new_template = await db[database_name][template_collection_name].insert_one(template)
    return await db[database_name][template_collection_name].find_one({"_id": new_template.inserted_id})

async def db_get_template_by_id(id:str, db: AsyncIOMotorClient)->Template:
    template : Template = await db[database_name][template_collection_name].find_one({"_id": ObjectId(id)})
    return template

async def db_update_template_by_id(id:str, request, db:AsyncIOMotorClient):
    update = await db[database_name][template_collection_name].update_one({"_id": ObjectId(id)}, {"$set": request})
    if update:
        return True
    return False

async def db_delete_template_by_id(id: str, db:AsyncIOMotorClient) -> bool:
    delete = await db[database_name][template_collection_name].delete_one({"_id": ObjectId(id)})
    if delete.deleted_count:
        return True
    return False