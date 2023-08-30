import uvicorn

from . import App

# Cria a instância do app
app = App().get_app()

if __name__ == "__main__":
    # Inicia o servidor
    uvicorn.run(app=app)
