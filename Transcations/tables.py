import boto3
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, SetAttribute, OptionalAttribute
from pynamodb.transactions import TransactWrite, TransactGet
from myapp.config import settings

class Book(Model):
    class Meta:
        table_name = 'LibraryBooks'
        region = settings.DB_REGION_NAME

    book_id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(required=True)
    author = UnicodeAttribute(required=True)
    quantity = NumberAttribute(default=0)
    borrowed_by = OptionalAttribute(UnicodeAttribute())

class User(Model):
    class Meta:
        table_name = 'LibraryUsers'
        region = settings.DB_REGION_NAME

    user_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(required=True)
    email = UnicodeAttribute(required=True)
    books_borrowed = SetAttribute(attribute_type=UnicodeAttribute())