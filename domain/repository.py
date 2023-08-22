import abc
from abc import ABC
from typing import List, Any, Protocol, Dict

from bson import ObjectId
from bunnet import Document
from bunnet.odm.queries.find import FindMany, FindOne
from pymongo import MongoClient

from domain import models
from domain.models import OID
from infrastructure.db import schema


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def create(self, obj):
        ...


class MongoDbRepository(BaseRepository, ABC):
    model = Document

    def __init__(self, client: MongoClient):
        self.client = client

    def create(self, obj) -> Document:
        book = self.model(**obj.dict())
        return book.insert()

    def list(self, search_criteria: Dict = None) -> FindMany:
        if search_criteria:
            return self.model.find(**search_criteria)

        return self.model.find()

    def first(self, search_criteria: Dict):
        return self.model.find_one(**search_criteria)

    @property
    def items(self):
        return self.model.all()

    def find_by_id(self, obj_id: ObjectId | Any) -> Document | None:
        return self.model.find_one(self.model.id == obj_id).run()

    def update(self, obj):
        doc = self.find_by_id(obj_id=obj.id)
        doc.set(obj.dict())


class MongoBooksRepository(MongoDbRepository):
    model = schema.Book
