from django.urls import path
from apps.Access.models import Convenio,Sucursal,Empleado,Usuario
from apps.Access.api.serializers import ConvenioSerializers, SucursalSeralizers,EmpleadoSerialzers,UsuarioSerializers
from apps.Access.api.views import CreateUser,Login,SolicitudRestablecerPass,ContraseñaRestablecida
from apps.Seguridad.CRUD import GetGeneral,PUT_DELETE_General,PostGeneral

urlpatterns=[
    path('convenio_api/',GetGeneral.as_view(model=Convenio,serializer_class=ConvenioSerializers)),
    path('convenio_api/<int:pk>',PUT_DELETE_General.as_view(model=Convenio,serializer_class=ConvenioSerializers)),
    path('convenio/',PostGeneral.as_view(model=Convenio,serializer_class=ConvenioSerializers)),

    path('Sucursal_api/',GetGeneral.as_view(model=Sucursal,serializer_class=SucursalSeralizers)), 
    path('Sucursal_api/<int:pk>',PUT_DELETE_General.as_view(model=Sucursal,serializer_class=SucursalSeralizers)),
    path('sucursal/',PostGeneral.as_view(model=Sucursal,serializer_class=SucursalSeralizers)),

    path('empleado_api/',GetGeneral.as_view(model=Empleado,serializer_class=EmpleadoSerialzers)),
    path('empleado_api/<int:pk>',PUT_DELETE_General.as_view(model=Empleado,serializer_class=EmpleadoSerialzers)),
    path('empleado/',PostGeneral.as_view(model=Empleado,serializer_class=EmpleadoSerialzers)),

    path('usuario_api/',GetGeneral.as_view(model=Usuario,serializer_class=UsuarioSerializers)),
    path('usuario/',CreateUser.as_view()),
    path('usuario_api/<int:pk>',PUT_DELETE_General.as_view(model=Usuario,serializer_class=UsuarioSerializers)),

    path('login/',Login.as_view()),

    path('solicitarpassword/', SolicitudRestablecerPass.as_view()),
    path('restablecerpassword/<uidb64>/<token>',ContraseñaRestablecida.as_view())
  
]