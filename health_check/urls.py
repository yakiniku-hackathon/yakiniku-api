from django.urls import path

from .views import db_check, live, ready

urlpatterns = [
    path('ready/', ready, name='health_check_ready'),
    path('live/', live, name='health_check_live'),
    path('db_check/', db_check, name='health_check_db_check')
]