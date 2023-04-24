from fastapi import APIRouter,Depends
from JournalInformation import models,schemas
from User.database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from DataCrawler.Journal import crawl_journal_info
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/update")
async def update(journalinfo: schemas.journalinfo,db: Session = Depends(get_db)):
    db_Journalinfo = db.query(models.Journalinformation).filter(models.Journalinformation.papername == journalinfo.papername).first()
    db_Journalinfo.papername = journalinfo.papername
    db_Journalinfo.journalname = journalinfo.journalname
    db_Journalinfo.author = journalinfo.author
    db_Journalinfo.publish = journalinfo.publish
    db_Journalinfo.webdownload = journalinfo.webdownload
    db.add(db_Journalinfo)
    db.commit()
    return {
        'error': 0,
        'data': 'success'
    }


@router.get("/get")
def get_journalinfo(db: Session = Depends(get_db),page:int = 1,page_size: int = 10):
    skip =(page - 1) * page_size
    query = text("SELECT * FROM Journal_information LIMIT :skip, :limit;")
    result = db.execute(query, {"skip": skip, "limit": page_size + 1})
    Journalinfo = result.fetchall()
    has_more = len(Journalinfo) > page_size
    if has_more:
        Journalinfo = Journalinfo[:page_size]
    data = []
    id = 1
    for item in Journalinfo:
        authors = item.author.split(",")
        data.append({'id': id, 'paperName': item.papername, 'authors': authors, 'journalname': item.journalname,
                     'publishTime': item.publish, 'downloads': item.webdownload})
        id += 1
    #return {"data": data, "has_more": has_more}
    # Journalinfo = db.query(models.Journalinformation).all()
    return data

@router.delete('/delete')
def del_journalinfo(papername:str,db: Session = Depends(get_db)):
    db.query(models.Journalinformation).filter(models.Journalinformation.papername == papername).delete(synchronize_session=False)
    db.commit()
    return {"msg": "已经删除"}

@router.get('/list/get')
def get_journal(db: Session = Depends(get_db)):
    db_Journallist = db.query(models.JournalList).all()
    data = []
    id = 1
    for item in db_Journallist:
        data.append(
            {
                'id':id,
                '期刊名称': item.journalname,
                '主办单位': item.host_unit,
                '主编': item.editor,
                '出版周期': item.period,
                '国际刊号': item.intl_code,
                '国内刊号': item.dom_code,
                '影响因子': item.impact_factor,
                '文献量': item.document_count,
                '被引量': item.cited_count,
                '下载量': item.download_count,
                '基金论文量': item.fund_count,
                '电话': item.telephone,
                '地址': item.address
            }
        )
        id += 1
    return data


@router.get('/list/getjournalnamelist')
def get_journalname_list(db: Session = Depends(get_db)):
    query = text("SELECT journalname FROM Journal")
    result = db.execute(query)
    Journalnamelist = result.fetchall()
    data = []
    for item in Journalnamelist:
        data.append(
            item[0]
        )
    return data


@router.post('/list/create')
def create_journal(journalname:str,db: Session = Depends(get_db)):
    query = text("SELECT journalname FROM Journal")
    result = db.execute(query)
    Journallist = result.fetchall()
    isexist = False
    for item in Journallist:
        if journalname in item[0]:
            isexist = True
    if isexist:
        return {'msg':"期刊已存在"}
    else:
        try:
            crawl_journal_info(journalname)
        except Exception as e:
            return {'msg': '无法获取该期刊'}
        else:
            return {'msg': "添加成功"}


@router.delete('/list/delete')
def del_journal(papername:str,db: Session = Depends(get_db)):
    db.query(models.JournalList).filter(models.JournalList.papername == papername).delete(synchronize_session=False)
    db.commit()
    return {"msg": "已经删除"}

@router.get('/list/refresh')
def refresh_journal(db: Session = Depends(get_db)):
    query = text("SELECT journalname FROM Journal")
    result = db.execute(query)
    Journalnamelist = result.fetchall()
    for item in Journalnamelist:
        crawl_journal_info(item[0])
    return {'msg':"更新完成"}