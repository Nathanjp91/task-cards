# Backend Application

Contains the API portion of the system.
Uses Fastapi to serve CRUD routes.
Database is postgres docker container, modelled and connected with sqlalchemy backend via sqlmodel, using alembic to setup models in database

pre-commit framework handles linting via flake8 and black with custom pip requirements builder

testing via pytest and pytest-check
## Dependencies
- python 3.10>
- poetry

## Installation
setup the environment
```
poetry shell
poetry install
```
setup pre-commit for development hooks
```
pre-commit install
```
## Running
from app directory (with requirements.txt and poetry.lock)
```
uvicorn app.main:app
```

## Testing
Testing is a pre-commit hook on commit/push, however can be run manually via
```
pytest
```