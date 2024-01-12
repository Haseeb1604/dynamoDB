from tables import Book, User
from methods import *
from pynamodb.transactions import TransactWrite, TransactGet

create_tables()  

add_user(1, "Haseeb", "haseeb@abc.com")
add_user(2, "Osama", "Osama@abc.com")
add_user(3, "Ahmad", "ahmad@abc.com")

add_book(1, "Book 1", "Auther 1")
add_book(2, "Book 2", "Auther 2", quantity=3)
add_book(3, "Book 3", "Auther 3", quantity=2)

