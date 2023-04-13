import asyncio

import asyncpg

from .routes import router as time_router
from fastapi import FastAPI

from ..db_query.async_query.sql_query import stub, create_engine, \
    build_sessions, DataBaseProvider


def create_app() -> FastAPI:
    app = FastAPI()
    engine = create_engine()
    session = build_sessions(engine)
    db = DataBaseProvider(session)

    app.dependency_overrides[stub] = db.provide_db

    app.include_router(time_router)

    return app


app = create_app()
