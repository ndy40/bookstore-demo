from fastapi import FastAPI

from infrastructure.http.rest.routes.books import book_route


app = FastAPI(title="Champions Book Store")
app.include_router(book_route)
