from fastapi import APIRouter

from .models import UserResponse

endpoint: APIRouter = APIRouter(prefix="/auth", tags=["auth"])


@endpoint.get("/login")
async def login():
    return {"message": "login"}


@endpoint.get("/logout")
async def logout():
    return {"message": "logout"}


@endpoint.get("/refresh")
async def refresh():
    return {"message": "refresh"}


@endpoint.get("/me")
async def me():
    return {"message": "me"}


@endpoint.post("/register", status_code=201, response_model=UserResponse)
async def register(user: UserResponse):
    return UserResponse(name=user.name)
