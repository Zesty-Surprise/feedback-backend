from fastapi import APIRouter

from .endpoints.session import router as session_router
from .endpoints.forms import router as form_router
from .endpoints.template import router as template_router
from .endpoints.email import router as test_router

router = APIRouter()
router.include_router(session_router)
router.include_router(form_router)
router.include_router(template_router)
router.include_router(test_router)
