import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.Python.db.sql_query import *


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

    @app.router.get('/1_k_records')
    async def one_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_1K
                ))})

    @app.router.get('/10_k_records')
    async def ten_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_10K
                ))})

    @app.router.get('/100_k_records')
    async def thousand_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_100K
                ))})
