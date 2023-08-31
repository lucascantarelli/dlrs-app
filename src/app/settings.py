import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Classe de configuração do app
    APP_NAME: str = os.environ.get("APP_NAME")
    APP_VERSION: str = os.environ.get("APP_VERSION")
    APP_ENV: str = os.environ.get("APP_ENV", "development")

    # Logger settings
    APP_LOG_FILE: str = os.environ.get("APP_LOG_FILE", "logging.conf")
    APP_LOG_LEVEL: str = os.environ.get("APP_LOG_LEVEL", "DEBUG")
    APP_LOG_FORMAT: str = os.environ.get(
        "APP_LOG_FORMAT",
        "%(asctime)s %(levelname)s %(message)s",
    )

    @lru_cache
    def config() -> {}:
        configs = {"development": DevelopmentConfig, "production": ProductionConfig}
        return configs[os.environ.get("APP_ENV")]()


class DevelopmentConfig(Settings):
    pass


class ProductionConfig(Settings):
    pass
