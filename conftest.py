from infrastructure.config import config
from infrastructure.db.connect import book_repository


def pytest_sessionfinish(session, exitstatus):
    book_repository.client.drop_database(name_or_database=config.db_name)
