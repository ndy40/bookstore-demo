from typing import Union
from unittest.mock import patch

import pytest
from _pytest.config import ExitCode
from _pytest.main import Session

from domain.models import Book
from domain.repository import InMemoryRepository, MongoBooksRepo
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


def pytest_sessionfinish(session: Session, exitstatus: Union[int, ExitCode]):
    MongoBooksRepo().model.delete()
