from django.db import connection
from django.http import JsonResponse
from django.urls import path
from django.views import View

from Servers.Python.utils.db.sql_query import *


class Zero25SecondSleep(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_SLEEP_0_25)
        return JsonResponse({'Hello': 'World'})


class Zero5SecondSleep(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_SLEEP_0_5)
        return JsonResponse({'Hello': 'World'})


class Zero75SecondSleep(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_SLEEP_0_75)
        return JsonResponse({'Hello': 'World'})


class OneSecondSleep(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_SLEEP_1)
        return JsonResponse({'Hello': 'World'})


class TwoSecondSleep(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_SLEEP_2)
        return JsonResponse({'Hello': 'World'})


db_sleep_urlpatterns = [
    path('0_25_s_sleep', Zero25SecondSleep.as_view()),
    path('0_5_s_sleep', Zero5SecondSleep.as_view()),
    path('0_75_s_sleep', Zero75SecondSleep.as_view()),
    path('1_s_sleep', OneSecondSleep.as_view()),
    path('2_s_sleep', TwoSecondSleep.as_view())
]
