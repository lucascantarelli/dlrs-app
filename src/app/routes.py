from fastapi import APIRouter

from app.services.logger import Logger


class MainRoutes:
    endpoint: APIRouter = APIRouter(prefix="", tags=["main"])
    logger: Logger = Logger(__name__)

    @endpoint.get("/")
    async def root():
        await MainRoutes.logger.info("INFO")
        await MainRoutes.logger.error("ERROR")
        await MainRoutes.logger.warning("WARNING")
        return {"status_code": 200, "data": "OK"}

    @endpoint.get("/health")
    async def health():
        return {"status_code": 200, "data": "healthy"}
