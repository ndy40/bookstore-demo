import os

from bunnet import init_bunnet
from pymongo import MongoClient

from domain.repository import MongoDbRepository, BaseRepository, MongoBooksRepo
from infrastructure.config import config
from infrastructure.db.schema import Book


def get_mongodb_repo() -> BaseRepository:
    client = MongoClient(config.MONGODB_URL)
    init_bunnet(database=getattr(client, config.db_name), document_models=[Book])
    return MongoBooksRepo(client)


book_repository = get_mongodb_repo()
