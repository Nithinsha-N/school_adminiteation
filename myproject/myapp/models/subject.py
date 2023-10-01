from django.db import models
from .user import User
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=10)
    teachers = models.ManyToManyField(User, related_name='teacher_subjects')

    def __str__(self):
        return self.name
