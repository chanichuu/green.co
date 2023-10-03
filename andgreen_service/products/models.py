from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    image_link = models.CharField(max_length=256)
    

class Device(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Reading(models.Model):
    timestamp = models.DateTimeField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    ppm_co2_water = models.FloatField()
    ppm_co2_air = models.FloatField()
    water_temp = models.FloatField()