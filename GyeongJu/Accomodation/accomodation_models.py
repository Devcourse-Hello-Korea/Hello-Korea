from django.db import models

class AccomodationInfo(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    class Meta:
        app_label = 'GyeongJu'