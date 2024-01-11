from myapp.config import settings  
from datetime import datetime
from pydantic import BaseModel
from myapp.tables import UserModel

from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, DiscriminatorAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.models import Model

# if not UserModel.exists():
#     UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

# user = list(UserModel.email_index.query("h"))
# print(user)
# # user = User.email_index.query(email, limit=1).next()

class UserByEmailIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = 'email-index' 
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    email = UnicodeAttribute(hash_key=True)

class User(Model):
    class Meta:
        table_name = 'User_Table'
        aws_region = settings.DB_REGION_NAME 
        aws_access_key_id = settings.DB_ACCESS_KEY_ID
        aws_secret_access_key = settings.DB_SECRET_ACCESS_KEY
    
    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    cls = DiscriminatorAttribute()
    email_index = UserByEmailIndex()

class AdminUser(User, discriminator='Admin'):
    access_level = UnicodeAttribute(default='full')

class RegularUser(User, discriminator='Regular'):
    subscription_level = UnicodeAttribute()

if not User.exists():
    User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

# admin = AdminUser(email='admin@example.com', name="example 123")
# regular_user = RegularUser(email='user@example.com', name="Regular 123", subscription_level='premium')

# admin.save()
# regular_user.save()

try:
    # email = "admin@example.com"
    # adminUser = User.email_index.query(email, limit=1).next()
    # print(adminUser.email)
    # print(adminUser.name)
    # print(adminUser.access_level)
    users = list(User.scan())
    for user in users:
        print(user.name)
        print(user.email)
        if user.__class__.__name__ == "AdminUser":
            print(user.access_level)
        else:
            print(user.subscription_level)
except Exception as e:
    print(str(e))




