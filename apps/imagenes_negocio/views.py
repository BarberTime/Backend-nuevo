from rest_framework import generics
from .models import ImagenesNegocio
from .serializers import ImagenesNegocioSerializer      

class ImagenesNegocioAPIView(generics.ListCreateAPIView):
    queryset = ImagenesNegocio.objects.all()
    serializer_class = ImagenesNegocioSerializer