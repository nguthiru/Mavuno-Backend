from rest_framework import serializers
from farmers.serializers import ProductSerializer
from .models import *
class MarketPriceSerailizer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = MarketPrice
        fields = '__all__'