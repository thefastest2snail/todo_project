from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from pkg_resources import _


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
