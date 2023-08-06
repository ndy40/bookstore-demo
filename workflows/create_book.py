import dataclasses
from typing import Callable, Optional

from pydantic import ValidationError

from returns.pipeline import flow
from returns.maybe import Maybe, Nothing
from returns.pointfree import bind
from returns.result import Result, Failure, Success, safe

from domain.models import Book
from infrastructure.db_context import repository

# Type definitions

CheckBookExistCallable = Callable[[Book], Result[Book, ValueError]]
SaveBookCallable = Callable[[Success[Book]], Result[Book, ValueError]]
ValidateBookCallable = Callable[[Maybe[Book]], Result[Book, ValueError]]


@dataclasses.dataclass
class BookSavedEvent:
    book: Book
    msg: Optional[str] = "Book created"


# Functions
def check_books_exists(book: Book) -> Result[Book, str]:
    return Success(book)


def validate_book(payload: dict) -> Result[Book, str]:
    try:
        return Success(Book(**payload))
    except ValidationError as e:
        return Failure('Missing fields when creating Book')


@safe
def save_book(book: Book) -> BookSavedEvent:
    repository.create(book)
    return BookSavedEvent(book=book)


# Workflow

def create_new_book_workflow(request: dict):
    """
    workflow steps:
    1. Serialize to model
    2. Validate Book
    3. Check if book exists
    4. Save book to db
    5. Send response
    """
    ...
    return flow(
        Success(request),
        bind(validate_book),
        bind(check_books_exists),
        bind(save_book)
    )
