import dataclasses
from typing import Callable, Optional

from pydantic import ValidationError

from returns.pipeline import flow
from returns.maybe import Maybe
from returns.pointfree import bind
from returns.result import Result, Failure, Success, safe

from domain.models import Book

# Type definitions

CheckBookExistCallable = Callable[[Book], Result[Book, ValueError]]
SaveBookCallable = Callable[[Success[Book]], Result[Book, ValueError]]
ValidateBookCallable = Callable[[Maybe[Book]], Result[Book, ValueError]]


@dataclasses.dataclass
class BookSavedEvent:
    book: Book
    msg: Optional[str] = "Book created"


# Functions
def check_books_exists(book: Book) -> Result[Book, ValueError]:
    return Success(book)


@safe
def validate_book(payload: dict) -> Book:
    return Book(**payload)

@safe
def save_book(book: Book):
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
