# FastAPI + Async SQL Server: User Management API

This is my first FastAPI project — a simple user management API built with **FastAPI**, **SQLAlchemy (Async)**, and **Microsoft SQL Server**. 
It supports user registration and is designed with a clean, modern project structure for scalability and maintainability.

## Features

- FastAPI-based REST API
- Asynchronous database connection using `SQLAlchemy 2.0` + `aioodbc`
- Dependency injection with `Depends`
- Modular project structure (`routers`, `operations`, `schema`)
- Basic endpoints:
  - `POST /users/register` – register a new user


## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 (async)](https://docs.sqlalchemy.org/en/20/)
- [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server)
- `aioodbc` driver for async DB connections
- `Pydantic` for data validation

## What I Learned
 This project helped me understand:
 - FastAPI’s core features and routing
 - Asynchronous programming with databases
 - Clean separation of concerns in backend architecture



