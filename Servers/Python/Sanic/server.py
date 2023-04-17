from sanic import Sanic
from Servers.Python.Sanic.routers.json_response import bp as json_response_bp
from Servers.Python.Sanic.routers.db_sleep import bp as db_sleep_bp
from Servers.Python.Sanic.routers.db_select import bp as db_select_bp
from Servers.Python.db.async_query.db import Database


def init_app() -> Sanic:
    app_ = Sanic('Sanic_test_speed')
    db = Database()

    @app_.before_server_start
    async def setup_db(app__: Sanic):
        await db.create_pool()
        app__.ctx.pool = db.pool

    app_.blueprint([db_sleep_bp, db_select_bp, json_response_bp])

    return app_


app = init_app()
