from django.db import models
# Create your models here. test the webhook
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
