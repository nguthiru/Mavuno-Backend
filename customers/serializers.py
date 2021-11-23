from rest_framework import serializers
from accounts.serializers import UserSerializer
from shops.serializers import FarmItemSerializer
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item = FarmItemSerializer()
    user = UserSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','item','user','quantity','date_paid']

        
