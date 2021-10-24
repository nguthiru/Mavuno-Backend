from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import BasePermission, IsAuthenticated,AllowAny,SAFE_METHODS
from customers.models import OrderItem
from customers.serializers import OrderItemSerializer
from farmers.models import Bid, Farm, Produce
from farmers.serializers import BidSerializer, FarmSerializer, ProduceSerializer
from shops.serializers import FarmItemImagesSerializer, FarmItemSerializer, ShopSerializer
from shops.models import FarmItem, Shop
from rest_framework.response import Response
# Create your views here.


class isOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user



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

    def create(self,request,*args,**kwargs):
        user = request.user
        price = int(float(request.data.get('price')))
        weight = int(request.data.get('weight'))
        produce = Produce.objects.get(pk=request.data.get("produce"))
        if produce.least_orderable !=None:
            least = produce.least_orderable
        else:
            least = 0
        if price >= produce.starting_price and weight>least and weight!=0:
            
            bid = Bid.objects.create(user=user,produce=produce,kilograms=weight,bid_price=price)

            serializer = self.get_serializer_class()

            return Response(serializer(bid).data)
        else:
            error = {
                'error': "The entered values are not accepted"
            }
            return Response(error,status=400)
        

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer

    queryset = Shop.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = FarmItemSerializer
    queryset = FarmItem.objects.all()

class FarmViewSet(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    queryset=Farm.objects.all()


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated,isOwner]

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user,paid=False)


    def create(self, request, *args, **kwargs):
        farm_item = request.data.get('item_id')
        order_item = FarmItem.objects.get(pk=farm_item)
        if 'quantity' in request.data:
            cart_item, created = OrderItem.objects.get_or_create(item=order_item,user=request.user)
            cart_item.quantity = request.data.get('quantity')
            cart_item.save()
        else:
            cart_item, created = OrderItem.objects.get_or_create(item=order_item,user=request.user)

        if created == False: 
            cart_item.quantity+=1
            cart_item.save()

        

        serializer = self.get_serializer_class()

        return Response(serializer(cart_item).data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_queryset().get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        

    