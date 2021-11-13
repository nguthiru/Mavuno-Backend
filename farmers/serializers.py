from rest_framework import serializers
from accounts.serializers import UserSerializer

from farmers.models import Bid, Branch, Farm, Produce, ProduceImages, Product
from rest_polymorphic.serializers import PolymorphicSerializer
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"

class FarmSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField("get_user")
    branch = BranchSerializer(many=True,read_only=True)
    class Meta:
        model = Farm
        fields = ['id',"farm_name","city","image","branch"]




    def get_user(self,farm):
        from accounts.serializers import UserSerializer
        return UserSerializer(farm.user,read_only=True).data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProduceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceImages
        fields = ['image']


class ProduceSerializer(serializers.ModelSerializer):

    produce_images = ProduceImageSerializer(many=True)
    product = ProductSerializer(read_only=True)
    farm = FarmSerializer(read_only=True)
    class Meta:
        model = Produce
        fields = ['id','name','farm','product','weight_kgs','starting_price','least_orderable','date_added','produce_images']
        ordering = ['-date_added',]

class BidSerializer(serializers.ModelSerializer):

    produce = ProduceSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Bid
        fields = ['id','user','produce','kilograms','bid_price','status','date_made']
        ordering = ['-date_made',]

class UniversalSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Bid:BidSerializer,
        Produce:ProduceSerializer,
        Farm:FarmSerializer
    }