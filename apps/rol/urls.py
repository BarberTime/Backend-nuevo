from django.urls import path
from .views import RolAPIView

urlpatterns = [
    path('api/v1/roles/', RolAPIView.as_view(), name='api_roles'),
]