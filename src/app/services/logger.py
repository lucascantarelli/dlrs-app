import logging
from logging.config import dictConfig

from app.settings import Settings


class Logger:
    _log: logging.Logger = None
    _settings: dict = Settings.config()

    def __init__(self, name: str):
        # Configura o logging.
        self._log_config: dict = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "access": {
                    "()": "uvicorn.logging.AccessFormatter",
                    "fmt": "%(levelprefix)s %(asctime)s - %(client_addr)s"
                    + '- "%(request_line)s" %(status_code)s',
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                    "use_colors": True,
                },
                "default": {
                    "()": "uvicorn.logging.DefaultFormatter",
                    "fmt": "%(levelprefix)s %(asctime)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                    "use_colors": True,
                },
            },
            "handlers": {
                "access": {
                    "class": "logging.StreamHandler",
                    "formatter": "access",
                    "stream": "ext://sys.stdout",
                },
                "default": {
                    "formatter": "default",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stderr",
                },
            },
            "loggers": {
                name: {"handlers": ["default"], "level": "DEBUG", "propagate": False},
                "uvicorn": {
                    "handlers": ["default"],
                    "level": "DEBUG",
                    "propagate": True,
                },
                "uvicorn.access": {
                    "handlers": ["access"],
                    "level": "INFO",
                    "propagate": False,
                },
                "uvicorn.error": {"level": "INFO", "propagate": False},
            },
        }

        dictConfig(self._log_config)
        self._log = logging.getLogger(name)

    async def info(self, message: str, *args):
        # Logging information
        self._log.info(message, *args)

    async def warning(self, message: str, *args):
        # Logging warning
        self._log.warning(message, *args)

    async def error(self, message: str, *args):
        # Logging error
        self._log.error(message, *args)
