from django.http import JsonResponse
from django.urls import path
from django.views import View

from Servers.Python.utils.path import ExtraTests


class HelloWorld(View):
    def get(self, _):
        return JsonResponse(
            {'Hello': 'World'}
        )


extra_response_urlpatterns = [
    path('hello', HelloWorld.as_view()),
]
