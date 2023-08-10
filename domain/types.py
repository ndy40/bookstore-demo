from typing import Optional, Tuple

from pydantic import BaseModel

from domain import Author
from domain.models import BookAttributes


class CreateBookRequest(BaseModel):
    title: str
    author: Author
    genre: str
    attributes: Optional[BookAttributes]


class UpdateBookRequest(BaseModel):
    title: Optional[str]
    author: Optional[Author]
    genre: Optional[str]
    attributes: Optional[BookAttributes]


UpdateBookInput = Tuple[int, UpdateBookRequest]