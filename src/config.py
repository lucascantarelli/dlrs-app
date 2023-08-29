import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Classe de configuração do app
    APP_NAME: str = os.environ.get("APP_NAME")
    APP_VERSION: str = os.environ.get("APP_VERSION")
    APP_ENV: str = os.environ.get("APP_ENV", "development")

class DevelopmentConfig(Settings):
    pass

class ProductionConfig(Settings):
    pass

@lru_cache
def get_config() -> {}:
    configs = {"development": DevelopmentConfig, "production": ProductionConfig}
    return configs[os.environ.get("APP_ENV")]()
