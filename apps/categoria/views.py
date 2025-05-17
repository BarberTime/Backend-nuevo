from .models import Categoria
from .serializers import CategoriaSerializer
from rest_framework import generics

class CategoriaAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


    


