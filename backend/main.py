from typing import Union
import logging
import uvicorn
import hashlib
from fastapi import FastAPI,Depends
from User import models,schemas,crud
from User.database import SessionLocal,engine
from typing import Optional
logger = logging.getLogger("uvicorn.default")
app = FastAPI(title="Academic_journal_evaluation")
from sqlalchemy.orm import Session
models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/sign_in')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = models.User()
    db_user.password = hashlib.new('md5', user.password.encode()).hexdigest()
    db_user.username = user.username
    db_user.isAdmin = user.isAdmin
    db_user.email = db_user.email
    db_user.phone = db_user.phone
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        'error': 0,
        'data': 'success'
    }
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="127.0.0.1",
        port=8080,
    )