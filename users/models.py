from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    developers = models.ManyToManyField(Developer)

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    developers = models.ManyToManyField(Developer)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Bug(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    solved = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
