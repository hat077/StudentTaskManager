from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    class Type(models.TextChoices):
        HOMEWORK = 'HW', 'Homework'
        PROJET = 'PR', 'Project'
        EXAM = 'EX', 'Exam'

    class Urgency(models.TextChoices):
        CRITICAL = 'CR', 'Critical'
        HIGH = 'HI', 'High'
        MEDIUM = 'ME', 'Medium'
        LOW = 'LO', 'Low'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(
        choices = Type.choices,
        max_length = 8,
        default = Type.HOMEWORK
    )
    task_urgency = models.CharField(
        choices = Urgency.choices,
        max_length = 8,
        default = Urgency.LOW
    )
    start_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title