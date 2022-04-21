from fastapi import FastAPI
from .settings import logger
from .settings import environments


def create_app():
    logger.configure_logger()
    config = environments.get_environment()
    app = FastAPI(**config.fastapi_kwargs())
    return app
