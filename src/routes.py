from fastapi import APIRouter


class MainRoutes:
    endpoint: APIRouter = APIRouter(prefix="", tags=["main"])

    @endpoint.get("/")
    async def root():
        return {"status_code": 200, "data": "OK"}
    @endpoint.get("/health")
    async def health():
        return {200, "Healthy"}
