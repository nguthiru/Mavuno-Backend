
from django.contrib import admin
from .models import Farm,Bid,Branch,Produce,Product,ProduceImages,TrackedProducts
# Register your models here.
admin.site.register([Farm,Bid,Branch,Produce,Product,ProduceImages,TrackedProducts])