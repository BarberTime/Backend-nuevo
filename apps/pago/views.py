from rest_framework import generics
from .models import Pago
from .serializers import PagoSerializer     

class PagoAPIView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer