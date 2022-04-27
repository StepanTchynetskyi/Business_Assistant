FROM python:3.10.4-buster

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app
RUN apt-get update

COPY poetry.lock pyproject.toml ./
ENV PATH="${PATH}:/root/.poetry/bin"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    &&. $HOME/.poetry/env \
    && poetry install

COPY . ./

CMD poetry install && poetry run alembic upgrade head && poetry run python wsgi.py