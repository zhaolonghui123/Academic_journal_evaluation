from fastapi import APIRouter,Depends
from Citation import models,schemas
from User.database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import text


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/get')
def get_journal(db: Session = Depends(get_db)):
    db_journalcitation = db.query(models.journalcitation).all()

    return db_journalcitation
