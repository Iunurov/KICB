from rest_framework.routers import DefaultRouter
from django.urls import path, include
from bank.views import *


app_name = 'bank'

router = DefaultRouter()

router.register('acustomer', CustomerDetail2)
router.register('account', AccountViewSet)
router.register('action', ActionViewSet)
router.register('transaction', TransactionViewSet)
router.register('transfer', TransferViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('customer/', CustomerDetail3.as_view(), name='customer'),
    path('transfer_alt/', CreateTransferView.as_view()),

]

