from rest_framework import generics
from .models import Horario
from .serializers import HorarioSerializer  

class HorarioAPIView(generics.ListCreateAPIView):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

