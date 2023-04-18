from blacksheep.server.responses import json
from blacksheep import Application, Response

from Servers.Python.utils.path import JsonResponse

import Servers.test_data


def config_routes(
        app: Application,
) -> None:
    @app.router.get("/1_k_json")
    async def one_k_json() -> Response:
        return json(Servers.test_data.JSON_1K)

    @app.router.get(JsonResponse.ten_k_json)
    async def ten_k_json() -> Response:
        return json(Servers.test_data.JSON_10K)

    @app.router.get(JsonResponse.hundred_k_json)
    async def hundred_k_json() -> Response:
        return json(Servers.test_data.JSON_100K)

    @app.router.get(JsonResponse.one_kk_json)
    async def one_kk_json() -> Response:
        return json(Servers.test_data.JSON_1M)

    @app.router.get(JsonResponse.five_kk_json)
    async def five_kk_json() -> Response:
        return json(Servers.test_data.JSON_5M)
