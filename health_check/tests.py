from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import HealthCheck
from .serializers import HealthCheckSerializers


class HealthCheckTestCase(APITestCase):

    fixtures = ['status.json']

    def test_ready(self):
        url = reverse('health_check_ready')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "status": "OK",
            "text": "Ready!"
        })

    def test_live(self):
        url = reverse('health_check_live')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "status": "OK",
            "text": "Live!"
        })

    def test_db_check(self):        
        url = reverse('health_check_db_check') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # シリアライザを使用してデータをシリアライズ
        data = HealthCheck.objects.all()
        serializers = HealthCheckSerializers(data, many=True)
        
        self.assertEqual(response.data, serializers.data)
