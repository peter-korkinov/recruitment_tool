from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from recruitment_tool.candidates.models import CandidateModel
from recruitment_tool.candidates.serializers import CandidateSerializer


class CandidateView(APIView):
    def get(self, request, candidate_id):
        candidate = get_object_or_404(CandidateModel, pk=candidate_id)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, candidate_id):
        candidate = get_object_or_404(CandidateModel, pk=candidate_id)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, candidate_id):
        candidate = get_object_or_404(CandidateModel, pk=candidate_id)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateCandidate(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
