import abc
from abc import ABC
from typing import List, Any, Protocol

from bson import ObjectId
from bunnet import Document
from bunnet.odm.queries.find import FindMany

from domain import models
from domain.models import OID
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
            obj.id = OID(ObjectId())
            self.items.append(obj)
            return obj

        raise ValueError('Item already exists')

    def find_by_id(self, model, obj_id: str) -> None | object:
        for item in self.items:
            if item.id == obj_id:
                return model(**item.dict())

    def update(self, model, attr) -> None:
        ...


class MongoDbRepository(BaseRepository, ABC):
    model = Document

    def __init__(self, client):
        self.client = client

    def create(self, obj: models.Book) -> Document:
        book = self.model(**obj.dict())
        return book.insert()

    def list(self) -> FindMany:
        return self.model.find()

    @property
    def items(self):
        return self.model.all()

    def find_by_id(self, model, obj_id: str) -> None | Document:
        ...


class MongoBooksRepo(MongoDbRepository):
    model = schema.Book