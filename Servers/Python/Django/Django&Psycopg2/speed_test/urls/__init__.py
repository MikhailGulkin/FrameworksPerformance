from django.urls import path, include
from .db_select import db_select_urlpatterns
from .db_sleep import db_sleep_urlpatterns

urlpatterns = [
    path('', include(db_sleep_urlpatterns)),
    path('', include(db_select_urlpatterns)),
]
