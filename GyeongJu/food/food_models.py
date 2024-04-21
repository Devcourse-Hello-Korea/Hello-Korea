from django.db import models

class korean_food_model(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

class western_food_model(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

class japanese_food_model(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

class chinese_food_model(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

class text_food_form(models.Model):
    lang = models.CharField(max_length=10)
    korean_text = models.CharField(max_length=20)
    western_text = models.CharField(max_length=20)
    japanese_text = models.CharField(max_length=20)
    chinese_text = models.CharField(max_length=20)