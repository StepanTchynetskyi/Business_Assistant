import logging
from uvicorn.config import logger


def configure_logger(file_path: str = "/etc/business_assistant.log") -> None:
    file_handler = logging.FileHandler(file_path)
    logger.addHandler(file_handler)
