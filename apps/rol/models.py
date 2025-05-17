from django.db import models
import uuid
class Rol(models.Model):
    id_rol = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    