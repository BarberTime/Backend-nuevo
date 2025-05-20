from django.urls import path
from .views import NegocioList, NegocioDetail, NegocioUpdate, NegocioDelete, UploadImagen, UploadLogo, NegocioPublicoList

urlpatterns = [
    path('api/negocio/', NegocioList.as_view(), name='negocio-list'),
    path('api/negocio/<uuid:id_negocio>/', NegocioDetail.as_view(), name='negocio-detail'),
    path('api/negocio/<uuid:id_negocio>/actualizar/', NegocioUpdate.as_view(), name='negocio-update'),
    path('api/negocio/<uuid:id_negocio>/eliminar/', NegocioDelete.as_view(), name='negocio-delete'),
    path('api/negocio/<uuid:id_negocio>/upload-imagen/', UploadImagen.as_view(), name='upload-imagen'),
    path('api/negocio/<uuid:id_negocio>/upload-logo/', UploadLogo.as_view(), name='upload-logo'),
    path('api/negocios-publicos/', NegocioPublicoList.as_view(), name='negocios-publicos'),
]