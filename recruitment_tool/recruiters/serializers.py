from rest_framework import serializers
from .models import RecruiterModel


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterModel
        fields = '__all__'
