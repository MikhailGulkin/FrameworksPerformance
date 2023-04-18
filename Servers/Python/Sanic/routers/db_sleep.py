import json
from sanic import Blueprint, Request, json
from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSleep

bp = Blueprint('db_sleep')


@bp.get(DbSleep.zero_25_second_sleep)
async def zero_25_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return json({'hello': 'world'})


@bp.get(DbSleep.zero_5_second_sleep)
async def zero_5_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return json({'hello': 'world'})


@bp.get(DbSleep.zero_75_second_sleep)
async def zero_75_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return json({'hello': 'world'})


@bp.get(DbSleep.one_second_sleep)
async def one_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return json({'Hello': 'World'})


@bp.get(DbSleep.two_second_sleep)
async def two_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return json({'hello': 'world'})
