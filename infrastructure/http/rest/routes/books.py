from typing import List, Optional

from fastapi import FastAPI, APIRouter, Response

import workflows.create_book
from domain import Book
from domain.types import CreateBookRequest, UpdateBookRequest, UpdateBookInput
from domain.utils import handle_response

book_route = APIRouter(prefix='/books')


@book_route.post("/")
def create_book(book: CreateBookRequest) -> Book:
    resp = workflows.create_new_book_workflow(book.dict())
    return handle_response(resp)


@book_route.get('/')
def list_books() -> List[Book]:
    result = workflows.list_books()
    return handle_response(result)


@book_route.patch('/{id}', name='Update book fields')
def update_book(id: int, book: UpdateBookRequest) -> Optional[Book]:
    return workflows.update_book(UpdateBookInput(id, book))


@book_route.put('/{id}', name="Replace book with new attributes")
def replace_book(book: CreateBookRequest) -> Optional[Book]:
    """
    If you need to replace the entire book object with updated values.
    """
    ...
