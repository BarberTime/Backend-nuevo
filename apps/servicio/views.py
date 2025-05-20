from .models import Servicio
from .serializers import ServicioSerializer, ServicioDetailSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioDetail(generics.RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioDetailSerializer
    lookup_field = 'id_servicio'

class ServicioUpdate(generics.UpdateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioDetailSerializer
    lookup_field = 'id_servicio'

class ServicioDelete(generics.DestroyAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    lookup_field = 'id_servicio'

class ServicioPublicoList(generics.ListAPIView):
    serializer_class = ServicioSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        negocio_id = self.request.query_params.get('negocio_id')
        if negocio_id:
            return Servicio.objects.filter(negocio_id=negocio_id)
        return Servicio.objects.all()