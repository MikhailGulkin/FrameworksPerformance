import json
from sanic import Blueprint, Request, json
from Servers.Python.db.sql_query import *

bp = Blueprint('db_select')


@bp.get("/1_record")
async def one_record(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(await con.fetch(
            QUERY_1
        ))})


@bp.get('/1_k_records')
async def one_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_1K
            ))})


@bp.get('/10_k_records')
async def ten_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_10K
            ))})


@bp.get('/100_k_records')
async def thousand_k_records(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(
            await con.fetch(
                QUERY_100K
            ))})
