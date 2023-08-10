from datetime import date
from typing import Optional, List

from pydantic import BaseModel
from bson.objectid import ObjectId


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


class Author(BaseModel):
    first_name: str
    last_name: str
    year_of_birth: Optional[date]


class Publisher(BaseModel):
    name: str


class Borrower(BaseModel):
    username: str
    email: str


class BookAttributes(BaseModel):
    available_quantity: Optional[int] = 0
    borrowed_by: Optional[List[Borrower]]


class Book(BaseEntity):
    title: str
    author: Author
    genre: str
    attributes: Optional[BookAttributes] = None
