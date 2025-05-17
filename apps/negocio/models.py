from django.db import models
from apps.usuario.models import Usuario 
import uuid   
class Negocio(models.Model):
    id_negocio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    logo = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'
        db_table = 'negocio'
    
    def __str__(self):
        return self.nombre
    
