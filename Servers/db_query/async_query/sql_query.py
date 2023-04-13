from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def create_engine() -> AsyncEngine:
    return create_async_engine(
        'postgresql+asyncpg://postgres:1234@localhost:5431/SpeedTest',
    )


def build_sessions(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=engine,
        autoflush=False,  # Фиктивные изменения
        expire_on_commit=False,  # Ручные коммиты
    )


class DataBaseProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def provide_db(self) -> AsyncSession:
        async with self.pool() as session:
            yield session


async def stub():
    pass
