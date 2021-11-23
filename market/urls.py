from django.urls import path
from .views import *
urlpatterns = [
    path('price/<int:id>/',MarketPrice),
    path('price/',MarketPrice)
]