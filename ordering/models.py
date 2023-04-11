from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name= models.CharField(max_length=200)
    availability= models.IntegerField()
    cost= models.FloatField()
    photo= models.ImageField(blank=True)

class Order(models.Model):
    order_details=models.CharField(max_length=1000)
    user= models.ForeignKey(User, on_delete=models.CASCADE)


    
