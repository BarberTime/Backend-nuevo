from django.urls import path
from .views import ImagenesNegocioAPIView

urlpatterns = [
    path('api/v1/imagenes_negocio/', ImagenesNegocioAPIView.as_view(), name='api_imagenes_negocio'),
]