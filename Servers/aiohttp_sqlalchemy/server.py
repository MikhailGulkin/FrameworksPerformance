from ..db_query.async_query.sql_query import stub, create_engine, \
    build_sessions, DataBaseProvider, async_sessionmaker

from aiohttp import web

from Servers.aiohttp_sqlalchemy.routes import router


def init_app() -> web.Application:
    app = web.Application()
    pool = build_sessions(engine=create_engine())
    app['pool'] = pool

    app.add_routes(router)
    return app


app = init_app()
