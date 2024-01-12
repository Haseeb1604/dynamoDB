import boto3
from .tables import Book, User

def create_tables():
    if not Book.exists():
        Book.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    if not User.exists():
        User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

def add_user(user_id, name, email):
    user = User(user_id=user_id, name=name, email=email)
    user.save()

def add_book(book_id, title, author, quantity=1):
    book = Book(book_id=book_id, title=title, author=author, quantity=quantity)
    book.save()