from typing import Union
import logging
import uvicorn
from User.routers import router as user_router
from fastapi import FastAPI,Depends
from User import models
from User.database import engine
logger = logging.getLogger("uvicorn.default")
app = FastAPI(title="Academic_journal_evaluation")
models.Base.metadata.create_all(engine)
app.include_router(user_router,prefix="/api")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
    )