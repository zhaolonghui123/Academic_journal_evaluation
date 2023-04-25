from fastapi import APIRouter,Depends
from Citation import models,schemas
from User.database import SessionLocal
from sqlalchemy.orm import Session
from DataCrawler.impact_factor import search_cnki_journal
from DataCrawler.Journalcitation import save_data_to_db
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


@router.get('/initIF')
def update_impact_factor(db: Session = Depends(get_db)):
    journals = db.query(models.journalcitation).all()

    for journal in journals:
        if journal.doc_count != 0:
            journal.impact_factor = round(journal.two_years_citation / journal.doc_count, 3)
            db.add(journal)
            db.commit()
    return True

@router.post('/create')
def create(journalname:str,startyear:int):
    try:
        save_data_to_db(journalname,startyear)
        search_cnki_journal(journalname,startyear)
    except Exception:
        return {'msg':'False'}
    else:
        return {'msg':'添加成功'}