from pydantic import BaseModel

class papercount(BaseModel):
    journalname :str
    year1: int
    year2: int
    year3: int
    year4: int
    year5: int
    year6 : int