# Business Assistant

## Project Configuration
### Install poetry from [Poetry installation](https://python-poetry.org/docs/#installation)
#### To install project dependencies run `poetry install`

### Create `.env` file with environment variables(|- separator of possible values, choose only one):
```angular2html
CONFIG_TYPE=dev|prod|test
```

### To run server use command `poetry run python wsgi.py`