from fastapi import APIRouter

from .journal import router as journal_router

router = APIRouter()

router.include_router(journal_router, prefix="/journal", tags=["journal"])