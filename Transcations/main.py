from tables import Book, User
from methods import *
from pynamodb.transactions import TransactWrite, TransactGet

# if not Book.exists():
#     Book.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
# if not User.exists():
#     User.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

# users = [
#     User(user_id = 1, name="Haseeb", email="haseeb@abc.com"),
#     User(user_id = 2, name="Osama", email="124@abc.com"),
#     User(user_id = 3, name="Ahmad", email="abc1@abc.com"),
# ]

# books = [
#     Book(book_id = 1, title="Book 1", author="Auther 1"),
#     Book(book_id = 2, title="Book 2", author="Auther 2", quantity=2),
#     Book(book_id = 3, title="Book 3", author="Auther 3", quantity=3),
# ]

# with User.batch_write() as batch:
#     for user in users:
#         batch.save(user)

# with Book.batch_write() as batch:
#     for book in books:
#         batch.save(book)


for item in User.batch_get([1, 2, 3]):
    print(item)