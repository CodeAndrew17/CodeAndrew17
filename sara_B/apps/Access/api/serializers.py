from rest_framework import serializers,generics
from apps.Access.models import Convenios,Sucursales,Empleados,Usuarios

class ConveniosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Convenios
        fields= '__all__'

class SucursalesSeralizers(serializers.ModelSerializer):
    class Meta:
        model=Sucursales
        fields= '__all__'

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields='__all__'

class EmpleadosSerialzers(serializers.ModelSerializer):
    class Meta:
        model=Empleados
        fields='__all__'


