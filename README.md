# axa tech task

This is a simple application which allows you to manage (view and create) a list of tasks, along with their due dates.

## Pre-Requisites

- [Install `GNU Make`]
  - Mac: `brew install make` using homebrew
  - Windows: (https://cmake.org/download/)
- [Install `python`](https://www.python.org/downloads/) (version 3.11 or higher)
- [Install `poetry`](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Install `docker`
  - Mac: `brew install docker` using homebrew
  - Windows: [download docker desktop](https://www.docker.com/products/docker-desktop/)

## Quick Start Guide

1. Spin up the database & run the migrations:

```bash
make db-fresh
```

2. Start the api (NOTE: this will generate a venv for you):

```bash
make run
```

3. You can interact with the api using your REST client of choice. The endpoints you can interact with are as follows (also see `docs/endpoints.http`):

```bash
GET http://localhost:5000/health # Health check endpoint.

GET http://localhost:5000/tasks # Retrieves all tasks.

POST http://localhost:5000/tasks # Creates a task. You MUST have a body in the request.
content-type: application/json
{
    "task": "this is a random task that is due at some point", # This is required.
    "due_date": "27-06-2025 15:30"                             # This is optional. If it is entered, the date must be in the future.
}
```

4. Run the tests:

```bash
make test
```

5. When finished, you can tear down the database:

```bash
make db-down
```
