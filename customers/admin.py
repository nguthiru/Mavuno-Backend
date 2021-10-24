from django.contrib import admin
from .models import OrderItem,ShippingDetails
# Register your models here.
admin.site.register([OrderItem,ShippingDetails])