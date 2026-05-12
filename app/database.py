import logging

import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import PG_DB, PG_HOST, PG_PASSWORD, PG_PORT, PG_USER, USER_DB_URL

logger = logging.getLogger(__name__)


async def _ensure_database():
    conn = await asyncpg.connect(
        host=PG_HOST,
        port=int(PG_PORT),
        user=PG_USER,
        password=PG_PASSWORD,
        database="postgres",
    )
    try:
        exists = await conn.fetchval(
            "SELECT 1 FROM pg_database WHERE datname = $1", PG_DB
        )
        if not exists:
            await conn.execute(f'CREATE DATABASE "{PG_DB}"')
            logger.info("DB 생성: %s", PG_DB)
    finally:
        await conn.close()


user_engine = create_async_engine(USER_DB_URL, echo=False, pool_pre_ping=True, pool_size=5)
UserSession = async_sessionmaker(user_engine, expire_on_commit=False)


class UserBase(DeclarativeBase):
    pass


async def get_user_db():
    async with UserSession() as session:
        yield session


async def init_db():
    from .models import user  # noqa: F401
    await _ensure_database()
    async with user_engine.begin() as conn:
        await conn.run_sync(UserBase.metadata.create_all)
