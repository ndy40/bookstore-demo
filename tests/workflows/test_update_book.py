from returns.result import Failure, Success

from domain import Book
from domain.types import UpdateBookRequest, UpdateBookInput
from infrastructure.db.connect import repository
from workflows import create_new_book_workflow
from workflows.update_book import update_book


def test_update_book_returns_failure_when_book_not_exists():
    req = UpdateBookRequest(title='random')
    data = (100, req)
    result = update_book(data)
    assert isinstance(result, Failure)


def test_update_book_returns_success_when_updating_book(book_model):
    create_new_book_workflow(book_model)

    update_attr = {
        "title": "updated title"
    }

    req = UpdateBookRequest(**update_attr)

    params = (repository.items[0].id, req)
    result = update_book(params)
    assert isinstance(result, Success)
