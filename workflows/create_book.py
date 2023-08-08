import dataclasses
from typing import Callable, Optional, Any

from pydantic import ValidationError

from returns.pipeline import flow
from returns.maybe import Maybe
from returns.pointfree import bind
from returns.result import Result, Failure, Success, safe

from domain.models import Book
from infrastructure.db.connect import repository

# Type definitions

CheckBookExistCallable = Callable[[Book], Result[Book, ValueError]]
SaveBookCallable = Callable[[Success[Book]], Result[Book, ValueError]]
ValidateBookCallable = Callable[[Maybe[Book]], Result[Book, ValueError]]


# Functions
def check_books_exists(book: Book) -> Result[Book, str]:
    return Success(book)


def validate_book(payload: dict) -> Result[Book, str]:
    try:
        return Success(Book(**payload))
    except ValidationError as e:
        return Failure('Missing fields when creating Book')


@safe
def save_book(book: Book) -> Book:
    doc = repository.create(book)
    return Book(**doc.dict())


# Workflow

def create_new_book_workflow(request: dict) -> Result[Book, Any]:
    return flow(
        Success(request),
        bind(validate_book),
        bind(check_books_exists),
        bind(save_book)
    )
