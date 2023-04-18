from aiohttp import web

from Servers.Python.utils.path import ExtraTests

router = web.RouteTableDef()


@router.get(ExtraTests.hello_world)
async def hello_world(_: web.Request) -> web.Response:
    return web.json_response({"Hello": "World"})
