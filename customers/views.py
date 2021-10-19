from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from customers.models import OrderItem
from customers.serializers import OrderItemSerializer
from farmers.models import Bid, Farm, Produce
from farmers.serializers import BidSerializer, FarmSerializer, ProduceSerializer
from shops.serializers import FarmItemImagesSerializer, FarmItemSerializer, ShopSerializer
from shops.models import FarmItem, Shop
from rest_framework.response import Response
# Create your views here.

class ProduceViewSet(viewsets.ModelViewSet):
    serializer_class = ProduceSerializer

    def get_queryset(self):
        return Produce.objects.all()


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action=='create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(user=self.request.user.id)

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer

    queryset = Shop.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = FarmItemSerializer
    queryset = FarmItem.objects.all()


def view_cart(request):
    order_qs = OrderItem.objects.filter(user=request.user,paid=False)
    serializer_class = OrderItemSerializer(order_qs,many=True)

    return Response(serializer_class.data)
