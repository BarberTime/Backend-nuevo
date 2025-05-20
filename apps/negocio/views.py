from .models import Negocio
from .serializers import NegocioSerializer, NegocioDetailSerializer, ImagenSerializer, LogoSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response

class NegocioList(generics.ListCreateAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class NegocioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioDetailSerializer
    lookup_field = 'id_negocio'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo permitir ver los negocios del usuario actual
        return self.queryset.filter(usuario=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class NegocioPublicoList(generics.ListAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    permission_classes = []  # No requiere autenticación

class UploadImagen(generics.CreateAPIView):
    serializer_class = ImagenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        negocio_id = request.data.get('negocio_id')
        if not negocio_id:
            return Response({'error': 'negocio_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar que el negocio pertenece al usuario actual
        negocio = Negocio.objects.get(id_negocio=negocio_id, usuario=request.user)
        serializer.save(negocio_id=negocio_id)
        return Response({'message': 'Imagen subida exitosamente'}, status=status.HTTP_201_CREATED)
        if not negocio_id:
            return Response({'error': 'negocio_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        negocio = Negocio.objects.get(id_negocio=negocio_id)
        serializer.save(negocio_id=negocio_id)
        return Response({'message': 'Imagen subida exitosamente'}, status=status.HTTP_201_CREATED)

class UploadLogo(generics.CreateAPIView):
    serializer_class = LogoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        negocio_id = request.data.get('negocio_id')
        if not negocio_id:
            return Response({'error': 'negocio_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Verificar que el negocio pertenece al usuario actual
        negocio = Negocio.objects.get(id_negocio=negocio_id, usuario=request.user)
        serializer.save(negocio_id=negocio_id)
        return Response({'message': 'Logo subido exitosamente'}, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        negocio_id = request.data.get('negocio_id')
        if not negocio_id:
            return Response({'error': 'negocio_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
class NegocioUpdate(generics.UpdateAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    lookup_field = 'id_negocio'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo permitir actualizar los negocios del usuario actual
        return self.queryset.filter(usuario=self.request.user)

class NegocioDelete(generics.DestroyAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioSerializer
    lookup_field = 'id_negocio'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo permitir eliminar los negocios del usuario actual
        return self.queryset.filter(usuario=self.request.user)
    
class NegocioPublicoList(generics.ListAPIView):
    queryset = Negocio.objects.all()
    serializer_class = NegocioDetailSerializer
    permission_classes = []  # No se requiere autenticación