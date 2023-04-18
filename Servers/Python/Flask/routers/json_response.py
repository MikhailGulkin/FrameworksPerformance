from flask import Blueprint

import Servers.test_data
from Servers.Python.utils.path import JsonResponse

bp = Blueprint(
    'json_response',
    __name__
)


@bp.route(JsonResponse.one_k_json)
def one_k_json():
    return Servers.test_data.JSON_1K


@bp.route(JsonResponse.ten_k_json)
def ten_k_json():
    return Servers.test_data.JSON_10K


@bp.route(JsonResponse.hundred_k_json)
def hundred_k_json():
    return Servers.test_data.JSON_100K


@bp.route(JsonResponse.one_kk_json)
def one_kk_json():
    return Servers.test_data.JSON_1M


@bp.route(JsonResponse.five_kk_json)
def five_kk_json():
    return Servers.test_data.JSON_5M
