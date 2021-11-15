from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from farmers.models import Bid, Farm, Produce
from farmers.serializers import BidSerializer, FarmSerializer, ProduceSerializer
from rest_framework.response import Response
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

    @action(methods=["GET"],detail=False)
    def stats(self):
        pass

class BidViewSet(viewsets.ModelViewSet):
    serializer_class = BidSerializer

    def get_queryset(self):
        return Bid.objects.filter(produce__farm__user=self.request.user.id)

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

@api_view(['GET'])
def myfarm(request):
    try:
        farm = Farm.objects.get(user=request.user.id)
        serialized = FarmSerializer(farm)
    

        return Response(serialized.data)
    except Exception as e:
        return Response({'error':str(e)},status=400)

