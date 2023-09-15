import pytest

from src.auth.models import UserResponse


@pytest.mark.anyio
async def test_login_route(client):
    # Arrange
    response = await client.get("/auth/login")

    # Act
    data = response.json()

    # Assert
    if data["message"] != "login":
        raise ValueError("Not logged in")


@pytest.mark.anyio
async def test_logout_route(client):
    # Arrange
    response = await client.get("/auth/logout")

    # Act
    data = response.json()

    # Assert
    if data["message"] != "logout":
        raise ValueError("Not logged out")


@pytest.mark.anyio
async def test_refresh_route(client):
    # Arrange
    response = await client.get("/auth/refresh")

    # Act
    data = response.json()

    # Assert
    if data["message"] != "refresh":
        raise ValueError("No refresh")


@pytest.mark.anyio
async def test_me_route(client):
    # Arrange
    response = await client.get("/auth/me")

    # Act
    data = response.json()

    # Assert
    if data["message"] != "me":
        raise ValueError("No me information")


@pytest.mark.anyio
async def test_register_route(client):
    # Arrange
    user = UserResponse(name="testuser")

    # Act
    response = await client.post("/auth/register", json=user.model_dump(by_alias=True))

    # Assert
    if response.status_code != 201:
        raise ValueError("Unexpected status code")

    if response.json() != user.model_dump(by_alias=True):
        raise ValueError("User not matching")
