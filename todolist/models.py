from turtle import title
from typing_extensions import Self
from django.db import models

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey()
    date = models.TextField()
    title = models.TextField()
    description = models.TextField()
