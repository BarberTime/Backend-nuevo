from django.urls import path
from .views import ServicioAPIView

urlpatterns = [
    path('api/v1/servicios/', ServicioAPIView.as_view(), name='api_servicios'),
]   