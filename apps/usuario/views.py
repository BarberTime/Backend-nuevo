from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer, RegisterSerializer, LoginSerializer, UsuarioDetalleSerializer
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from apps.usuario_rol.models import UsuarioRol

class LoginAPI(generics.CreateAPIView):
    """API para iniciar sesión de usuarios"""
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        """Procesa el inicio de sesión del usuario"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # Obtener o crear token para el usuario
        token, created = Token.objects.get_or_create(user=user)
        
        # Obtener el rol del usuario
        usuario_rol = UsuarioRol.objects.filter(usuario=user).first()
        rol = usuario_rol.rol.nombre if usuario_rol else 'Cliente'
        
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'rol': rol,
            'token': token.key
        })

from django.db import transaction
from apps.negocio.models import Negocio

class RegistroAPI(generics.CreateAPIView):
    """API para registrar nuevos usuarios"""
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        es_barbero = request.data.get('es_barbero', False)
        
        datos_negocio = {
            'nombre': request.data.get('nombre_negocio', ''),
            'direccion': request.data.get('direccion', '')
        }
        
        with transaction.atomic():
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            usuario = serializer.save()
            
            if es_barbero:
                Negocio.objects.create(
                    usuario=usuario,
                    nombre=datos_negocio['nombre'],
                    direccion=datos_negocio['direccion']
                )
            
            rol = 'Barbero' if es_barbero else 'Cliente'
            
            return Response({
                'usuario': UsuarioSerializer(usuario).data,
                'rol': rol
            }, status=201)

class ListaUsuarios(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class DetalleUsuario(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'

class ActualizarUsuario(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'pk'
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instancia = self.get_object()
        serializer = self.get_serializer(instancia, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class EliminarUsuario(generics.DestroyAPIView):
    """API para eliminar un usuario"""
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'pk'
    
    def delete(self, request, *args, **kwargs):
        """Elimina un usuario del sistema"""
        return self.destroy(request, *args, **kwargs)
    
class VerRolAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            usuario_rol = UsuarioRol.objects.get(usuario=request.user)
            return Response({
                'rol': usuario_rol.rol.nombre
            })
        except UsuarioRol.DoesNotExist:
            return Response({
                'rol': 'Cliente'
            })