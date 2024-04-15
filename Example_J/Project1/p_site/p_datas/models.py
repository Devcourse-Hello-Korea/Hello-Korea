from django.db import models

class MotelInfo(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)