from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Model, Vps
from .serializers import ModelSerializers, VpsSerializers


class GlbTestCase(APITestCase):

    fixtures = ['init_model.json', 'init_vps.json']

    def test_get_model(self):
        url = reverse('get_glb_model')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_vps(self):
        url = reverse('get_glb_vps')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)