from sqlalchemy import Column, Integer, String
from .database import Base,engine

# User继承Base类
class User(Base):
    # 表名
    __tablename__ = "users"

    # 2、创建模型属性/列，使用Column来表示 SQLAlchemy 中的默认值。
    username = Column(String(225), primary_key=True, index=True)
    isAdmin = Column(Integer)
    phone = Column(String(225))
    email = Column(String(225))
    password = Column(String(225))

