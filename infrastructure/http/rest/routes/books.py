from typing import List, Optional

from fastapi import APIRouter

import workflows.create_book
from domain import Book
from domain.types import CreateBookRequest, UpdateBookRequest, UpdateBookInput
from domain.utils import handle_response

book_route = APIRouter(prefix="/books", tags=["books"])


@book_route.post("/")
def create_book(book: CreateBookRequest) -> Book:
    resp = workflows.create_new_book_workflow(book.dict())
    return handle_response(resp)


@book_route.get("/")
def list_books() -> List[Book]:
    result = workflows.list_books()
    return handle_response(result)


@book_route.patch("/{id}", name="Update book fields")
def update_book(id: str, book: UpdateBookRequest) -> Optional[Book]:
    return handle_response(workflows.update_book(UpdateBookInput(id, book)))


@book_route.get("/{id}", name="Get book")
def get_book(id: str) -> Optional[Book]:
    return handle_response(workflows.fetch_book(id))


@book_route.delete("/{id}")
def delete_book(id: str) -> None:
    ...


@book_route.post("/{id}/borrow-book")
def borrow_book(id: str):
    ...


@book_route.post("/{id}/return-book")
def borrow_book(id: str):
    ...
