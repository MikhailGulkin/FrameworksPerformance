import asyncio

import asyncpg
import blacksheep

from Servers.black_sheep.routes import configure_routes


async def init_app() -> blacksheep.Application:
    app_ = blacksheep.Application()

    # db = DataBaseProvider(session)
    # app.services.add_alias()
    configure_routes(app_)
    return app_


loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
