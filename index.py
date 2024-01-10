from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import DoesNotExist
from app.config import settings  
from datetime import datetime

class UserModel(Model):
    class Meta:
        table_name = 'user'
        awd_region = settings.DB_REGION_NAME 
        aws_access_key_id = settings.DB_ACCESS_KEY_ID
        aws_secret_access_key = settings.DB_SECRET_ACCESS_KEY

    email = UnicodeAttribute(hash_key=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()

# if not UserModel.exists():
#         UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

# user_item = UserModel(email="haseeb@gmail.com", first_name="Muhammad", last_name="Haseeb")

# print(user_item)

# user_item.save()


print(UserModel.exists())