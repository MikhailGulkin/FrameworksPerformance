from blacksheep.server.responses import json
from blacksheep import Application, Response

import Servers.test_data


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/1_k_json")
    async def one_second_sleep() -> Response:
        return json(Servers.test_data.JSON_1K)
