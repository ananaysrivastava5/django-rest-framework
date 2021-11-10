from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)
    passby = models.CharField(max_length=200, default='SOME STRING')