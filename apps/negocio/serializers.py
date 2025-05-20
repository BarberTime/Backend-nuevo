from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import CurrentUserDefault
from .models import Negocio

class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = ['id_negocio', 'nombre', 'direccion', 'telefono', 'logo', 'imagen', 'fecha_registro']
        read_only_fields = ['id_negocio', 'fecha_registro', 'usuario']
        extra_kwargs = {
            'logo': {'required': False},
            'imagen': {'required': False}
        }
    
    def create(self, validated_data):
        return Negocio.objects.create(**validated_data)

from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class NegocioDetailSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    
    class Meta:
        model = Negocio
        fields = ['id_negocio', 'nombre', 'usuario', 'direccion', 'telefono', 'logo', 'imagen', 'fecha_registro']
        read_only_fields = ['id_negocio', 'fecha_registro', 'usuario']
        extra_kwargs = {
            'logo': {'required': False},
            'imagen': {'required': False}
        }

class ImagenSerializer(serializers.Serializer):
    imagen = serializers.ImageField(required=True)
    
    def save(self, negocio_id):
        negocio = Negocio.objects.get(id_negocio=negocio_id)
        negocio.imagen = self.validated_data['imagen']
        negocio.save()
        return negocio

class LogoSerializer(serializers.Serializer):
    logo = serializers.ImageField(required=True)
    
    def save(self, negocio_id):
        negocio = Negocio.objects.get(id_negocio=negocio_id)
        negocio.logo = self.validated_data['logo']
        negocio.save()
        return negocio