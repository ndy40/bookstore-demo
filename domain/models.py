from typing import Optional

from pydantic import BaseModel
from bson.objectid import ObjectId

from domain.types import BookAttributes, Author


class OID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")

        if isinstance(v, str):
            return v

        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class BaseEntity(BaseModel):
    id: Optional[OID] = None

    class Config:
        json_encoders = {ObjectId: lambda oid: str(oid)}


class Publisher(BaseModel):
    name: str


class Book(BaseEntity):
    title: str
    author: Author
    genre: str
    attributes: Optional[BookAttributes] = None
