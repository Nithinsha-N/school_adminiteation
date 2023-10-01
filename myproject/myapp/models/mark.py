from django.db import models
from .subject import Subject
from .user import User
from django.contrib.auth.models import User

class Mark(models.Model):

    class Meta:

        unique_together = ('student', 'subject')

    score = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}"