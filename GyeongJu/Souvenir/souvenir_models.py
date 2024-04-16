from django.db import models

class Bread(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Shop(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=300)
    business_hours = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name