import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Mystery, Question, UserMysteryStatus
from .serializers import MysterySerializers, QuestionSerializers, UserMysteryStatusSerializers

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_mysteries(request):
    if request.method == 'GET':
        mysteries = Mystery.objects.filter(published_at__isnull=False)
        serializers = MysterySerializers(mysteries, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_my_mysteries(request):
    if request.method == 'GET':
        mysteries = Mystery.objects.filter(user=request.user.id)
        serializers = MysterySerializers(mysteries, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_mystery(request, mystery_id):
    if request.method == 'GET':
        try:
            mystery = Mystery.objects.get(id=mystery_id)
        except Mystery.DoesNotExist:
            return Response({"error": "Mystery not found."}, status=status.HTTP_404_NOT_FOUND)
        serializers = MysterySerializers(mystery)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def post_mystery(request):
    mystery = request.data.copy()
    logger.debug('user_id:{}による新規謎解きの追加'.format(request.user.id))
    mystery['user'] = request.user.id
    mystery['status'] = 0
    serializer = MysterySerializers(data=mystery)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['PATCH'])
def patch_mystery(request, mystery_id):
    try:
        mystery = Mystery.objects.get(id=mystery_id)
    except Mystery.DoesNotExist:
        return Response({"error": "Mystery not found."}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        data = request.data
        serializer = MysterySerializers(mystery, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_questions(request, mystery_id):
        if request.method == 'GET':
            questions = Question.objects.filter(mystery=mystery_id)
        serializers = QuestionSerializers(questions, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_question(request, mystery_id):
    question = request.data.copy()
    logger.debug('user_id:{}による新規謎解きの追加'.format(request.user.id))
    question['user'] = request.user.id
    question['mystery'] = mystery_id
    serializer = QuestionSerializers(data=question)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_question(request, mystery_id, question_id):
    if request.method == 'GET':
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
        serializers = QuestionSerializers(question)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['PATCH'])
def patch_question(request, mystery_id, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        data = request.data
        serializer = QuestionSerializers(question, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_mysteries_status(request):
    if request.method == 'GET':
        user_mysteries_status = UserMysteryStatus.objects.filter(user=request.user.id)
        serializers = UserMysteryStatusSerializers(user_mysteries_status, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_mystery_status(request, status_id):
    if request.method == 'GET':
        try:
            user_mystery_status = UserMysteryStatus.objects.get(id=status_id)
        except UserMysteryStatus.DoesNotExist:
            return Response({"error": "Uset Mystery Status not found."}, status=status.HTTP_404_NOT_FOUND)
        serializers = UserMysteryStatusSerializers(user_mystery_status)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def post_user_mystery_status(request):
    logger.debug(request)
    user_mystery_status = request.data.copy()
    logger.debug('user_id:{}による謎解きのゲーム開始'.format(request.user.id))
    user_mystery_status['user'] = request.user.id
    serializer = UserMysteryStatusSerializers(data=user_mystery_status)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def patch_user_mystery_status(request, status_id):
    try:
        user_mystery_status = UserMysteryStatus.objects.get(id=status_id)
    except UserMysteryStatus.DoesNotExist:
        return Response({"error": "Question not found."}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        data = request.data
        serializer = UserMysteryStatusSerializers(user_mystery_status, data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)