from django.db import models
class Hospital(models.Model):
    sido = models.CharField(max_length=50),
    name = models.CharField(max_length=50),
    medical = models.IntegerField(),
    room = models.IntegerField(),
    tel = models.CharField(max_length=15),
    address = models.CharField(max_length=100)
# Create your models here.
