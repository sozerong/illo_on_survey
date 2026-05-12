import logging

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import USER_DB_URL

logger = logging.getLogger(__name__)

user_engine = create_async_engine(USER_DB_URL, echo=False, pool_pre_ping=True, pool_size=5)
UserSession = async_sessionmaker(user_engine, expire_on_commit=False)


class UserBase(DeclarativeBase):
    pass


async def get_user_db():
    async with UserSession() as session:
        yield session


async def init_db():
    from .models import user  # noqa: F401
    async with user_engine.begin() as conn:
        await conn.run_sync(UserBase.metadata.create_all)
