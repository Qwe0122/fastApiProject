from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_async_session
from app.models import User
from app.dto.dtos import UserCreateDTO
from app.service.UserService import UserService
from app.repository.UserRepository import SqlUserRepository

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.post("/create")
async def create_user(
    user_dto: UserCreateDTO,
    session: AsyncSession = Depends(get_async_session)
):
    return await UserService(SqlUserRepository(session)).create_user(user_dto)

@user_router.get("/get/{id}")
async def get_user(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await UserService(SqlUserRepository(session)).get_user(id)