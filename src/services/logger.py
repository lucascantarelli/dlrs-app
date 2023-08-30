import logging

from src.settings import Settings


class Logger:
    _log: logging.Logger = None
    _settings: dict = Settings.config()

    def __init__(self, name: str):
        # Configura o logging.
        logging.basicConfig(
            format=self._settings.APP_LOG_FORMAT,
            level=self._settings.APP_LOG_LEVEL,
        )

        # Seta o logging.
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
