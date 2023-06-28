from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class Developer(models.Model):
    name = models.CharField(max_length=20)

class Team(models.Model):
    name = models.CharField(max_length=20)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    complete = models.BooleanField()
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

class Bug(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    solved = models.BooleanField()
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
