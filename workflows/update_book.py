from returns._internal.pipeline.flow import flow
from returns.maybe import Maybe
from returns.result import safe, Result, Success

from domain import Book
from domain.types import UpdateBookInput
from infrastructure.db.connect import repository


def get_book(book_param) -> Maybe[Book]:
    id, _ = book_param
    return Success(id).map(repository.find_by_id)



@safe
def update_book(book_update: UpdateBookInput) -> Book:
    # get book. If none, return Failure(Nothing)
    # update book, could raise validation error
    # save to db
    # return book
    ...