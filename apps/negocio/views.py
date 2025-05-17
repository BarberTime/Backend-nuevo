from rest_framework import generics
from .models import Negocio
from .serializers import NegocioSerializer      

class NegocioAPIView(generics.ListCreateAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer   