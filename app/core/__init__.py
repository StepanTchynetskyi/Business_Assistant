from fastapi import FastAPI
from .settings import logger
from .settings import environments
from app.api.auth.views import router


def create_app():
    logger.configure_logger()
    config = environments.get_environment()
    app = FastAPI(**config.fastapi_kwargs())
    app.include_router(router)
    return app
