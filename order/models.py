from django.db import models

# Create your models here.

class Order(models.Model):
    title = models.CharField(max_length=100,)
    owner = models.IntegerField()
    
    
    
class OrderItem(models.Model):
    title = models.CharField(max_length=100,)
    order = models.IntegerField()
    product = models.IntegerField()
    