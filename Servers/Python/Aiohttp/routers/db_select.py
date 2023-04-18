from aiohttp import web

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSelect

router = web.RouteTableDef()


@router.get(DbSelect.one_record)
async def one_record(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_1
            ))})


@router.get(DbSelect.one_k_records)
async def one_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_1K
            ))})


@router.get(DbSelect.ten_k_records)
async def ten_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_10K
            ))})


@router.get(DbSelect.hundred_k_records)
async def hundred_k_records(request: web.Request) -> web.Response:
    async with request.app['pool'].acquire() as con:
        return web.json_response({'len': len(
            await con.fetch(
                QUERY_100K
            ))})
