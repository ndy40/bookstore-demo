from returns.result import Success

from domain.models import Book
from workflows.create_book import create_new_book_workflow, BookSavedEvent


def test_create_book_workflow():
    payload = {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            "last_name": "author-lastname",
            "year_of_birth": "1975-01-01"

        },
        "genre": "pop"
    }

    assert create_new_book_workflow(payload) == Success(BookSavedEvent(book=Book(**payload)))
