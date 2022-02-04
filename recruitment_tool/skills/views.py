from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from recruitment_tool.skills.models import SkillModel
from recruitment_tool.skills.serializers import SkillSerializer


class ActiveSkillsView(APIView):
    def get(self, request):
        active_skills = SkillModel.objects.filter(candidatemodel=not None)
        serializer = SkillSerializer(active_skills, many=True)
        return Response({'active skills': serializer.data})


class SkillDetailsView(APIView):
    def get(self, request, skill_id):
        skill = get_object_or_404(SkillModel, pk=skill_id)
        serializer = SkillSerializer(skill)
        return Response({'skill': serializer.data})
