from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *

router = DefaultRouter()


urlpatterns = router.urls