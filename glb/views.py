import logging

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Vps, Model
from .serializers import VpsSerializers, ModelSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def get_glb_model(request):
    if request.method == 'GET':
        models = Model.objects.all()
        serializers = ModelSerializers(models, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_glb_vps(request):
    if request.method == 'GET':
        vpses = Vps.objects.all()
        serializers = VpsSerializers(vpses, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)