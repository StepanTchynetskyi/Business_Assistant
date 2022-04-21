FROM python:3.10.4-alpine3.14

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app
RUN apk update && apk upgrade && apk add curl

COPY poetry.lock pyproject.toml ./

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -  \
    && source $HOME/.poetry/env \
    && poetry install

ENV PATH="${PATH}:/root/.poetry/bin"


COPY . ./

CMD poetry run python wsgi.py