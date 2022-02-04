from random import choice

from django.db import models

from recruitment_tool.skills.models import SkillModel
from recruitment_tool.data.recruiters_list import recruiters
from recruitment_tool.recruiters.models import RecruiterModel


def get_recruiter():
    recruiter_record = choice(recruiters)

    if RecruiterModel.objects.filter(email=recruiter_record['email']).exists():
        recruiter = RecruiterModel.objects.get(email=recruiter_record['email'])
        recruiter.experience += 1
        recruiter.save()
        return recruiter.pk

    recruiter = RecruiterModel.objects.create(**recruiter_record)
    return recruiter.pk


class CandidateModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField(max_length=3000)
    birth_date = models.DateField()
    skills = models.ManyToManyField(SkillModel)
    recruiter = models.ForeignKey(RecruiterModel, on_delete=models.CASCADE, default=get_recruiter())

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'


