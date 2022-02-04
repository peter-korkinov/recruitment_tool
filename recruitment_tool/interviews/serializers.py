from rest_framework import serializers
from .models import InterviewModel


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewModel
        fields = '__all__'
