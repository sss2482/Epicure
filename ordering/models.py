from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

from users.models import User
usr= User.objects.get(username='sakam')

class Item(models.Model):
    name= models.CharField(max_length=200)
    availability= models.IntegerField()
    cost= models.FloatField()
    photo= models.ImageField(blank=True)

class Order(models.Model):
    STATUS_CHOICES=(('Payment transaction-id not submitted', 'Payment transaction-id not submitted'),
                    ('Payment verification pending','Payment verification pending'),
                    ('Payment not received','Payment not received'),
                    ('Payment verification done','Payment verification done'),
                    ('Delivered','Delivered'),)
    order_details=models.JSONField(max_length=1000)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, choices=STATUS_CHOICES,default='Payment verification pending')
    transaction_id=models.CharField(max_length=200, blank=True)
    cost=models.FloatField(default=0)
    address=models.TextField(max_length=400, blank=True, null=True)


    
