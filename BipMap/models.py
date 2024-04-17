from django.db import models

# Create your models here.
class Map_marker(models.Model):
    crimetype = models.CharField(max_length=200)
    datetime = models.CharField(max_length=200)
    casenumber = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    location = models.ArrayField(models.CharField(max_length=200), size=2,)