import boto3
from tables import Book, User

def add_user(user_id:int, name:str, email:str):
    user = User(user_id=user_id, name=name, email=email)
    user.save()

def add_book(book_id:int, title:str, author:str, quantity:int=1):
    book = Book(book_id=book_id, title=title, author=author, quantity=quantity)
    book.save()