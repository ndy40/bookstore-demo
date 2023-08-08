from typing import List

from returns.result import safe

from domain import Book
from infrastructure.db import schema
from infrastructure.db.connect import repository


@safe
def list_books() -> List[Book]:
    return [Book(**book.dict()) for book in repository.list(schema.Book)]

