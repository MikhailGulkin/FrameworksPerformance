from flask import Flask

from Servers.Python.Flask.routers.db_select import bp as db_sel_bp
from Servers.Python.Flask.routers.db_sleep import bp as db_sleep_bp
from Servers.Python.Flask.routers.json_response import bp as json_bp
from Servers.Python.Flask.routers.extra import bp as extra_bp


def init_app() -> Flask:
    app_ = Flask(__name__)
    app_.register_blueprint(db_sel_bp)
    app_.register_blueprint(db_sleep_bp)
    app_.register_blueprint(json_bp)
    app_.register_blueprint(extra_bp)
    return app_


app = init_app()
