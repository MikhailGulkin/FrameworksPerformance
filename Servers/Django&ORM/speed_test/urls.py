import time

from django.contrib import admin
from django.db import connection
from django.http import JsonResponse
from django.urls import path
from django.views import View


class OneRecord(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = connection.cursor()

    def get(self, request):
        self.cursor.execute(f"""
                SELECT *
                FROM Speed
                LIMIT 1
            """)
        row = self.cursor.fetchall()
        return JsonResponse({'len': len(row)})


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('1_record', OneRecord.as_view()),
    # path('one_second_sleep', OneSecondResponse.as_view())
]
