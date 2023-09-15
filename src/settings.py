import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Classe de configuração do app
    APP_NAME: str = os.environ.get("APP_NAME", "Test APP")
    APP_VERSION: str = os.environ.get("APP_VERSION", "0.0.0")
    APP_ENV: str = os.environ.get("APP_ENV", "development")
    APP_HOST: str = os.environ.get("APP_HOST", "localhost")
    APP_PORT: int = os.environ.get("APP_PORT", 8000)
    APP_RELOAD: bool = True
