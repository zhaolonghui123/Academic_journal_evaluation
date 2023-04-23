from pydantic import BaseModel

class journalinfo(BaseModel):
    id : int
    papername : str
    author : str
    publish : str
    journalname : str
    webdownload : int