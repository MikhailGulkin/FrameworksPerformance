import asyncpg
from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSelect


def config_routes(
        app: Application,
) -> None:
    @app.router.get(DbSelect.one_record)
    async def one_record(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_1
                ))})

    @app.router.get(DbSelect.one_k_records)
    async def one_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_1K
                ))})

    @app.router.get(DbSelect.ten_k_records)
    async def ten_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_10K
                ))})

    @app.router.get(DbSelect.hundred_k_records)
    async def hundred_k_records(pool: asyncpg.Pool) -> Response:
        async with pool.acquire() as con:
            return json({'len': len(
                await con.fetch(
                    QUERY_100K
                ))})
