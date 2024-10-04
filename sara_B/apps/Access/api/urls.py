from django.urls import path
from apps.Access.models import Convenio,Sucursal,Empleado,Usuario
from apps.Access.api.serializers import ConvenioSerializers, SucursalSeralizers,EmpleadoSerialzers,UsuarioSerializers
from apps.Access.api.views import SEF_POST_General,PUT_DELETE_General

urlpatterns=[
    path('convenios_api/',SEF_POST_General.as_view(model=Convenio,serializer_class=ConvenioSerializers)),
    path('convenios_api/<int:pk>',PUT_DELETE_General.as_view(model=Convenio,serializer_class=ConvenioSerializers)),

    path('Sucursales_api/',SEF_POST_General.as_view(model=Sucursal,serializer_class=SucursalSeralizers)), 
    path('Sucursales_api/<int:pk>',PUT_DELETE_General.as_view(model=Sucursal,serializer_class=SucursalSeralizers)),

    path('empleados_api/',SEF_POST_General.as_view(model=Empleado,serializer_class=EmpleadoSerialzers)),
    path('empleados_api/<int:pk>',PUT_DELETE_General.as_view(model=Empleado,serializer_class=EmpleadoSerialzers)),

    path('usuario_api/',SEF_POST_General.as_view(model=Usuario,serializer_class=UsuarioSerializers)),
    path('usuario_api/<int:pk>',PUT_DELETE_General.as_view(model=Usuario,serializer_class=UsuarioSerializers)),
    
]