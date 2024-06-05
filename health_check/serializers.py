from rest_framework import serializers

from .models import HealthCheck


class HealthCheckSerializers(serializers.ModelSerializer):

    class Meta:
        model = HealthCheck
        fields = '__all__'