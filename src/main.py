from fastapi import FastAPI

from src import App

# Cria a instância do app
app: FastAPI = App.create_app()

if __name__ == "__main__":
    # Inicia o servidor
    App.run_app(app)
