from app_order.views import NewOrderAPIView
from django.urls import path

from app_order.views import get_payment_data

class CustomerNewOrderView(NewOrderAPIView):
    pass

urlpatterns = [
    path('new-order/payment-data/', get_payment_data),
    path('new-order/', CustomerNewOrderView.as_view()),
]
