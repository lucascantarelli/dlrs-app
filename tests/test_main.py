import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_check(client: AsyncClient) -> None:
    response = await client.get("/health")

    if response.json() != {"status_code": 200, "data": "healthy"}:
        raise ValueError("Unhealthy")


@pytest.mark.anyio
async def test_main(client: AsyncClient) -> None:
    response = await client.get("/")

    if response.json() != {"status_code": 200, "data": "OK"}:
        raise ValueError("Error")
