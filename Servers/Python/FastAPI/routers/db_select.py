from fastapi import APIRouter, Request

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.path import DbSelect

router = APIRouter()


@router.get(DbSelect.one_record)
async def one_record(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_1
            ))}


@router.get(DbSelect.one_k_records)
async def one_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_1K
            ))}


@router.get(DbSelect.ten_k_records)
async def ten_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_10K
            ))}


@router.get(DbSelect.hundred_k_records)
async def hundred_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_100K
            ))}
