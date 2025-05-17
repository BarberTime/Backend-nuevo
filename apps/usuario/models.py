from django.db import models
from apps.rol.models import Rol 
import uuid 
class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    foto_perfil = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
    
    def __str__(self):
        return self.nombre
