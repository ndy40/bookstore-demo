from bunnet import init_bunnet
from pymongo import MongoClient

from domain.repository import MongoBooksRepository
from infrastructure.config import config
from infrastructure.db.schema import Book

client = MongoClient(config.MONGODB_URL)
init_bunnet(database=getattr(client, config.db_name), document_models=[Book])

book_repository = MongoBooksRepository(client)
