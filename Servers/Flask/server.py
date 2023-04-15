from flask import Flask
from Servers.Flask.routes.db_select import router as db_sel_router
from Servers.Flask.routes.db_sleep import router as db_sleep_router
from Servers.Flask.routes.json_response import router as json_router


def init_app() -> Flask:
    app_ = Flask(__name__)
    app_.register_blueprint(db_sel_router)
    app_.register_blueprint(db_sleep_router)
    app_.register_blueprint(json_router)
    return app_


app = init_app()
