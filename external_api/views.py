import logging
import os

import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_weather(request):
    if request.method == 'GET':
        if "location" in request.GET:
            location = request.GET.get('location')
            secret_key = os.environ.get('WEATHER_SECRET_KEY', '')
            response = requests.get('https://api.weatherapi.com/v1/current.json?key={}&q={}'.format(secret_key, location))
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            secret_key = os.environ.get('WEATHER_SECRET_KEY', '')
            response = requests.get('https://api.weatherapi.com/v1/current.json?key={}&q=tokyo'.format(secret_key))
            return Response(response.json(), status=status.HTTP_200_OK)
