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

class JournalList(Base):
    # 表名
    __tablename__ = "Journal"

    # 2、创建模型属性/列，使用Column来表示 SQLAlchemy 中的默认值。
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    journalname = Column(String(250))
    host_unit = Column(String(250))
    editor = Column(String(250))
    period = Column(String(250))
    intl_code = Column(String(250))
    dom_code = Column(String(250))
    impact_factor = Column(String(250))
    document_count = Column(String(250))
    cited_count = Column(String(250))
    download_count = Column(String(250))
    fund_count = Column(String(250))
    telephone = Column(String(250))
    address = Column(String(250))
