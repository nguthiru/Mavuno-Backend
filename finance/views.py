from django.db.models.functions.datetime import ExtractMonth
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SubscriptionSeriailizer, TransactionSerializer, WalletSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Subscription, Transaction, Wallet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import ExtractWeek
from django.db.models import Sum
# Create your views here.

class WalletViewset(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return Wallet.objects.get(user=self.request.user)
    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def create(self, request):
        return Response({'error':'Operation not allowed'},status=400)
    def update(self, request,**kwargs):
        return Response({'error':'Operation not allowed'},status=400)
    def destroy(self, request,**kwargs):
        return Response({'error':'Operation not allowed'},status=400)
    def partial_update(self, request,**kwargs):
        return Response({'error':'Operation not allowed'},status=400)


    @action(methods=['GET'],detail=True)
    def mywallet(self):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)



class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(wallet__user=self.request.user.id)

    @action(methods=['GET'],detail=False)
    def stats(self,*args,**kwargs):
        response = {}
        
        # labels = self.get_queryset().annotate(week=ExtractWeek('date_added')).values('week').annotate(total=Sum('amount'))

        withdraws = self.get_queryset().filter(wallet_action__action='W').annotate(month=ExtractMonth('date_added')).values('month').annotate(total=Sum('amount'))
        bids = self.get_queryset().filter(wallet_action__action='B').annotate(month=ExtractMonth('date_added')).values('month').annotate(total=Sum('amount'))
        subs = self.get_queryset().filter(wallet_action__action='S').annotate(month=ExtractMonth('date_added')).values('month').annotate(total=Sum('amount'))
        deposits = self.get_queryset().filter(wallet_action__action='D').annotate(month=ExtractMonth('date_added')).values('month').annotate(total=Sum('amount'))
        response['withdraws'] = withdraws
        response['bids'] = bids
        response['subs'] = subs
        response['deposits'] = deposits


        return Response(response,status=200)
        
    
class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSeriailizer
    def get_queryset(self):
        return Subscription.objects.filter(wallet__user=self.request.user.id)

