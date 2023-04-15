import psycopg2

from django.http import JsonResponse
from django.urls import path
from django.views import View


class OneRecord(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cursor = psycopg2.connect(
            dbname='SpeedTest',
            user='postgres',
            port='5431',
            password='1234',
            host='localhost'
        ).cursor()

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
