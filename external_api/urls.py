from django.urls import path

from .views import get_weather

urlpatterns = [
    path('external_api/weather/', get_weather, name='get_weather'),
]