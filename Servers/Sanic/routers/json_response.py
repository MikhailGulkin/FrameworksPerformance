from sanic import Blueprint, Request, json
import Servers.test_data

bp = Blueprint('json_response')


@bp.get("/1_k_json")
async def one_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_1K)


@bp.get('/10_k_json')
async def ten_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_10K)


@bp.get('/100_k_json')
async def hundred_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_100K)


@bp.get('/1_kk_json')
async def one_kk_json(_: Request) -> json:
    return json(Servers.test_data.JSON_1M)


@bp.get('/5_kk_json')
async def five_kk_json(_: Request) -> json:
    return json(Servers.test_data.JSON_5M)
