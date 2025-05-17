from django.urls import path
from .views import NegocioAPIView

urlpatterns = [
    path('api/v1/negocios/', NegocioAPIView.as_view(), name='api_negocios'),
]