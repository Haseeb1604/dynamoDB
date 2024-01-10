from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import DoesNotExist
from myapp.config import settings  
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    email: str
    name: str

class UserModel(Model):
    class Meta:
        table_name = 'users'
        awd_region = settings.DB_REGION_NAME 
        aws_access_key_id = settings.DB_ACCESS_KEY_ID
        aws_secret_access_key = settings.DB_SECRET_ACCESS_KEY

    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

user_item = UserModel(email="haseeb123@gmail.com", name="M Haseeb")

user_item.save()

print(UserModel)

for user in UserModel.scan():
    print(user.email, user.name)

