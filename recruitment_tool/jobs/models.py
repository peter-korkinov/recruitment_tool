from django.db import models

from recruitment_tool.skills.models import SkillModel


class JobModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=2000)
    salary = models.FloatField()
    required_skills = models.ManyToManyField(SkillModel)

    def __str__(self):
        return f'{self.title}'


