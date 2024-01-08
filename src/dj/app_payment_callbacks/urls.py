#django urls
from django.urls import path

from . import views

urlpatterns = [
    path('liqpay/', views.liqpay_callback),
]

