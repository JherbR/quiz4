from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default='CREATED')
    hours_consumed = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
