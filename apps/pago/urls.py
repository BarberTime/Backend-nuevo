from django.urls import path
from .views import PagoAPIView

urlpatterns = [
    path('api/v1/pagos/', PagoAPIView.as_view(), name='api_pagos'),
]