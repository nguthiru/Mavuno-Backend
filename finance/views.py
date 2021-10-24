from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WalletSerializer
from .models import Wallet
# Create your views here.

class WalletViewset(viewsets.ModelViewSet):
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.get(user=self.request.user)

    
