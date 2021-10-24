from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('produce',ProduceViewSet,basename='produce')
router.register("bids",BidViewSet,basename="bids")
router.register('shops',ShopViewSet,basename='shops')
router.register('farms',FarmViewSet,basename='farms')
router.register('farm-items',ItemViewSet,basename='farm-items')
router.register('cart',CartViewSet,basename='cart')
urlpatterns = router.urls