from datetime import date
from typing import Optional, Tuple, List, Any

from pydantic import BaseModel


class Author(BaseModel):
    first_name: str
    last_name: str
    year_of_birth: Optional[date]


class Borrower(BaseModel):
    username: str
    email: str


class BookAttributes(BaseModel):
    available_quantity: Optional[int] = 0
    borrowed_by: Optional[List[Borrower]] = None


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


UpdateBookInput = Tuple[str, UpdateBookRequest]
