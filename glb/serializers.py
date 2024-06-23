from rest_framework import serializers

from .models import Model, Vps


class VpsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vps
        fields = '__all__'

class ModelSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Model
        fields = '__all__'