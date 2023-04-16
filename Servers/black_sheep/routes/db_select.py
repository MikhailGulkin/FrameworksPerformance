import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.db.sql_query import *


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/1_record")
    async def one_record(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_1
                ))})
