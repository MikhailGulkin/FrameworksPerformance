from sanic import Blueprint, Request, json
from Servers.Python.utils.path import ExtraTests

bp = Blueprint('extra')


@bp.get(ExtraTests.hello_world)
async def hello_world(_: Request) -> json:
    return json({'Hello': 'World'})
