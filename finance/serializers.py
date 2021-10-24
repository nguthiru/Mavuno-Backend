from rest_framework import serializers
from .models import *
class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ["balance","uuid"]

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'