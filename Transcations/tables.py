from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from config import settings
from typing import Optional

class Book(Model):
    class Meta:
        table_name = 'LibraryBooks'
        region = settings.DB_REGION_NAME

    book_id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(required=True)
    author = UnicodeAttribute(required=True)
    quantity = NumberAttribute(default=0)
    borrowed_by = Optional[UnicodeAttribute]

class User(Model):
    class Meta:
        table_name = 'LibraryUsers'
        region = settings.DB_REGION_NAME

    user_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(required=True)
    email = UnicodeAttribute(required=True)
    books_borrowed = Optional[UnicodeAttribute]