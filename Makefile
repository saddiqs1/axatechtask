.DEFAULT_GOAL := help

.PHONY: help run test db-up db-down

help:
	@echo Available commands:
	@echo   run         - Activate the poetry environment and run the api
	@echo   test        - Activate the poetry environment and run the tests
	@echo   db-up       - Spin up the Postgres database using Docker Compose
	@echo   db-down     - Tear down the Postgres database

run:
	@poetry install --quiet && @poetry run python .\src\app.py

test:
	@poetry install --quiet && @poetry run pytest

db-up:
	@docker-compose up -d

db-down:
	@docker-compose down