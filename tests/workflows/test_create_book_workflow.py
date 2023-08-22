from unittest.mock import patch

from returns.result import Success, Failure

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

@patch('workflows.create_book.check_books_exists')
def test_create_book_fails_when_book_already_exists(func_book_exists):
    func_book_exists.return_value = Failure("Item already exists")
    payload = {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            "last_name": "author-lastname",
            "year_of_birth": "1975-01-01"
        },
        "genre": "pop"
    }

    assert isinstance(create_new_book_workflow(payload), Failure)


def test_create_book_workflow_succeeds(book_model):
    assert isinstance(create_new_book_workflow(book_model), Success)


@patch('workflows.create_book.book_repository')
def test_create_book_returns_failure_when_error_happens_while_saving_book(repository, book_model):
    repository.side_effect = ValueError('Database error')
    assert isinstance(create_new_book_workflow(book_model), Failure)
