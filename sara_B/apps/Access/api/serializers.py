from rest_framework import serializers,generics
from apps.Access.models import Convenios,Sucursales,Empleados,Usuarios
from .Validaciones import logitud_minima,validaciones_positive

class ConveniosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Convenios
        fields= '__all__'

    def validate_telefono(self, value):
        return validaciones_positive(value)

    def validate_nit(self, value):
        return logitud_minima(value)

class SucursalesSeralizers(serializers.ModelSerializer):
    class Meta:
        model=Sucursales
        fields= '__all__'

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields= '__all__'
    
    

class EmpleadosSerialzers(serializers.ModelSerializer):
    class Meta:
        model=Empleados
        fields='__all__'


