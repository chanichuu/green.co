from django.db import models
from products.models import Product

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    pw = models.CharField(max_length=128)
    login_trials = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)
