import pytest

from domain.models import Book
from infrastructure.db.connect import repository


@pytest.fixture
def book_model():
    return {
        "title": "We go be",
        "author": {
            "first_name": "author 1",
            "last_name": "author-lastname",
            "year_of_birth": "1975-01-01"
        },
        "genre": "pop"
    }


@pytest.fixture(scope="function", autouse=True)
def reset_repository():
    repository.clear()
