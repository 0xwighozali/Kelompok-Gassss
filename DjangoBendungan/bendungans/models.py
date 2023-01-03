from django.db import models

# Create your models here.
class Bendungan(models.Model):
    nm_bendungan = models.CharField(max_length=100)
    lk_bendungan = models.CharField(max_length=100)
    luas_bendungan = models.CharField(max_length=100)
    vlm_bendungan = models.CharField(max_length=100)