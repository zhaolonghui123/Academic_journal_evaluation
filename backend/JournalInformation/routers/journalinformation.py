from fastapi import APIRouter,Depends
from JournalInformation import models,schemas
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