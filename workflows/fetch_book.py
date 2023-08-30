from typing import Any

import pymongo.errors
from returns._internal.pipeline.flow import flow
from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure

from domain.models import OID, Book
from infrastructure.db import schema
from infrastructure.db.connect import book_repository


def get_book_by_id(id: OID) -> Result[Book, Any]:
    try:
        result = book_repository.find_by_id(id)
    except pymongo.errors.PyMongoError:
        return Failure("Error fetching book")

    match result:
        case schema.Book() as x:
            return Success(Book(**x.dict()))
        case _:
            return Failure(Nothing)


def fetch_book(id: str) -> Result[Maybe[Book], str]:
    return flow(
        OID(id),
        get_book_by_id,
    )
