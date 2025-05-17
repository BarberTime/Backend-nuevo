from rest_framework import generics
from .models import Rol
from .serializers import RolSerializer

class RolAPIView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
