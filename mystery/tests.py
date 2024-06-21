from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

from .models import Mystery, Question
from .serializers import MysterySerializers, QuestionSerializers


class AuthorizationMysteryTestCase(APITestCase):

    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def setUp(self):
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

    def test_patch_mystery(self):
        url = reverse('patch_mystery', kwargs={'mystery_id': 2})
        data = {"complate_msg": "テスト用完全制覇メッセージ"}
        response = self.client.patch(url, data)
        data = Mystery.objects.get(id=response.data['id'])
        serializers = MysterySerializers(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers.data)

    def test_404_not_found_patch_mystery(self):
        url = reverse('patch_mystery', kwargs={'mystery_id': 12})
        data = {"complate_msg": "テスト用完全制覇メッセージ"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

class MysteryTestCase(APITestCase):
    
    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def test_get_mysteries(self):
        url = reverse('get_mysteries')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_mystery(self):
        url = reverse('get_mystery', kwargs={'mystery_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_mystery(self):
        url = reverse('post_mystery')
        data = {"title": "テスト用タイトル"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_mystery(self):
        url = reverse('patch_mystery', kwargs={'mystery_id': 2})
        data = {"complate_msg": "テスト用完全制覇メッセージ"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class AuthorizationQuestionTestCase(APITestCase):

    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def setUp(self):
        self.user = User.objects.create_user(email='testuser@test.com', username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + str(refresh.access_token))

    def test_get_questions(self, ):
        url = reverse('get_questions', kwargs={'mystery_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_question(self, ):
        url = reverse('get_question', kwargs={'mystery_id': 1, 'question_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_404_not_found_get_question(self):
        url = reverse('get_question', kwargs={'mystery_id': 1, 'question_id': 4})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_question(self, ):
        url = reverse('post_question', kwargs={'mystery_id': 1})
        data = {
            "title": 'テスト用問題のタイトル',
            "description": 'テスト用問題文'
        }
        response = self.client.post(url, data)
        data = Question.objects.get(id=response.data['id'])
        serializers = QuestionSerializers(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializers.data)

    def test_patch_question(self):
        url = reverse('patch_question', kwargs={'mystery_id': 1, 'question_id': 1})
        data = {"hint": "ヒント用メッセージだよー"}
        response = self.client.patch(url, data)
        data = Question.objects.get(id=response.data['id'])
        serializers = QuestionSerializers(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializers.data)

    def test_404_not_found_patch_question(self):
        url = reverse('patch_question', kwargs={'mystery_id': 1, 'question_id': 3})
        data = {"hint": "ヒント用メッセージだよー"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class QuestionTestCase(APITestCase):
    
    fixtures = ['init_mystery.json', 'init_question.json', 'admin.json']

    def test_get_questions(self):
        url = reverse('get_questions', kwargs={'mystery_id': 1})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_question(self):
        url = reverse('get_question', kwargs={'mystery_id': 1, 'question_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_question(self):
        url = reverse('post_question', kwargs={'mystery_id': 1})
        data = {
            "title": 'テスト用問題のタイトル',
            "description": 'テスト用問題文'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_mystery(self):
        url = reverse('patch_question', kwargs={'mystery_id': 1, 'question_id': 1})
        data = {"hint": "ヒント用メッセージだよー"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)