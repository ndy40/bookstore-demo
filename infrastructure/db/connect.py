import os

from bunnet import init_bunnet
from pymongo import MongoClient

from domain.repository import InMemoryRepository, MongoDbRepository, BaseRepository
from infrastructure.config import config
from infrastructure.db.schema import Book


def get_mongodb_repo() -> BaseRepository:
    client = MongoClient(config.MONGODB_URL)
    init_bunnet(database=client.bookstore, document_models=[Book])
    return MongoDbRepository(client)


repository = (
    InMemoryRepository()
    if os.environ.get('APP_ENV') == 'test' else get_mongodb_repo()
)
