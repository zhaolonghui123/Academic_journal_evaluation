from typing import Union
import logging
import uvicorn
from User.routers import router as user_router
from JournalData.routers import router as Journal_router
from JournalInformation.routers import router as  Journalinformation_router
from Citation.routers import router as Journalcitation_router
from fastapi import FastAPI
import User,JournalData,Citation
from User.database import engine
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger("uvicorn.default")
app = FastAPI(title="Academic_journal_evaluation")
User.models.Base.metadata.create_all(engine)
JournalData.models.Base.metadata.create_all(engine)
app.include_router(user_router,prefix="/api")
app.include_router(Journal_router,prefix="/api")
app.include_router(Journalinformation_router,prefix="/api")
app.include_router(Journalcitation_router,prefix="/api")

origins = [
    "http://localhost:8000",
    "http://localhost:8002",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
    )