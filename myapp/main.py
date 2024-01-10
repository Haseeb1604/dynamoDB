from fastapi import FastAPI, status
from uuid import UUID
from pydantic import BaseModel

from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import DoesNotExist
from pynamodb.models import Model

from .config import settings  
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserModel(Model):
    class Meta:
        table_name = 'user'
        awd_region = settings.DB_REGION_NAME 
        aws_access_key_id = settings.DB_ACCESS_KEY_ID
        aws_secret_access_key = settings.DB_SECRET_ACCESS_KEY

    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

@app.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.User,
)
def create(user: schemas.User):
    user_create = UserModel.create(user)
    print(user_create)
    user_create.save()
    return user_create

@app.get(
    "/users/",
)
def create():
    users = UserModel.get()
    print(users)
    return users

