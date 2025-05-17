from rest_framework import generics
from .models import Servicio
from .serializers import ServicioSerializer      

class ServicioAPIView(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer   