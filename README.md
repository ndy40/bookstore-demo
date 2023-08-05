# bookstore-demo
A bookstore demo application that explores the ideas of Railway Oriented Programming in Python.

## Project Objective
- Explore what building a project in python using the railway oriented programming approach.
- Make use of the *returns library* which facilitates the `railway oriented programming` approach.


## Sample Project Description

A simple API that provides a few CRUD functionalities around a bookstore. You can perform the following actions: 

1. Add books to store
2. Update quantity of books in store
3. Search books in store
4. Borrow books in store
5. Return books back to store

Once completed, I will write a brief writeup on my experience of building a simple project using the Railway Oriented Programming using Python. 
I will also conclude with my verdict on whether I would recommend adopting this approach in a real world project. 

### Structure

```
- project roots
  | 
  | - apps.py
  | - cli.py
  | - infrastructure/*
	  | - db_context
	  | - http 
  | - domains/*
      | - models.py
      | - requests.py
      | - functions.py
  | - workflows/*
      | - create_book.py
	  | - fetch_book.py
	  | - search_books.py
	  | - borrow_book.py
	  | - return_book.py
	  | - ....
  | - tests/*
```

## References
* [Railway Oriented Programming](https://fsharpforfunandprofit.com/rop/)
* [Returns library](https://returns.readthedocs.io/en/latest/index.html)
* [FastAPI](https://fastapi.tiangolo.com/)
