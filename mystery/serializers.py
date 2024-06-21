from rest_framework import serializers

from .models import Mystery, Question


class MysterySerializers(serializers.ModelSerializer):

    class Meta:
        model = Mystery
        fields = '__all__'

class QuestionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'