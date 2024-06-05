from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import HealthCheck
from .serializers import HealthCheckSerializers


@api_view(['GET'])
def ready(request):
    if request.method == 'GET':
        return Response({
            "status": "OK",
            "text": "Ready!"
        })
    
@api_view(['GET'])
def live(request):
    if request.method == 'GET':
        return Response({
            "status": "OK",
            "text": "Live!"
        })

@api_view(['GET'])
def db_check(request):
    if request.method == 'GET':
        data = HealthCheck.objects.all()
        serializers = HealthCheckSerializers(data, many=True)
        return Response(serializers.data)