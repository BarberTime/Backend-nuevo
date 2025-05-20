
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('apps.rol.urls')),
    path('', include('apps.negocio.urls')),
    path('', include('apps.horario.urls')),
    path('', include('apps.reserva.urls')),
    path('', include('apps.servicio.urls')),
    path('', include('apps.categoria.urls')),
    path('', include('apps.pago.urls')),
    path('', include('apps.imagenes_negocio.urls')),
]