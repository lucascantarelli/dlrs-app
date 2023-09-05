from typing import Any, Generator

import pytest
from httpx import AsyncClient

from src.run import app


@pytest.fixture()
async def client() -> Generator[AsyncClient, Any, None]:
    test_client = AsyncClient(
        app=app,
        base_url="http://localhost:8000",
    )

    yield test_client
    await test_client.aclose()
