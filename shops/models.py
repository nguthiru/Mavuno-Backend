from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
# Create your models here.
USER = get_user_model()
class Shop(models.Model):
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Ratings(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    rating = models.IntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self) -> str:
        return self.item
class FarmItem(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name="shop")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=100)
    discount = models.DecimalField(decimal_places=2,max_digits=100)

    rating = GenericRelation(Ratings)

    def __str__(self) -> str:
        return self.name

class ItemImages(models.Model):
    item = models.ForeignKey(FarmItem,on_delete=models.CASCADE,related_name="image")

    image = models.ImageField()

    def __str__(self) -> str:
        return self.item.name

