from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Dict, Any, Union
from .. import schema, tables
from ..tables import UserModel
from pynamodb.exceptions import DoesNotExist 
from uuid import UUID

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post( "/", status_code=status.HTTP_201_CREATED, response_model=schema.User)
def create(user: schema.User):
  user_al =UserModel.email_index.query(user.email)
  if any(user_al):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="User with this email already exists"
    )
  else:
    user_item = UserModel(**user.dict())
    user_item.save()
    return user_item

@router.get("/", response_model=List[schema.UserOut])
def get_users():
    try:
        users = list(UserModel.scan())
        return users
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/{email}", response_model=schema.UserOut)
def get_user_by_email(email: str):
  try:
    user = list(UserModel.email_index.query(email))[0]
    return user
  except DoesNotExist:
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_email}", response_model=schema.UserOut)
def update_user(user_email: str, user_data: schema.User):
  try:
    user = list(UserModel.email_index.query(user_email))[0]

    user.update(
      actions=[
          UserModel.name.set(user_data.name)
      ]
    )

    return user
  except DoesNotExist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email address {user_email} Not found"
    )

@router.delete("/{user_email}")
def delete_user(user_email: str):
  try:
    user = list(UserModel.email_index.query(user_email))[0]
    user.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
  except DoesNotExist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email address {user_email} Not found"
    )

