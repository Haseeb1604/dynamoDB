import pynamodb
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.exceptions import DoesNotExist
from pynamodb.models import Model

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