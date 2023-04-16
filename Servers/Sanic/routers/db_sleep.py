import json
from sanic import Blueprint, Request, json
from Servers.db.sql_query import *

bp = Blueprint('db_sleep')


@bp.get("/0_25_s_sleep")
async def zero_25_second_sleep(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        await con.fetch(
            QUERY_SLEEP_0_25
        )
        return json({'hello': 'world'})
