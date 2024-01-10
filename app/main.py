from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from uuid import UUID

from app.tables import UserModel
from app import schemas

from .config import settings

app = FastAPI()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    # status_code=status.HTTP_201_CREATED,
    # response_model=schemas.User,
)
def create():
    users = UserModel.get()
    print(users)
    return users

