import hashlib

from fastapi import APIRouter,Depends
from User import models,schemas
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
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = models.User()
    db_user.password = hashlib.new('md5', user.password.encode()).hexdigest()
    db_user.username = user.username
    db_user.isAdmin = user.isAdmin
    db_user.email = user.email
    db_user.phone = user.phone
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {
        'error': 0,
        'data': 'success'
    }
@router.get("/get")
def get_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.delete('/delete')
def del_user(usename:str,db: Session = Depends(get_db)):
    db.query(models.User).filter(models.User.username == usename).delete(synchronize_session=False)
    db.commit()
    return {"msg": "已经删除"}