from datetime import date
from typing import Optional, List

from pydantic import BaseModel


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
