from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


class Developer(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.CharField(max_length=70, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

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