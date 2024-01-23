from app_order.views import NewOrderAPIView
from django.urls import path

class CustomerNewOrderView(NewOrderAPIView):
    pass

urlpatterns = [
    path('new-order/', CustomerNewOrderView.as_view()),
]
