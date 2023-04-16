from fastapi import APIRouter
from fastapi import Request

from Servers.db.sql_query import *

router = APIRouter()


@router.get("/0_25_s_sleep")
async def zero_25_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return {'hello': 'world'}


@router.get('/0_5_s_sleep')
async def zero_5_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return {'hello': 'world'}


@router.get('/0_75_s_sleep')
async def zero_75_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return {'hello': 'world'}


@router.get('/1_s_sleep')
async def one_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return {'hello': 'world'}


@router.get('/2_s_sleep')
async def two_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return {'hello': 'world'}
