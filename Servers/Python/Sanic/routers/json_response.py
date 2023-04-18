from sanic import Blueprint, Request, json
from Servers.Python.utils.path import JsonResponse
import Servers.test_data

bp = Blueprint('json_response')


@bp.get(JsonResponse.one_k_json)
async def one_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_1K)


@bp.get(JsonResponse.ten_k_json)
async def ten_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_10K)


@bp.get(JsonResponse.hundred_k_json)
async def hundred_k_json(_: Request) -> json:
    return json(Servers.test_data.JSON_100K)


@bp.get(JsonResponse.one_kk_json)
async def one_kk_json(_: Request) -> json:
    return json(Servers.test_data.JSON_1M)


@bp.get(JsonResponse.five_kk_json)
async def five_kk_json(_: Request) -> json:
    return json(Servers.test_data.JSON_5M)
