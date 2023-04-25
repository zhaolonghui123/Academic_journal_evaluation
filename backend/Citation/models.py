from sqlalchemy import Column, Integer, String, Float
from User.database import Base

class journalcitation(Base):
    # 表名
    __tablename__ = "journal_citation"

    # 2、创建模型属性/列，使用Column来表示 SQLAlchemy 中的默认值。
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(250))
    year = Column(Integer)
    doc_count = Column(Integer)
    cite_count = Column(Integer)
    avg_cite_count = Column(Float)
    two_years_citation = Column(Integer)
    impact_factor = Column(Float)
    H_index = Column(Float)
