from functools import lru_cache

import uvicorn
from fastapi import FastAPI

from src.auth.routes import endpoint as auth_routes

from .events import Events
from .settings import Settings


class App:
    @lru_cache
    def app_settings() -> Settings:
        # Carrega as configurações
        return Settings()

    @staticmethod
    def create_app() -> FastAPI:
        # Cria o app
        settings = App.app_settings()

        app = FastAPI(
            title=settings.APP_NAME,
            description="Dlrs API",
            version=settings.APP_VERSION,
        )
        app.settings = settings

        # Registra eventos
        app.add_event_handler("startup", Events.startup_event)
        app.add_event_handler("shutdown", Events.shutdown_event)

        # Registra rotas
        app.include_router(auth_routes)

        return app

    @staticmethod
    def run_app(app: FastAPI) -> None:
        # Inicia o servidor
        uvicorn.run(app, host=app.settings.HOST, port=app.settings.PORT)
