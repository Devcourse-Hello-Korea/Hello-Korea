from django.db import models

class Breads(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name