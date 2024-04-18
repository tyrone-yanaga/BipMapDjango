from django.db import models

# Create your models here.
class MapMarker(models.Model):
    crimetype = models.CharField(max_length=200)
    datetime = models.CharField(max_length=200)
    casenumber = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    lat = models.DecimalField()
    lon = models.DecimalField()