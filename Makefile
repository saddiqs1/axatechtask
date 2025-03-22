.DEFAULT_GOAL := help

.PHONY: help run test db-up db-down

help:
	@echo Available commands:
	@echo   run                                           - Activate the poetry environment and run the api
	@echo   test                                          - Activate the poetry environment and run the tests
	@echo   db-up                                         - Spin up the Postgres database using Docker Compose
	@echo   db-down                                       - Tear down the Postgres database
	@echo   db-migration-create name='MIGRATION NAME'     - Create migration
	@echo   db-migration-up                               - Run migrations to the latest available migration
	@echo   db-migration-down                             - Downgrade the most recent migration

run:
	@poetry install --quiet && @poetry run python .\src\app.py

test:
	@poetry install --quiet && @poetry run pytest

db-up:
	@docker-compose up -d

db-down:
	@docker-compose down

db-migration-create:
	@poetry install --quiet && @poetry run alembic revision -m '$(name)'

db-migration-up:
	@poetry install --quiet && @poetry run alembic upgrade head

db-migration-down:
	@poetry install --quiet && @poetry run alembic downgrade -1