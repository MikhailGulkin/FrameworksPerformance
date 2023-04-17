import json
from sanic import Blueprint, Request, json
from Servers.Python.db.sql_query import *

bp = Blueprint('db_sleep')


@bp.get("/0_25_s_sleep")
async def zero_25_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return json({'hello': 'world'})


@bp.get('/0_5_s_sleep')
async def zero_5_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return json({'hello': 'world'})


@bp.get('/0_75_s_sleep')
async def zero_75_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return json({'hello': 'world'})


@bp.get("/1_s_sleep")
async def one_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return json({'Hello': 'World'})


@bp.get('/2_s_sleep')
async def two_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return json({'hello': 'world'})
