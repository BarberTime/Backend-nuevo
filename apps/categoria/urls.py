from django.urls import path
from .views import CategoriaAPIView

urlpatterns = [
    path('api/v1/categorias/', CategoriaAPIView.as_view(), name='api_categorias'),
]
