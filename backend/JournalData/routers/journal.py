from fastapi import APIRouter,Depends
from JournalData import models,schemas
from User.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
def create_paper_count(papercount: schemas.papercount, db: Session = Depends(get_db)):
    db_Journal = models.Journal()
    db_Journal.journalname = papercount.journalname
    db_Journal.year1 = papercount.year1
    db_Journal.year2 = papercount.year2
    db_Journal.year3 = papercount.year3
    db_Journal.year4 = papercount.year4
    db_Journal.year5 = papercount.year5
    db_Journal.year6 = papercount.year6

    db.add(db_Journal)
    db.commit()
    db.refresh(db_Journal)
    return {
        'error': 0,
        'data': 'success'
    }
@router.get("/get_one")
def get_journal_paper_count(journalname:str,db: Session = Depends(get_db)):
    paper_count = db.query(models.Journal).filter(models.Journal.journalname == journalname).first()
    data = []
    data.append({'year': 2018,'value': paper_count.year1})
    data.append({'year':2019,'value':paper_count.year2})
    data.append({'year':2020,'value':paper_count.year3})
    data.append({'year':2021,'value':paper_count.year4})
    data.append({'year':2022,'value':paper_count.year5})
    data.append({'year':2023,'value':paper_count.year6})
    return data

@router.get("/get")
def get_user(db: Session = Depends(get_db)):
    users = db.query(models.Journal).all()
    return users

@router.delete('/delete')
def del_user(journalname:str,db: Session = Depends(get_db)):
    db.query(models.Journal).filter(models.Journal.journalname == journalname).delete(synchronize_session=False)
    db.commit()
    return {"msg": "已经删除"}