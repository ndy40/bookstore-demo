from functools import partial
from typing import Dict

from returns import pointfree
from returns._internal.pipeline.flow import flow
from returns.curry import curry
from returns.io import IO
from returns.pointfree import bind, apply
from returns.result import safe, Result, Success, Failure

from domain import Book
from domain.types import UpdateBookInput
from infrastructure.db.connect import book_repository


def get_book(book_param: UpdateBookInput) -> Result[Book, str]:
    obj_id, _ = book_param

    find_obj = book_repository.find_by_id(obj_id=obj_id)

    if find_obj:
        return Success(find_obj)

    return Failure('Book not found')


@curry
@safe
def update_book_attr(book: Book, attr: Dict) -> Book:
    for key, value in attr.items():
        if value:
            setattr(book, key, value)
    return book

@safe
def save_book(obj):
    book_repository.update(obj)
    return Success(obj)


def update_book(book_update: UpdateBookInput) -> Book:
    update_attr_partial = update_book_attr(attr=book_update[1].dict())

    return flow(
        book_update,
        get_book,
        bind(update_attr_partial),
        bind(save_book)
    )
