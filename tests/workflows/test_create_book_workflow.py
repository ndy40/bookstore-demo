from unittest.mock import patch

from returns.result import Success, Failure

from domain.models import Book
from domain.repository import InMemoryRepository
from workflows.create_book import create_new_book_workflow


def test_create_book_workflow_fails_with_invalid_book_payload():
    payload = {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            # missing last_name and year_of_birth
        },
        "genre": "pop"
    }

    assert create_new_book_workflow(payload) == Failure('Missing fields when creating Book')


@patch('infrastructure.db.connect.repository')
def test_create_book_fails_when_book_already_exists(repo):
    repo.side_effect = ValueError('Item already exists')
    payload = {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            "last_name": "author-lastname",
            "year_of_birth": "1975-01-01"
        },
        "genre": "pop"
    }

    assert isinstance(create_new_book_workflow(payload), Success)


def test_create_book_workflow_succeeds(_, book_model):
    payload = {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            "last_name": "author-lastname",
            "year_of_birth": "1975-01-01"
        },
        "genre": "pop"
    }

    assert isinstance(create_new_book_workflow(book_model), Success)


def test_create_book_returns_failure_when_error_happens_while_saving_book(repo, book_model):
    repo.side_effect = Exception('Database error')
    assert isinstance(create_new_book_workflow(book_model).failure(), Exception)
