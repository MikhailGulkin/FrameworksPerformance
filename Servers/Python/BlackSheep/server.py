from blacksheep import Application

from Servers.Python.BlackSheep.routers.db_sleep import config_routes as config_sleep_routes
from Servers.Python.BlackSheep.routers.db_select import config_routes as config_select_routes
from Servers.Python.BlackSheep.routers.json_response import config_routes as config_json_response_routes
from Servers.Python.BlackSheep.routers.extra import config_routes as config_extra_routes
from Servers.Python.utils.db.async_query.db import Database


def init_app() -> Application:
    app_ = Application()
    db = Database()

    @app_.on_start
    async def before_start(application: Application) -> None:
        await db.create_pool()
        application.services.add_instance(
            db.pool
        )

    config_sleep_routes(app_)
    config_select_routes(app_)
    config_json_response_routes(app_)
    config_extra_routes(app_)
    return app_


app = init_app()
