from typing import Any, AsyncGenerator

import pytest
from httpx import AsyncClient

from src.main import app


@pytest.fixture()
async def client() -> AsyncGenerator[AsyncClient, Any]:
    test_client = AsyncClient(
        app=app,
        base_url="http://localhost:8000",
        headers={"Content-Type": "application/json"},
    )

    yield test_client
    await test_client.aclose()
