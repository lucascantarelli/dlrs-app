import uvicorn

try:
    from src import App

    # Cria a instância do app
    app = App().create_app()

except Exception as e:
    print("Ocorreu um erro ao iniciar o app.")
    print(f"Error: {e}")

if __name__ == "__main__":
    # Inicia o servidor
    uvicorn.run(app)
