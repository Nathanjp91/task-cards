# task-cards

System contains the following 
- postgres docker container pulled from latest
- pgadmin docker container pulled from latest
- backend docker built from local folder (see Dockerfile)
- frontend docker build from local folder (see Dockerfile)
## Dependencies
- docker
- docker compose

## Installation
```
docker compose up -d --build
```

## Backend
Has a volume that runs the app, this is symlinked to the local directory

### Alembic
To run migrations, do it on the docker container. All code will be updated in the local directory because of the linked volume

To initially create alembic (should be completed already)
```
docker compose exec backend alembic init -t async migrations
```

To generate a migration
```
docker compose exec backend alembic revision --autogenerate -m "init"
```

To apply a migration
```
docker compose exec backend alembic upgrade head
```

Further tutorial can be found [here](https://testdriven.io/blog/fastapi-sqlmodel/)