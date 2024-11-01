from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class UserRepository(ABC):
    @abstractmethod
    async def get_user(self, user_id: int) -> User.User:
        pass
    @abstractmethod
    async def create_user(self, user: User.User) -> User.User:
        pass

class SqlUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, user_id: int) -> User.User:
        result = await self.session.execute(select(User.User).where(User.User.id == user_id))
        return result.scalars().first()

    async def create_user(self, user: User.User) -> User.User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
