from fastapi import APIRouter, Request

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSleep

router = APIRouter()


@router.get(DbSleep.zero_25_second_sleep)
async def zero_25_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return {'hello': 'world'}


@router.get(DbSleep.zero_5_second_sleep)
async def zero_5_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_5
        )
        return {'hello': 'world'}


@router.get(DbSleep.zero_75_second_sleep)
async def zero_75_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_75
        )
        return {'hello': 'world'}


@router.get(DbSleep.one_second_sleep)
async def one_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_1
        )
        return {'hello': 'world'}


@router.get(DbSleep.two_second_sleep)
async def two_second_sleep(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_2
        )
        return {'hello': 'world'}
