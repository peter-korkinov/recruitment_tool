from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from recruitment_tool.jobs.models import JobModel
from recruitment_tool.jobs.serializers import JobSerializer
from recruitment_tool.interviews.models import new_interview


def free_recruiter_slots(job):
    interviews = job.interviewmodel_set.all()
    for interview in interviews:
        interview.candidate.recruiter.available_slots += 1


class JobsView(APIView):
    def get(self, request):
        query = request.query_params.get('skill')
        if query:
            jobs = JobModel.objects.filter(required_skills__title=query)
            serializer = JobSerializer(jobs, many=True)
            return Response({f'jobs with skill: {query}': serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_interview(serializer.data['id'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, job_id):
        job = get_object_or_404(JobModel, pk=job_id)
        free_recruiter_slots(job)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
