from fastapi import FastAPI, status, HTTPException
from uuid import UUID

from typing import List

from .schema import User
from .tables import UserModel


app = FastAPI()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

@app.post( "/users/", status_code=status.HTTP_201_CREATED)
def create(user: User):
    if UserModel.get(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User with this email already exists"
            )

    user_item = UserModel(**user.dict())
    user_item.save()
    
    return user_item

@app.get("/users/", response_model=List[User])
def get_users():
    try:
        users = list(UserModel.scan())
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
