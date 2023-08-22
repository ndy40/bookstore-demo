from typing import List

from returns.result import safe

from domain import Book
from infrastructure.db import schema
from infrastructure.db.connect import book_repository


@safe
def list_books() -> List[Book]:
    return [Book(**book.dict()) for book in book_repository.list(schema.Book)]

