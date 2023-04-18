import json
from sanic import Blueprint, Request, json

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSelect

bp = Blueprint('db_select')


@bp.get(DbSelect.one_record)
async def one_record(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(await con.fetch(
            QUERY_1
        ))})


@bp.get(DbSelect.one_k_records)
async def one_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_1K
            ))})


@bp.get(DbSelect.ten_k_records)
async def ten_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_10K
            ))})


@bp.get(DbSelect.hundred_k_records)
async def hundred_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_100K
            ))})
