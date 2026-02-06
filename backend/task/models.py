from django.db import models
from django.conf import settings
from project.models import Project

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=200)
    task_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='CREATED')
    hours_consumed = models.IntegerField(default=0)
    user_assigned = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()