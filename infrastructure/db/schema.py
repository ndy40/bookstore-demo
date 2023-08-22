from datetime import date
from typing import Optional

from bunnet import Document
from pydantic import BaseModel

from domain.types import BookAttributes


class Author(BaseModel):
    first_name: str
    last_name: str
    year_of_birth: Optional[date]


class Book(Document):
    title: str
    author: Author
    genre: str
    attributes: Optional[BookAttributes] = None

    class Settings:
        name = "books"
        bson_encoders = {
            date: lambda dt: dt.isoformat()
        }
