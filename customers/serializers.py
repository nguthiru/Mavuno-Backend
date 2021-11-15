from rest_framework import serializers

from shops.serializers import FarmItemSerializer
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item = FarmItemSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','item','user','quantity']

        
