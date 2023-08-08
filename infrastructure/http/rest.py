from typing import List

from fastapi import FastAPI, APIRouter

import workflows.create_book
from domain import Book
from domain.utils import handle_response

book_route = APIRouter(prefix='/books')


@book_route.post("/")
def create_book(book: Book) -> Book:
    resp = workflows.create_new_book_workflow(book.dict())
    return handle_response(resp)


@book_route.get('/')
def list_books() -> List[Book]:
    return handle_response(workflows.list_books())


app_settings = {
    "title": "Champions Book Store",
    "summary": """
        An API to manage a simple book store for adding and tracking book borrowing.
    """
}

app = FastAPI(**app_settings)
app.include_router(book_route)
