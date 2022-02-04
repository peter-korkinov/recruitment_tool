from django.db import models

from recruitment_tool.candidates.models import CandidateModel
from recruitment_tool.jobs.models import JobModel


class InterviewModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.job} {self.candidate}'


def new_interview(job_id):
    job = JobModel.objects.get(pk=job_id)
    required_skills = job.required_skills.all()
    candidates = CandidateModel\
        .objects.filter(skills__in=required_skills)\
        .annotate(num_skills=models.Count('skills'))\
        .order_by('-num_skills')

    for candidate in candidates:
        recruiter = candidate.recruiter
        if recruiter.available_slots > 0:
            InterviewModel.objects.create(**{'job': job, 'candidate': candidate})
            recruiter.available_slots -= 1
            recruiter.save()
