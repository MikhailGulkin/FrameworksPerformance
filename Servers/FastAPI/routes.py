from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from Servers.db_query.async_query.sql_query import stub
from Servers.db_query.query import *

router = APIRouter()


@router.get('/1_record')
async def one_record(session: AsyncSession = Depends(stub)):
    query = (await session.execute(
        text(QUERY_1)
    )).fetchall()
    return {'len': len(query)}


@router.get('/1_s_sleep')
async def one_second_sleep(session: AsyncSession = Depends(stub)):
    await session.execute(
        text(QUERY_SLEEP_1)
    )
    return {'hello': 'world'}
