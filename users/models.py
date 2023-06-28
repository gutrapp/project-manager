from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class Developer(models.Model):
    name = models.CharField(max_length=20)
    projects = models.ManyToManyField(Project)

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    complete = models.BooleanField()
    developers = models.ManyToManyField(Developer)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

class Bug(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    solved = models.BooleanField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
