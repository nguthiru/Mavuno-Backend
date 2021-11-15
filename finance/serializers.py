from django.contrib.contenttypes import fields
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import *
from farmers.serializers import UniversalSerializer
# class UniversalSerializer:

#     serializers = {}
#     def register(self,serializer_or_iterable):
#         serializers = [serializer_or_iterable]
#         for serializer in serializers:
#             serializers[serializer.Meta.model.__name__] = serializer

#     def get_serializer(self,object,many=True):
#         if not many:
#             return serializers[object._meta.model.__name__]
#         else:
#             return serializers[object[0]._meta.model.__name__]



class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ["balance","uuid"]

class WalletActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletAction
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    wallet_action = WalletActionSerializer()

    class Meta:
        model = Transaction
        exclude =['id']

    

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class SubscriptionSeriailizer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = Subscription
        fields = "__all__"