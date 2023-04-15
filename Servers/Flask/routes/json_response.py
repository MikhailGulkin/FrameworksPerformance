from flask import Blueprint

import Servers.test_data

router = Blueprint(
    'json_response',
    __name__
)


@router.route('/1_k_json')
def one_k_json():
    return Servers.test_data.JSON_1K


@router.route('/10_k_json')
def ten_k_json():
    return Servers.test_data.JSON_10K


@router.route('/100_k_json')
def hundred_k_json():
    return Servers.test_data.JSON_100K


@router.route('/1_kk_json')
def one_kk_json():
    return Servers.test_data.JSON_1M


@router.route('/5_kk_json')
def five_kk_json():
    return Servers.test_data.JSON_5M
