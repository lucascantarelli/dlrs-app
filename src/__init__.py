from fastapi import APIRouter, FastAPI
from fastapi.responses import RedirectResponse

from .config import get_config


class App:
    # Classe de configuração do app
    _app: FastAPI
    _settings: dict = get_config()
    _router: APIRouter = APIRouter()

    def __init__(self) -> None:
        # Cria a instância do app
        self._app = FastAPI(
            title=self._settings.APP_NAME,
            description="",
            version=self._settings.APP_VERSION,
        )
        # Cria o middleware
    @_router.get("/")
    def index() -> RedirectResponse:
        # Redireciona para a documentação
        return RedirectResponse("/docs")
    def create_app(self) -> FastAPI():
        # Registra as rotas
        self._app.include_router(self._router)
        return self._app
