from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

from .models import Mystery
from .serializers import MysterySerializers


class AuthorizationMysteryTestCase(APITestCase):

    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def setUp(self):
        # テスト用ユーザーの作成
        self.user = User.objects.create_user(email='testuser@test.com', username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(refresh.access_token))

    def test_get_mysteries(self):
        url = reverse('get_mysteries')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_get_mystery(self):
        url = reverse('get_mystery', kwargs={'mystery_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_404_not_found_get_mystery(self):
        url = reverse('get_mystery', kwargs={'mystery_id': 4})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_mystery(self):
        url = reverse('post_mystery')
        data = {"title": "テスト用タイトル"}
        response = self.client.post(url, data)
        data = Mystery.objects.get(id=response.data['id'])
        serializers = MysterySerializers(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializers.data)
        

class MysteryTestCase(APITestCase):
    
    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def test_get_mysteries(self):
        url = reverse('get_mysteries')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
