from typing import Dict, Any
from enum import Enum
from uvicorn.config import logger


class BaseConfig:
    config_type = "base"
    debug: bool = False,
    docs_url: str = "/docs"
    openapi_prefix: str = "",
    openapi_url: str = "/openapi.json",
    redoc_url: str = "/redoc",
    title: str = "Business Assistant",
    version: str = "0.1.0"
    disable_docs: bool = False

    @classmethod
    def fastapi_kwargs(cls) -> Dict[str, Any]:
        return cls.__dict__


class DevelopmentConfig(BaseConfig):
    debug: bool = True


class TestConfig(BaseConfig):
    debug: bool = True


class ProductionConfig(BaseConfig):
    pass


class ConfigTypeEnum(Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"

    @classmethod
    def _missing_(cls, value):
        logger.warning(value + " config type is not exist, chose DEV environment type")
        return ConfigTypeEnum.DEV
