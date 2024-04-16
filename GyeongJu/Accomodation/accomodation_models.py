from django.db import models

class AccomodationInfo(models.Model):
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    month = models.CharField(max_length=4)
    link = models.URLField(max_length=300)
    img_src1 = models.TextField(null=True)
    img_src2 = models.TextField(null=True)
    img_src3 = models.TextField(null=True)
    class Meta:
        app_label = 'GyeongJu'

