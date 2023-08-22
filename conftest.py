import pytest

from infrastructure.config import config
from infrastructure.db.connect import book_repository


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


def pytest_sessionfinish(session, exitstatus):
    book_repository.client.drop_database(name_or_database=config.db_name)