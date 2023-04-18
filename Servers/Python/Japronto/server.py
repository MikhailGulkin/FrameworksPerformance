import sys

from japronto import Application

import Servers.test_data
from Servers.Python.utils.path import ExtraTests, JsonResponse


def parse_factory(keyword: str, default_arg: int):
    def parse_cmd_args(cmd_arg: list[str]) -> int:
        for line in cmd_arg:
            try:
                return int(line.replace(keyword, ''))
            except ValueError:
                continue
        return default_arg

    return parse_cmd_args


def one_k_json(request):
    return request.Response(json=Servers.test_data.JSON_1K)


def ten_k_json(request):
    return request.Response(json=Servers.test_data.JSON_10K)


def hundred_k_json(request):
    return request.Response(json=Servers.test_data.JSON_100K)


def hello_world(request):
    return request.Response(json={'Hello': 'World'})


def init_app():
    app_ = Application()

    r = app_.router
    r.add_route(JsonResponse.one_k_json, one_k_json, method='GET')
    r.add_route(JsonResponse.ten_k_json, ten_k_json, method='GET')
    r.add_route(JsonResponse.hundred_k_json, hundred_k_json, method='GET')
    r.add_route(ExtraTests.hello_world, hello_world, method='GET')
    return app_


app = init_app()
app.run(
    port=parse_factory('port=', 5008)(sys.argv),
    worker_num=parse_factory('workers=', 1)(sys.argv)
)
