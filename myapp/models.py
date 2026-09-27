from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name