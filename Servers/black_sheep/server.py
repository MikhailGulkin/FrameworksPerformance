import asyncio

import asyncpg
import blacksheep

from .routes import configure_routes
from ..db_query.async_query.sql_query import stub, create_engine, \
    build_sessions, DataBaseProvider


async def init_app() -> blacksheep.Application:
    app = blacksheep.Application()
    engine = create_engine()
    # db = DataBaseProvider(session)
    app.services.add_instance(build_sessions(engine=engine))
    # app.services.add_alias()
    configure_routes(app, pool=build_sessions(engine=engine))
    return app


loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
