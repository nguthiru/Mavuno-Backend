from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from customers.models import OrderItem
from customers.serializers import OrderItemSerializer
from .models import FarmItem, Shop
from .serializers import FarmItemSerializer, ShopSerializer
# Create your views here
@api_view(['GET'])
def myshop(request):
    try:
        shop = Shop.objects.get(user=request.user.id)
        serialized = ShopSerializer(shop)
    

        return Response(serialized.data)
    except Exception as e:
        return Response({'error':str(e)},status=400)
class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class = FarmItemSerializer

    def get_queryset(self):
        return FarmItem.objects.filter(shop__user=self.request.user.id)

    def get_shop(self):
        return Shop.objects.get(user=self.request.user.id)
        
    @action(methods=['GET'],detail=False)
    def orders(self,*args,**kwargs):
        
        orders = OrderItem.objects.filter(item__shop=self.get_shop().id,paid=True)
        serialized = OrderItemSerializer(orders,many=True)
        return Response(serialized.data)

    
