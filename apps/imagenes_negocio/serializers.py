from rest_framework import serializers
from .models import ImagenesNegocio 

class ImagenesNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesNegocio
        fields = '__all__'