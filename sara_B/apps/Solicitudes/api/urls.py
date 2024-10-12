from django.urls import path
from apps.Seguridad.CRUD import GetGeneral,PostGeneral,PUT_DELETE_General
from apps.Solicitudes.api.serializers import SolicitudSerializers, EmpleadoSerializers,CategoriaServicioSerializers

urlpatterns=[
    path(''),

]



