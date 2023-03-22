from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# 查询多个用户
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session,username:str,password:str):
    # 使用您的数据创建一个 SQLAlchemy 模型实例。
    db_user = models.User(username=username, password=password,isAdmin=0)
    # 使用add来将该实例对象添加到您的数据库。
    db.add(db_user)
    # 使用commit来对数据库的事务提交（以便保存它们）。
    db.commit()
    # 使用refresh来刷新您的数据库实例（以便它包含来自数据库的任何新数据，例如生成的 ID）。
    db.refresh(db_user)
    return db_user
