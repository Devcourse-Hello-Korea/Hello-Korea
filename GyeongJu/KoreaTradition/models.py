from django.db import models

class TraditionExperienceInfo(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    info = models.CharField(max_length=200)
    call = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    homepage = models.URLField(max_length=100)
    