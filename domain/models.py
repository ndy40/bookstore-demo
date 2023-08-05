from datetime import datetime
from typing import Optional, List


class Author:
    first_name: str
    last_name: str
    year_of_birth: Optional[datetime]


class Publisher:
    name: str


class Borrower:
    username: str
    email: str


class BookAttributes:
    available_quantity: int
    borrowed_by: Optional[List[Borrower]]


class Book:
    title: str
    isbn: str
    published_on: datetime
    author: Author
    genre: str
    publisher: Publisher
    status: BookAttributes
