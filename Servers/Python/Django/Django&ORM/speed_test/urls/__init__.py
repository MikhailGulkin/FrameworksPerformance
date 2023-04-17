from django.urls import path, include
from .db_select import db_select_urlpatterns
from .db_sleep import db_sleep_urlpatterns
from .response_json import json_response_urlpatterns

urlpatterns = [
    path('', include(db_sleep_urlpatterns)),
    path('', include(db_select_urlpatterns)),
    path('', include(json_response_urlpatterns))
]
