from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model
import uuid
from .config import settings
from datetime import datetime

class UserByEmailIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'email-index' 
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    email = UnicodeAttribute(hash_key=True)

class UserModel(Model):
    class Meta:
        table_name = 'Users'
        aws_region = settings.DB_REGION_NAME 
        aws_access_key_id = settings.DB_ACCESS_KEY_ID
        aws_secret_access_key = settings.DB_SECRET_ACCESS_KEY
        read_capacity_units = 1  
        write_capacity_units = 1 

    id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    creation_date = UTCDateTimeAttribute(default=datetime.now)

    email_index = UserByEmailIndex()

    def save(self, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4())
        super().save(**kwargs)