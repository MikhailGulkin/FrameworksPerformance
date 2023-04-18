from django.db import connection
from django.http import JsonResponse
from django.urls import path
from django.views import View

from Servers.Python.utils.db.sql_query import *


class OneRecord(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_1)
        return JsonResponse({'len': len(
            self.cursor.fetchall()
        )})


class OneKRecords(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_1K)
        return JsonResponse({'len': len(
            self.cursor.fetchall()
        )})


class TenKRecords(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_10K)
        return JsonResponse({'len': len(
            self.cursor.fetchall()
        )})


class HundredKRecords(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, _):
        self.cursor.execute(QUERY_100K)
        return JsonResponse({'len': len(
            self.cursor.fetchall()
        )})


db_select_urlpatterns = [
    path('1_record', OneRecord.as_view()),
    path('1_k_records', OneKRecords.as_view()),
    path('10_k_records', TenKRecords.as_view()),
    path('100_k_records', HundredKRecords.as_view()),

]
