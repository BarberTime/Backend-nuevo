from django.db import models
from apps.negocio.models import Negocio 
class ImagenesNegocio(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'ImagenesNegocio'
        verbose_name_plural = 'ImagenesNegocios'
        db_table = 'imagenes_negocio'
    
    def __str__(self):
        return self.imagen