from django.urls import path
from .views import ReservaAPIView

urlpatterns = [
    path('api/v1/reservas/', ReservaAPIView.as_view(), name='api_reservas'),
]