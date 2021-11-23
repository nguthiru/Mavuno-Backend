from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MarketPrice as MarketPriceModel
from .serializers import MarketPriceSerailizer
from itertools import groupby


@api_view(['GET'])
def MarketPrice(request, **kwargs):
    if id in kwargs:

        price_qs = MarketPriceModel.objects.filter(product=kwargs['id'])

        return Response(MarketPriceSerailizer(price_qs, many=True).data)
    else:
        price_qs = MarketPriceModel.objects.all()

        def designation_key_func(price): return price.product.id
        products = []
        for designation, member_group in groupby(price_qs, designation_key_func):
            print(designation)
            products += [MarketPriceSerailizer(
                list(member_group), many=True).data]

        return Response(products)
