import os
from app.core.settings import config_setup
from uvicorn.config import logger

environments = {
    config_setup.ConfigTypeEnum.DEV: config_setup.DevelopmentConfig,
    config_setup.ConfigTypeEnum.PROD: config_setup.ProductionConfig,
    config_setup.ConfigTypeEnum.TEST: config_setup.TestConfig
}


def get_environment():
    config_type = os.environ.get("CONFIG_TYPE").lower()
    config = environments.get(config_setup.ConfigTypeEnum(config_type))
    logger.info("App started with " + config.__name__)
    return config()
