import json
from sanic import Blueprint, Request, json
from Servers.db.sql_query import *

bp = Blueprint('db_select')


@bp.get("/1_record")
async def one_record(request: Request) -> json:
    async with request.app.ctx.pool.acquire() as con:
        return json({'len': len(await con.fetch(
            QUERY_1
        ))})
