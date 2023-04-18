from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.Python.utils.path import ExtraTests


def config_routes(
        app: Application,
) -> None:
    @app.router.get(ExtraTests.hello_world)
    async def hello_world() -> Response:
        return json({'Hello': 'World'})
