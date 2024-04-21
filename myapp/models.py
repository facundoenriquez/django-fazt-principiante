from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=200)


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
