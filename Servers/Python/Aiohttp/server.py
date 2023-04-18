import asyncio

from aiohttp import web
import asyncpg

from Servers.Python.Aiohttp.routers.json_response import router as json_router
from Servers.Python.Aiohttp.routers.db_select import router as db_select_router
from Servers.Python.Aiohttp.routers.db_sleep import router as db_sleep_router


async def init_app() -> web.Application:
    app = web.Application()
    app['pool'] = await asyncpg.create_pool(
        database='SpeedTest',
        user='postgres',
        port='5431',
        password='1234',
        host='localhost'
    )

    app.add_routes(json_router)
    app.add_routes(db_select_router)
    app.add_routes(db_sleep_router)

    return app


loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
