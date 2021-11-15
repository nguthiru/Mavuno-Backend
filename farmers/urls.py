from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('produce',ProduceViewSet,basename='produce')
router.register('farm',FarmViewSet,basename='farm')
router.register("bids",BidViewSet,basename="bids")
urlpatterns = [
    path("farm/myfarm/",myfarm,name='my-farm')
]
urlpatterns+= router.urls