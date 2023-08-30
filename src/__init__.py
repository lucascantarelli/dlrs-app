from fastapi import FastAPI

from .routes import MainRoutes
from .settings import Settings


class App:
    # Classe de configuração do app
    _app: FastAPI
    _settings: dict = Settings.config()

    def __init__(self) -> None:
        # Cria a instância do app
        self._app = FastAPI(
            title=self._settings.APP_NAME,
            description="",
            version=self._settings.APP_VERSION,
        )

    def create_app(self) -> FastAPI():
        # Registra as rotas
        self._app.include_router(MainRoutes.endpoint)

        return self._app
