from fastapi import FastAPI
from fastapi.testclient import TestClient

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

        # Registra as rotas
        self.register_routes()

    def register_routes(self) -> None:
        # Registra as rotas
        self._app.include_router(MainRoutes.endpoint)

    def get_app(self) -> TestClient:
        return self._app
