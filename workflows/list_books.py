from typing import Set, Any, List

from returns.result import safe, Result

from domain import Book
from domain.repository import MongoBooksRepository
from infrastructure.db.connect import client

book_repository = MongoBooksRepository(client)


@safe
def _fetch_all_books() -> List[Book]:
    return [
        Book(**book.dict()) for book in book_repository.list()
    ]


def list_books() -> Result[List[Book], Any]:
    return _fetch_all_books()
