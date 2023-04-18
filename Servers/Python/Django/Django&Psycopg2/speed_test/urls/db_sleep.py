from django.http import JsonResponse
from django.urls import path
from django.views import View

from Servers.Python.utils.db.sql_query import *
from Servers.Python.utils.db.sync_query.db_con import cursor


class Zero25SecondSleep(View):
    def get(self, _):
        cursor.execute(QUERY_SLEEP_0_25)
        return JsonResponse({'Hello': 'World'})


class Zero5SecondSleep(View):

    def get(self, _):
        cursor.execute(QUERY_SLEEP_0_5)
        return JsonResponse({'Hello': 'World'})


class Zero75SecondSleep(View):

    def get(self, _):
        cursor.execute(QUERY_SLEEP_0_75)
        return JsonResponse({'Hello': 'World'})


class OneSecondSleep(View):

    def get(self, _):
        cursor.execute(QUERY_SLEEP_1)
        return JsonResponse({'Hello': 'World'})


class TwoSecondSleep(View):

    def get(self, _):
        cursor.execute(QUERY_SLEEP_2)
        return JsonResponse({'Hello': 'World'})


db_sleep_urlpatterns = [
    path('0_25_s_sleep', Zero25SecondSleep.as_view()),
    path('0_5_s_sleep', Zero5SecondSleep.as_view()),
    path('0_75_s_sleep', Zero75SecondSleep.as_view()),
    path('1_s_sleep', OneSecondSleep.as_view()),
    path('2_s_sleep', TwoSecondSleep.as_view())
]
