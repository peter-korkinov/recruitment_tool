from django.db import models


class RecruiterModel(models.Model):
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=30)
    experience = models.IntegerField(default=1)
    available_slots = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.last_name} {self.email} {self.country}'
