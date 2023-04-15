from blacksheep.server.responses import json
from blacksheep import Application, Response

import Servers.test_data


def configure_routes(
        app: Application,
) -> None:
    # @app.router.get("/1_record")
    # async def one_record() -> Response:
    #     async with pool() as session:
    #         query = (await session.execute(
    #             text(QUERY_1)
    #         )).fetchall()
    #         return json({'len': len(query)})
    #
    # @app.router.get("/1_s_sleep")
    # async def one_second_sleep() -> Response:
    #     async with pool() as session:
    #         await session.execute(
    #             text(QUERY_SLEEP_1)
    #         )
    #         return json({'hello': 'world'})

    @app.router.get("/1_k_json")
    async def one_second_sleep() -> Response:
        return json(Servers.test_data.JSON_1K)
