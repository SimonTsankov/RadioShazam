from django.db import models
# Create your models here. test2
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
