from aiohttp import web

from Servers.db.sql_query import *

router = web.RouteTableDef()


@router.get('/0_25_s_sleep')
async def zero_25_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return web.json_response({'hello': 'world'})


@router.get('/0_5_s_sleep')
async def zero_5_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return web.json_response({'hello': 'world'})


@router.get('/0_75_s_sleep')
async def zero_75_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return web.json_response({'hello': 'world'})


@router.get('/1_s_sleep')
async def one_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return web.json_response({'hello': 'world'})


@router.get('/2_s_sleep')
async def two_second_sleep(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return web.json_response({'hello': 'world'})
