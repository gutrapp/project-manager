from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    complete = models.BooleanField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

class Developer(models.Model):
    name = models.CharField(max_length=20)
    projects = models.ManyToManyField(Project, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)

class Bug(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    solved = models.BooleanField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
