# axa tech task

This is a simple application which allows you to manage (view and create) a list of tasks, along with their due dates.

## TODO

- [ ] DB migrations
  - [ ] table for tasks
  - [ ] seed data for initial run
- [ ] Web UI to use to interact with api
  - [ ] list all notes page
  - [ ] add note button
- [ ] GET all notes endpoint
- [ ] POST new note endpoint
  - [ ] sanitise date/time input, only accept certain format
- [ ] tests

## Quick-Start Guide

- [Install `python`](https://www.python.org/downloads/) (version 3.11 or higher)
- [Install `poetry`](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Install `docker`
  - Mac: `brew install docker` using homebrew
  - Windows: [download docker desktop](https://www.docker.com/products/docker-desktop/)
- Spin up the database: `make db-up`
- Start the api: `make run` (NOTE: this will generate a venv for you)
- Run the tests: `make test`
- When finished, you can tear down the database: `make db-down`
