import abc
from abc import ABC
from typing import List, Any

from bunnet import Document
from bunnet.odm.queries.find import FindMany

from domain import models
from infrastructure.db import schema


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, obj):
        ...


class InMemoryRepository(BaseRepository, ABC):
    items: List[Any] = []

    def clear(self):
        self.items = []

    def create(self, obj) -> None:
        if obj not in self.items:
            self.items.append(obj)
            return obj.dict()

        raise ValueError('Item already exists')


class MongoDbRepository(BaseRepository, ABC):
    def __init__(self, client):
        self.client = client

    def create(self, obj: models.Book) -> Document:
        book = schema.Book(**obj.dict())
        return book.insert()

    def list(self, model: Document) -> FindMany:
        return model.find()
