from fastapi import APIRouter,Depends,Response
from JournalData import models,schemas
from User.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
import os
from pathlib import Path
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
@router.post("/update")
async def update(papercount:schemas.papercount,db: Session = Depends(get_db)):
    db_Journal = db.query(models.Journal).filter(models.Journal.journalname == papercount.journalname).first()
    db_Journal.journalname = papercount.journalname
    db_Journal.year1 = papercount.year1
    db_Journal.year2 = papercount.year2
    db_Journal.year3 = papercount.year3
    db_Journal.year4 = papercount.year4
    db_Journal.year5 = papercount.year5
    db_Journal.year6 = papercount.year6
    db.commit()
    return {
        'error': 0,
        'data': 'success'
    }

@router.get("/pdf/{filename}")
async def get_pdf(filename: str):
    # 获取 PDF 文件路径
    pdf_path = "C:/Users/Admin/Desktop/Academic_journal_evaluation/backend/Journalpdf/"+filename+".pdf"
    return FileResponse(pdf_path,media_type='application/pdf')
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
def get_journal_paper_count(db: Session = Depends(get_db)):
    paper_count = db.query(models.Journal).all()
    data= []
    for item in paper_count:
        data.append({'year': 2018, 'value': item.year1,'category':item.journalname})
        data.append({'year': 2019, 'value': item.year2,'category':item.journalname})
        data.append({'year': 2020, 'value': item.year3,'category':item.journalname})
        data.append({'year': 2021, 'value': item.year4,'category':item.journalname})
        data.append({'year': 2022, 'value': item.year5,'category':item.journalname})
        data.append({'year': 2023, 'value': item.year6,'category':item.journalname})
    return data

@router.delete('/delete')
def del_journal_paper_count(journalname:str,db: Session = Depends(get_db)):
    db.query(models.Journal).filter(models.Journal.journalname == journalname).delete(synchronize_session=False)
    db.commit()
    return {"msg": "已经删除"}

@router.get('/test')
def get_test(db: Session = Depends(get_db)):
    data = [
  {
    "item": "Design",
    "user": "a",
    "score": 70
  },
  {
    "item": "Design",
    "user": "b",
    "score": 30
  },
  {
    "item": "Development",
    "user": "a",
    "score": 60
  },
  {
    "item": "Development",
    "user": "b",
    "score": 70
  },
  {
    "item": "Marketing",
    "user": "a",
    "score": 50
  },
  {
    "item": "Marketing",
    "user": "b",
    "score": 60
  },
  {
    "item": "Users",
    "user": "a",
    "score": 40
  },
  {
    "item": "Users",
    "user": "b",
    "score": 50
  },
  {
    "item": "Test",
    "user": "a",
    "score": 60
  },
  {
    "item": "Test",
    "user": "b",
    "score": 70
  },
  {
    "item": "Language",
    "user": "a",
    "score": 70
  },
  {
    "item": "Language",
    "user": "b",
    "score": 50
  },
  {
    "item": "Technology",
    "user": "a",
    "score": 50
  },
  {
    "item": "Technology",
    "user": "b",
    "score": 40
  },
  {
    "item": "Support",
    "user": "a",
    "score": 30
  },
  {
    "item": "Support",
    "user": "b",
    "score": 40
  },
  {
    "item": "Sales",
    "user": "a",
    "score": 60
  },
  {
    "item": "Sales",
    "user": "b",
    "score": 40
  },
  {
    "item": "UX",
    "user": "a",
    "score": 50
  },
  {
    "item": "UX",
    "user": "b",
    "score": 60
  }
]
    return data