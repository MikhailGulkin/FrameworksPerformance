from fastapi import FastAPI

from Servers.Python.utils.db.async_query.db import Database

from Servers.Python.FastAPI.routers.db_select import router as db_select_router
from Servers.Python.FastAPI.routers.db_sleep import router as db_sleep_router
from Servers.Python.FastAPI.routers.json_response import router as json_router
from Servers.Python.FastAPI.routers.extra import router as extra_router


def init_app() -> FastAPI:
    app_ = FastAPI()
    db = Database()

    @app_.on_event("startup")
    async def startup():
        await db.create_pool()
        app_.state.pgpool = db.pool

    app_.include_router(db_select_router)
    app_.include_router(db_sleep_router)
    app_.include_router(json_router)
    app_.include_router(extra_router)
    return app_


app = init_app()
