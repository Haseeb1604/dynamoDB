from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    email: EmailStr
    name: str

class UserOut(User):
    id: str
    creation_date: datetime