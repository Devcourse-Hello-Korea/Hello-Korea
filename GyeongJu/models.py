from django.db import models

# Create your models here.
class hard_coded_text(models.Model):
    lang = models.CharField(max_length=10)
    Gyeongju_text = models.CharField(max_length=30)
    Suncheon_text = models.CharField(max_length=30)
    Jeonju_text = models.CharField(max_length=30)
    lodging_text = models.CharField(max_length=30)
    Food_text = models.CharField(max_length=30)
    Experience_text = models.CharField(max_length=30)
    Souvenir_text = models.CharField(max_length=30)
    Main_Gyeongju_text1 = models.CharField(max_length=300)
    Main_Gyeongju_text2 = models.CharField(max_length=300)
    Main_Gyeongju_text3 = models.CharField(max_length=300)
    Main_Gyeongju_text4 = models.CharField(max_length=300)
