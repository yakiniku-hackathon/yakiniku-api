from django.urls import path

from .views import db_check, live, ready

urlpatterns = [
    path('health_check/ready/', ready, name='health_check_ready'),
    path('health_check/live/', live, name='health_check_live'),
    path('health_check/db_check/', db_check, name='health_check_db_check')
]