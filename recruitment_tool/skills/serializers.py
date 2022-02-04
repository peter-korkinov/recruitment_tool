from rest_framework import serializers
from .models import SkillModel


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = '__all__'
