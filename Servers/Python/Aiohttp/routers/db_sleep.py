from aiohttp import web

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSleep

router = web.RouteTableDef()


@router.get(DbSleep.zero_25_second_sleep)
async def zero_25_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return web.json_response({'hello': 'world'})


@router.get(DbSleep.zero_5_second_sleep)
async def zero_5_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return web.json_response({'hello': 'world'})


@router.get(DbSleep.zero_75_second_sleep)
async def zero_75_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return web.json_response({'hello': 'world'})


@router.get(DbSleep.one_second_sleep)
async def one_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return web.json_response({'hello': 'world'})


@router.get(DbSleep.two_second_sleep)
async def two_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return web.json_response({'hello': 'world'})
