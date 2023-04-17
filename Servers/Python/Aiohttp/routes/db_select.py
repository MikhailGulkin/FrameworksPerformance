from aiohttp import web

from Servers.Python.db.sql_query import *

router = web.RouteTableDef()


@router.get('/1_record')
async def one_record(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_1
            ))})


@router.get('/1_k_records')
async def one_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_1K
            ))})


@router.get('/10_k_records')
async def ten_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_10K
            ))})


@router.get('/100_k_records')
async def thousand_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_100K
            ))})
