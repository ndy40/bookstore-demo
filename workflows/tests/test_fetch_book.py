from unittest.mock import patch

from returns.result import Failure, Success

from domain.models import OID
from domain.types import CreateBookRequest
from workflows import create_new_book_workflow, fetch_book


def test_fetch_book_returns_nothing_if_book_not_found():
    new_id_not_exists = OID()
    result = fetch_book(new_id_not_exists)
    assert isinstance(result, Failure)


@patch("workflows.fetch_book.book_repository")
def test_nothing_returned_on_db_error(repo):
    repo.side_effect = Exception("DB Error")
    new_id = OID()
    result = fetch_book(new_id)
    assert isinstance(result, Failure)


def test_success_returned_when_book_found(book_model):
    request = CreateBookRequest(**book_model)
    book = create_new_book_workflow(request.dict())
    result = fetch_book(book.unwrap().id)
    assert isinstance(result, Success)
