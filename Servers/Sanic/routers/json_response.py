from sanic import Blueprint, Request, json
import Servers.test_data

bp = Blueprint('json_response')


@bp.get("/1_k_json")
async def one_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_1K)
