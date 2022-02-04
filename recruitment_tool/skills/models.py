from django.db import models


class SkillModel(models.Model):
    title = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'{self.title}'

