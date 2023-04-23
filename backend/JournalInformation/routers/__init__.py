from fastapi import APIRouter

from .journalinformation import router as journalinformation_router

router = APIRouter()

router.include_router(journalinformation_router, prefix="/journalinformation", tags=["journal_information"])