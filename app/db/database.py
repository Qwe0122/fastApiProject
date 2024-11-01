from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings.config import settings

# Получаем URL базы данных
DATABASE_URL = settings.DATABASE_URL

# Создаем асинхронный движок
async_engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


# Базовый класс для декларативных моделей
Base = declarative_base()

# Функция для получения асинхронной сессии
async def get_async_session():
    async with async_session_maker() as session:
        yield session

# # Функция для получения синхронной сессии
# def get_db():
#     db = sync_session_maker()
#     try:
#         yield db
#     finally:
#         db.close()