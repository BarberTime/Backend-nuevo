from django.urls import path
from .views import UsuarioAPIView

urlpatterns = [
    path('api/v1/usuarios/', UsuarioAPIView.as_view(), name='api_usuarios'),
]   