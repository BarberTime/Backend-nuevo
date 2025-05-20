from django.db import models
from apps.negocio.models import Negocio 
from cloudinary.models import CloudinaryField

class ImagenesNegocio(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    negocio = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    imagen = CloudinaryField('imagen', folder='barberia/imagenes_negocio')
    
    class Meta:
        verbose_name = 'ImagenesNegocio'
        verbose_name_plural = 'ImagenesNegocios'
        db_table = 'imagenes_negocio'
    
    def __str__(self):
        return f'Imagen {self.id_imagen} - {self.negocio.nombre}'