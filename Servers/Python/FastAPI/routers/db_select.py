from fastapi import APIRouter, Request

from Servers.Python.db.sql_query import *

router = APIRouter()


@router.get("/1_record")
async def one_record(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_1
            ))}


@router.get('/1_k_records')
async def one_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_1K
            ))}


@router.get('/10_k_records')
async def ten_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_10K
            ))}


@router.get('/100_k_records')
async def thousand_k_records(request: Request) -> dict:
    async with request.app.state.pgpool.acquire() as con:
        return {'len': len(
            await con.fetch(
                QUERY_100K
            ))}
