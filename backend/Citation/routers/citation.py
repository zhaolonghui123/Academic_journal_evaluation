from datetime import datetime
from sqlalchemy import and_
from fastapi import APIRouter,Depends
from Citation import models,schemas
from JournalInformation.models import JournalList
from User.database import SessionLocal
from sqlalchemy.orm import Session
from DataCrawler.impact_factor import search_cnki_journal
from DataCrawler.Journalcitation import save_data_to_db
from DataCrawler.doc_count import save_doc_count_db
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
    journals1 = db.query(models.journalcitation).all()
    for journal in journals1:
        if journal.doc_count != 0:
            journal.impact_factor = round(journal.two_years_citation / journal.doc_count, 3)
            db.add(journal)
            db.commit()
    update_impact_factor(db)
    return True

@router.post('/create')
def create(journalname:str,startyear:int):

    #try:
    save_data_to_db(journalname, startyear)
    search_cnki_journal(journalname, startyear)
    save_doc_count_db(journalname, startyear)
    # except Exception:
    #     return {'msg':'False'}
    # else:
    #     return {'msg':'添加成功'}

@router.get('/doc_count')
def get_doc_count(db: Session = Depends(get_db)):
    current_year = datetime.now().year
    data= []
    result = db.query(models.journalcitation.name, models.journalcitation.doc_count, models.journalcitation.year).filter(and_(models.journalcitation.year<current_year,models.journalcitation.year>current_year-6)).all()
    for item in result:
        data.append({'year':item.year,'value':item.doc_count,'category':item.name})
    return data


@router.get('/cited_count')
def get_cited_count(db: Session = Depends(get_db)):
    current_year = datetime.now().year
    data= []
    result = db.query(models.journalcitation.name, models.journalcitation.cite_count, models.journalcitation.year).filter(and_(models.journalcitation.year<current_year,models.journalcitation.year>current_year-6)).all()
    for item in result:
        data.append({'year':item.year,'value':item.cite_count,'category':item.name})
    return data


@router.get('/IF')
def get_impact_factor(db: Session = Depends(get_db)):
    current_year = datetime.now().year
    data= []
    result = db.query(models.journalcitation.name, models.journalcitation.impact_factor, models.journalcitation.year).filter(and_(models.journalcitation.year<current_year,models.journalcitation.year>current_year-6)).all()
    for item in result:
        data.append({'year':item.year,'value':item.impact_factor,'category':item.name})
    return data


@router.get('/avg_cite_count')
def get_avg_cite_count(db: Session = Depends(get_db)):
    current_year = datetime.now().year
    data= []
    result = db.query(models.journalcitation.name, models.journalcitation.avg_cite_count, models.journalcitation.year).filter(and_(models.journalcitation.year<current_year,models.journalcitation.year>current_year-6)).all()
    for item in result:
        data.append({'year':item.year,'value':item.avg_cite_count,'category':item.name})
    return data


@router.get('/two_years_citation')
def get_two_years_citation(db: Session = Depends(get_db)):
    current_year = datetime.now().year
    data= []
    result = db.query(models.journalcitation.name, models.journalcitation.two_years_citation, models.journalcitation.year).filter(and_(models.journalcitation.year<current_year,models.journalcitation.year>current_year-6)).all()
    for item in result:
        data.append({'year':item.year,'value':item.two_years_citation,'category':item.name})
    return data


def update_impact_factor(db: Session = Depends(get_db)):
    # 创建数据库会话

    current_year = datetime.now().year
    last_year = current_year - 1
    # 获取当前年份前一年的期刊影响因子
    journals = db.query(models.journalcitation.name, models.journalcitation.impact_factor) \
        .filter(and_(models.journalcitation.year == last_year, models.journalcitation.impact_factor != None))

    # 根据期刊名称更新表二中对应期刊的影响因子
    for journal in journals:
        db.query(JournalList).filter_by(journalname=journal[0]).update({"impact_factor": journal[1]})
    db.commit()
