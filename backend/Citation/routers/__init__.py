from fastapi import APIRouter

from .citation import router as journalcitation_router

router = APIRouter()

router.include_router(journalcitation_router, prefix="/journalcitation", tags=["journal_citation"])