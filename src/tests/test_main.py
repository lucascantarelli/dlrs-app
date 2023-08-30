import pytest
from app.main import app
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")

    if response.status != 200:
        raise ValueError(f"HTTP Status: {response.status}")

    if response.json() != {"status_code": 200, "data": "healthy"}:
        raise ValueError(f"Response: {response.json()}")


@pytest.mark.anyio
async def test_main():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")

    if response.status != 200:
        raise ValueError(f"HTTP Status: {response.status}")

    if response.json() != {"status_code": 200, "data": "OK"}:
        raise ValueError(f"Response: {response.json()}")
