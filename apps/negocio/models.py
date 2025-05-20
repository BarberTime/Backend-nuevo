from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
from .utils import get_negocio_folder

class Negocio(models.Model):
    id_negocio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    logo = CloudinaryField('logo', folder='barberia/logos')
    imagen = CloudinaryField('imagen', folder='barberia/imagenes')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'
        db_table = 'negocio'
    
    def __str__(self):
        return self.nombre
    
