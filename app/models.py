from django.db import models

# Create your models here.
class Customer(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    phone = models.IntegerField()
    address = models.TextField()