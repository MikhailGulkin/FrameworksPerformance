import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.db.sql_query import *


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/1_s_sleep")
    async def one_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_1
            )
            return json({'Hello': 'World'})
