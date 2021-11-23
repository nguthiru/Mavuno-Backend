from django.contrib.auth import get_user_model
from django.db import models

from shops.models import FarmItem
# Create your models here.
User = get_user_model()

class OrderItem(models.Model):
    item = models.ForeignKey(FarmItem,on_delete=models.CASCADE,related_name='order_item')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders_user')       
    quantity = models.IntegerField(default=1)
    paid = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_paid = models.DateTimeField(null=True,blank=True)


    def __str__(self) -> str:
        return f'{self.item} {self.user}';


class ShippingDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    notes = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user




