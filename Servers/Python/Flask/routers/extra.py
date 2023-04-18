from flask import Blueprint

import Servers.test_data
from Servers.Python.utils.path import ExtraTests

bp = Blueprint(
    'extra',
    __name__
)


@bp.route(ExtraTests.hello_world)
def hello_world():
    return {"Hello": "world"}
