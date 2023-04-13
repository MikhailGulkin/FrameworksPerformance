import asyncio

import aiohttp
import asyncpg
from aiohttp import web

from Servers.db_query.query import *

router = web.RouteTableDef()


@router.get('/1_record')
async def one_record(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        query = await con.fetch(
            QUERY_1
        )
        return web.json_response({'len': len(query)})

@router.get('/1_s_sleep')
async def one_record(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return web.json_response({'hello': 'world'})


@router.get('/1_k_records')
async def one_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        query = await con.fetch(
            QUERY_1K
        )
        return web.json_response({'len': len(query)})


@router.get('/10_k_records')
async def ten_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        query = await con.fetch(
            QUERY_10K
        )
        return web.json_response({'len': len(query)})


@router.get('/100_k_records')
async def thousand_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        query = await con.fetch(
            QUERY_100K
        )
        return web.json_response({'len': len(query)})
