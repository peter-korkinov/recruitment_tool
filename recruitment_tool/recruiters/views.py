from rest_framework.views import APIView
from rest_framework.response import Response

from recruitment_tool.recruiters.models import RecruiterModel
from recruitment_tool.recruiters.serializers import RecruiterSerializer


class RecruitersView(APIView):
    def get(self, request):
        query = request.query_params.get('level')
        if query is None:
            recruiters = RecruiterModel.objects.all()
            serializer = RecruiterSerializer(recruiters, many=True)
            return Response({'recruiters': serializer.data})

        recruiters = RecruiterModel.objects.filter(level=query)
        serializer = RecruiterSerializer(recruiters, many=True)
        return Response({f'recruiters with level {query}': serializer.data})

