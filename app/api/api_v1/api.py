from fastapi import APIRouter

from .endpoints.session import router as session_router
from .endpoints.forms import router as form_router

router = APIRouter()
router.include_router(session_router)
router.include_router(form_router)

