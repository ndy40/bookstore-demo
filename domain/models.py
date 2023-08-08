from datetime import date
from typing import Optional, List

from pydantic import BaseModel
from bson.objectid import ObjectId as BsonObjectId


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)

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
    available_quantity: int
    borrowed_by: Optional[List[Borrower]]


class Book(BaseModel):
    title: str
    author: Author
    genre: str
    id: Optional[PydanticObjectId] = None

    class Config:
        json_encoders = {
            PydanticObjectId: lambda v: str(v),
        }
