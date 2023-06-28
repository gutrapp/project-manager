from django.db import models
from ..projects.models import Project

class Developer(models.Model):
    name = models.CharField(max_length=50)

class Team(models.Model):
    name = models.CharField(max_length=20)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)