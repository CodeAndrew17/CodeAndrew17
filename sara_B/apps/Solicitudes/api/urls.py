from django.urls import path
from apps.Seguridad.CRUD import GetGeneral,PostGeneral,PUT_DELETE_General
from apps.Solicitudes.api.serializers import SolicitudSerializers, ClienteSerializers,CategoriaServicioSerializers
from apps.Solicitudes.models import Cliente, Solicitud, CategoriaServicio
from apps.Solicitudes.api.views import PostSolicitud

urlpatterns=[
    path('cliente/', PostGeneral.as_view(model =Cliente, serializer_class= ClienteSerializers)),
    path('cliente_api/',GetGeneral.as_view(model =Cliente, serializer_class= ClienteSerializers)),
    path('cliente_api/<int:pk>',GetGeneral.as_view(model =Cliente, serializer_class= ClienteSerializers)),

    path('categoriaservicio/',PostGeneral.as_view(model =CategoriaServicio,serializer_class=CategoriaServicioSerializers)),
    path('categoriaservicio_api/',GetGeneral.as_view(model =CategoriaServicio,serializer_class=CategoriaServicioSerializers)),
    path('categoriaservicio_api/<int:pk>',GetGeneral.as_view(model =CategoriaServicio,serializer_class=CategoriaServicioSerializers)),

    path('solicitud/',PostSolicitud.as_view()),


]



