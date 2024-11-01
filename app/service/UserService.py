from app.repository.UserRepository import UserRepository
from app.models import User
from app.dto import dtos

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_dto: dtos.UserCreateDTO) -> User:
        new_user = User.User(name=user_dto.name, age=user_dto.age)
        created_user = await self.user_repository.create_user(new_user)
        return created_user

    async def get_user(self, user_id: int) -> User:
        return await self.user_repository.get_user(user_id)