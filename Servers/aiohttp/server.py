import asyncio

import asyncpg
from aiohttp import web
import asyncpg

from Servers.aiohttp.routes import router


async def init_app() -> web.Application:
    app = web.Application()
    app['pool'] = await asyncpg.create_pool(
        database='SpeedTest',
        user='postgres',
        port='5431',
        password='1234',
        host='localhost'
    )

    app.add_routes(router)
    return app


loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
