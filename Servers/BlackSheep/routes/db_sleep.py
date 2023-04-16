import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.db.sql_query import *


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/0_25_s_sleep")
    async def zero_25_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_0_25
            )
            return json({'hello': 'world'})

    @app.router.get('/0_5_s_sleep')
    async def zero_5_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_0_5
            )
            return json({'hello': 'world'})

    @app.router.get('/0_75_s_sleep')
    async def zero_75_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_0_75
            )
            return json({'hello': 'world'})

    @app.router.get("/1_s_sleep")
    async def one_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_1
            )
            return json({'Hello': 'World'})

    @app.router.get('/2_s_sleep')
    async def two_second_sleep(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            await con.fetch(
                QUERY_SLEEP_2
            )
            return json({'hello': 'world'})
