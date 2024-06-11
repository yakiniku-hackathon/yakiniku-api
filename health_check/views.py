from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import HealthCheck
from .serializers import HealthCheckSerializers


@api_view(['GET'])
@permission_classes([AllowAny])
def ready(request):
    if request.method == 'GET':
        return Response({
            "status": "OK",
            "text": "Ready!"
        })
    
@api_view(['GET'])
@permission_classes([AllowAny])
def live(request):
    if request.method == 'GET':
        return Response({
            "status": "OK",
            "text": "Live!"
        })

@api_view(['GET'])
@permission_classes([AllowAny])
def db_check(request):
    if request.method == 'GET':
        data = HealthCheck.objects.all()
        serializers = HealthCheckSerializers(data, many=True)
        return Response(serializers.data)