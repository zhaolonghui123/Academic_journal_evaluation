from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    password: str
    isAdmin: int
    email: Optional[str]
    phone: Optional[str]

default_user = User(
    username="test",
    email="test@sudamath.com",
    phone="",
    password="",
    isAdmin=0
)