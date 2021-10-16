from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from farmers.models import Bid, Farm, Produce
from farmers.serializers import BidSerializer, FarmSerializer, ProduceSerializer
# Create your views here.

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

   
