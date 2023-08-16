from returns.result import Failure, Success

from domain.models import OID
from domain.types import UpdateBookRequest
from workflows import create_new_book_workflow
from workflows.update_book import update_book


def test_update_book_returns_failure_when_book_not_exists(_):
    req = UpdateBookRequest(title='random')
    data = (OID(), req)
    result = update_book(data)
    assert isinstance(result, Failure)


def test_update_book_returns_success_when_updating_book(_, book_model):
    new_book = create_new_book_workflow(book_model).unwrap()

    update_attr = {
        "title": "updated title"
    }

    req = UpdateBookRequest(**update_attr)
    params = (new_book.id, req)
    result = update_book(params)
    assert isinstance(result, Success)
