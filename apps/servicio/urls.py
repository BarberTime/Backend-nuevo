from django.urls import path
from .views import ServicioList, ServicioDetail, ServicioUpdate, ServicioDelete, ServicioPublicoList

urlpatterns = [
    path('api/servicio/', ServicioList.as_view(), name='servicio-list'),
    path('api/servicio/<uuid:id_servicio>/', ServicioDetail.as_view(), name='servicio-detail'),
    path('api/servicio/<uuid:id_servicio>/actualizar/', ServicioUpdate.as_view(), name='servicio-update'),
    path('api/servicio/<uuid:id_servicio>/eliminar/', ServicioDelete.as_view(), name='servicio-delete'),
    path('api/servicios-publicos/', ServicioPublicoList.as_view(), name='servicios-publicos'),
]