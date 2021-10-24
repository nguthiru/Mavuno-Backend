from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('wallet',WalletViewset,basename='wallet')

urlpatterns = router.urls