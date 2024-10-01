from django.urls import path
from apps.Access.models import Convenios,Sucursales,Empleados,Usuarios
from apps.Access.api.serializers import ConveniosSerializers, SucursalesSeralizers,EmpleadosSerialzers
from apps.Access.api.views import GeneralCrear_listar,General_eliminar_modificiar,CrearEmpleadoUsuarioView,EmpleadosUsuarios

urlpatterns=[
    path('convenios_api/',GeneralCrear_listar.as_view(model=Convenios,serializer_class=ConveniosSerializers)),
    path('Sucursales_api',GeneralCrear_listar.as_view(model=Sucursales,serializer_class=SucursalesSeralizers)),
    path('convenios_api/<int:pk>',General_eliminar_modificiar.as_view(model=Convenios,serializer_class=ConveniosSerializers)),
    path('empleados_api/',CrearEmpleadoUsuarioView.as_view()),
]