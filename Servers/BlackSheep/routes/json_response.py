from blacksheep.server.responses import json
from blacksheep import Application, Response

import Servers.test_data


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/1_k_json")
    async def one_k_json() -> Response:
        return json(Servers.test_data.JSON_1K)

    @app.router.get('/10_k_json')
    async def ten_k_json() -> Response:
        return json(Servers.test_data.JSON_10K)

    @app.router.get('/100_k_json')
    async def hundred_k_json() -> Response:
        return json(Servers.test_data.JSON_100K)

    @app.router.get('/1_kk_json')
    async def one_kk_json() -> Response:
        return json(Servers.test_data.JSON_1M)

    @app.router.get('/5_kk_json')
    async def five_kk_json() -> Response:
        return json(Servers.test_data.JSON_5M)
