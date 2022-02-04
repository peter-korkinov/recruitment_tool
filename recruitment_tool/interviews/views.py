from rest_framework.views import APIView
from rest_framework.response import Response

from recruitment_tool.interviews.models import InterviewModel
from recruitment_tool.interviews.serializers import InterviewSerializer


class InterViews(APIView):
    def get(self, request):
        interviews = InterviewModel.objects.all()
        serializer = InterviewSerializer(interviews, many=True)
        return Response({'interviews': serializer.data})
