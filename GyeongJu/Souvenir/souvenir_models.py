from django.db import models

class Bread(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Shop(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=300)
    business_hours = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name
    

class ShopLocation(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name='location')
    lat = models.FloatField()
    lng = models.FloatField()
    
    def __str__(self):
        return f'Location of {self.shop.name}\n'