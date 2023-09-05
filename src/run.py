import uvicorn
from fastapi import FastAPI

from src.app import App

# Cria a instância do app
app: FastAPI = App().get_app()

if __name__ == "__main__":
    # Inicia o servidor
    uvicorn.run(app=app)
