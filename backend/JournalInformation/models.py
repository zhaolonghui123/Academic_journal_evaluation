from sqlalchemy import Column, Integer, String
from User.database import Base

class Journalinformation(Base):
    # 表名
    __tablename__ = "Journal_information"

    # 2、创建模型属性/列，使用Column来表示 SQLAlchemy 中的默认值。
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    papername = Column(String(250), index=True)
    author = Column(String(250))
    publish = Column(String(250))
    journalname = Column(String(250))
    webdownload = Column(Integer)
