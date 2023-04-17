from django.http import JsonResponse
from django.urls import path
from django.views import View

from Servers.Python.db.sql_query import *
from Servers.Python.db.sync_query.db_con import cursor


class OneRecord(View):

    def get(self, _):
        cursor.execute(QUERY_1)
        return JsonResponse({'len': len(
            cursor.fetchall()
        )})


class OneKRecords(View):

    def get(self, _):
        cursor.execute(QUERY_1K)
        return JsonResponse({'len': len(
            cursor.fetchall()
        )})


class TenKRecords(View):

    def get(self, _):
        cursor.execute(QUERY_10K)
        return JsonResponse({'len': len(
            cursor.fetchall()
        )})


class ThousandKRecords(View):

    def get(self, _):
        cursor.execute(QUERY_100K)
        return JsonResponse({'len': len(
            cursor.fetchall()
        )})


db_select_urlpatterns = [
    path('1_record', OneRecord.as_view()),
    path('1_k_records', OneKRecords.as_view()),
    path('10_k_records', TenKRecords.as_view()),
    path('100_k_records', ThousandKRecords.as_view()),

]
