from django.contrib import admin

from shops.models import FarmItem, ItemImages, Ratings, Shop

# Register your models here.
admin.site.register([Shop,ItemImages,FarmItem,Ratings])