from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('wallet',WalletViewset,basename='wallet')
router.register('transactions',TransactionViewSet,basename='transactions')
router.register('subscriptions',SubscriptionViewSet,basename='subscriptions')

urlpatterns = router.urls