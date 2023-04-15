from django.http import JsonResponse
from django.urls import path
from django.views import View

import Servers.test_data


class OneKJson(View):
    def get(self, _):
        return JsonResponse(
            Servers.test_data.JSON_1K,
            safe=False
        )


class TenKJson(View):
    def get(self, _):
        return JsonResponse(
            Servers.test_data.JSON_10K,
            safe=False
        )


class HundredKJson(View):
    def get(self, _):
        return JsonResponse(
            Servers.test_data.JSON_100K,
            safe=False
        )


class OneKKJson(View):
    def get(self, _):
        return JsonResponse(
            Servers.test_data.JSON_1M,
            safe=False
        )


class FiveKKJson(View):
    def get(self, _):
        return JsonResponse(
            Servers.test_data.JSON_5M,
            safe=False
        )


json_response_urlpatterns = [
    path('1_k_json', OneKJson.as_view()),
    path('10_k_json', TenKJson.as_view()),
    path('100_k_json', HundredKJson.as_view()),
    path('1_kk_json', OneKKJson.as_view()),
    path('5_kk_json', FiveKKJson.as_view())
]
