"""
URL configuration for speed_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

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
