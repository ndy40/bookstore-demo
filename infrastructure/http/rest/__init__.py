from fastapi import FastAPI

from infrastructure.http.rest.routes.books import book_route


app_settings = {
    "title": "Champions Book Store",
    "summary": """
        An API to manage a simple book store for adding and tracking book borrowing.
    """
}

app = FastAPI(**app_settings)
app.include_router(book_route)
