from django.db.models.aggregates import Count
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from market.models import MarketPrice
from farmers.models import Bid, Farm, Produce, Product, TrackedProducts
from farmers.serializers import BidSerializer, FarmSerializer, ProduceSerializer, ProductSerializer
from rest_framework.response import Response
from market.serializers import MarketPriceSerailizer
# Create your views here.

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
class ProduceViewSet(viewsets.ModelViewSet):
    serializer_class = ProduceSerializer

    def get_queryset(self):
        print(self.request.user.id)
        return Produce.objects.filter(farm__user=self.request.user.id)




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
        return Bid.objects.filter(produce__farm__user=self.request.user.id)

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


    @action(methods=['GET'],detail=False)
    def favproducts(self,*args,**kwargs):
        products = TrackedProducts.objects.filter(user=self.request.user)
        res = []

        for product in products:

            price = MarketPrice.objects.filter(product=product.id)

            res.append(MarketPriceSerailizer(price,many=True).data)

        return Response(res)

@api_view(['GET'])
def myfarm(request):
    try:
        farm = Farm.objects.get(user=request.user.id)
        serialized = FarmSerializer(farm)
    

        return Response(serialized.data)
    except Exception as e:
        return Response({'error':str(e)},status=400)

