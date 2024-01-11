from fastapi import FastAPI, status, HTTPException

from typing import List

from .tables import UserModel
from .routes import users

app = FastAPI()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

app.include_router(users.router)