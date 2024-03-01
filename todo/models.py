from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    deadline = models.DateTimeField(null=True)
    done = models.BooleanField(default=False)
