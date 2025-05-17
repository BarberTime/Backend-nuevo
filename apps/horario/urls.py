from django.urls import path
from .views import HorarioAPIView

urlpatterns = [
    path('api/v1/horarios/', HorarioAPIView.as_view(), name='api_horarios'),
]
