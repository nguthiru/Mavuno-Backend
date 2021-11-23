from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *

router = DefaultRouter()
router.register('shops',ShopViewSet,basename='shops')
router.register('items',ItemsViewSet,basename='shop_items')

urlpatterns = [
    path('myshop/',myshop)
]
urlpatterns += router.urls