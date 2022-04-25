# Business Assistant

## Project Configuration


### Create `.env` file with environment variables(|- separator of possible values, choose only one):
```angular2html
CONFIG_TYPE=dev
DATABASE_URL=postgresql://db_user:db_password@db:db_port/db_name
POSTGRES_DB=db_name
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
APP_PORT=your_port(8000)
JWT_SECRET_KEY=your_secret_key
```
## Start server locally
### Install poetry from [Poetry installation](https://python-poetry.org/docs/#installation)
### To install project dependencies run `poetry install`
### To run server use command `poetry run python wsgi.py`

## Start server with docker-compose
### To run server with docker-compose use command `docker-compose up`

## Alembic Migrations
#### To migrate using alembic use command `poetry alembic revision --autogenerate -m "your message"`
#### To upgrade your db use command `poetry alembic upgrade head`