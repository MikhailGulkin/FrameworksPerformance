from aiohttp import web
from sqlalchemy import text

from Servers.db_query.query import *

router = web.RouteTableDef()


@router.get('/1_record')
async def one_record(request: web.Request) -> web.Response:
    async with request.app['pool']() as session:
        query = (await session.execute(
            text(QUERY_1)
        )).fetchall()
        return web.json_response({'len': len(query)})
