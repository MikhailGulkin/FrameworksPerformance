import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from Servers.db_query.query import QUERY_1, QUERY_SLEEP_1


def configure_routes(
        app: Application,
        pool: async_sessionmaker[AsyncSession]
) -> None:
    @app.router.get("/1_record")
    async def one_record() -> Response:
        async with pool() as session:
            query = (await session.execute(
                text(QUERY_1)
            )).fetchall()
            return json({'len': len(query)})

    @app.router.get("/1_s_sleep")
    async def one_second_sleep() -> Response:
        async with pool() as session:
            await session.execute(
                text(QUERY_SLEEP_1)
            )
            return json({'hello': 'world'})
