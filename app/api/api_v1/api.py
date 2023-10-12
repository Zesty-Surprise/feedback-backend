from fastapi import APIRouter

from .endpoints.session import router as session_router

router = APIRouter()
router.include_router(session_router)

