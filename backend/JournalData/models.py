from sqlalchemy import Column, Integer, String
from User.database import Base

class Journal(Base):
    # 表名
    __tablename__ = "all_paper_count"

    # 2、创建模型属性/列，使用Column来表示 SQLAlchemy 中的默认值。
    journalname = Column(String(225), primary_key=True, index=True)
    year1 = Column(Integer)
    year2 = Column(Integer)
    year3 = Column(Integer)
    year4 = Column(Integer)
    year5 = Column(Integer)
    year6 = Column(Integer)

