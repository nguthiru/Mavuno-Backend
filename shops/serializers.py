from rest_framework import serializers
from .models import FarmItem, ItemImages, Ratings, Shop
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['user','name','city']
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['rating']
class FarmItemImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImages
        fields = ['image']



class FarmItemSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(read_only=True)
    image = FarmItemImagesSerializer(many=True)
    class Meta:
        model = FarmItem
        fields = ['shop','name','description','price','image']


