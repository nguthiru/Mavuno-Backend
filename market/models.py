from django.db import models

# Create your models here.
from farmers.models import Product

class MarketPrice(models.Model):
    product = models.ForeignKey(Product)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

