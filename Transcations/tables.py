from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()  

class Book(Model):
    class Meta:
        table_name = 'LibraryBooks'
        aws_region = os.environ.get("DB_REGION_NAME") 
        aws_access_key_id = os.environ.get("DB_ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("DB_SECRET_ACCESS_KEY")

    book_id = NumberAttribute(hash_key=True)
    title = UnicodeAttribute(null=False)
    author = UnicodeAttribute(null=False)
    quantity = NumberAttribute(default=0)
    borrowed_by = Optional[NumberAttribute]

class User(Model):
    class Meta:
        table_name = 'LibraryUsers'
        aws_region = os.environ.get("DB_REGION_NAME") 
        aws_access_key_id = os.environ.get("DB_ACCESS_KEY_ID")
        aws_secret_access_key = os.environ.get("DB_SECRET_ACCESS_KEY")

    user_id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    books_borrowed = Optional[NumberAttribute]