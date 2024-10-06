from rest_framework import serializers,generics
from apps.Access.models import Convenio,Sucursal,Empleado,Usuario
from .Validaciones import logitud_minima,validaciones_positive

class ConvenioSerializers(serializers.ModelSerializer):
    class Meta:
        model=Convenio
        fields= '__all__'

    def validate_telefono(self, value):
        return validaciones_positive(value)

    def validate_nit(self, value):
        return logitud_minima(value)

class SucursalSeralizers(serializers.ModelSerializer):
    class Meta:
        model=Sucursal
        fields= '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        exclude=['is_active','is_staff','is_superuser','last_login']
    
    
class EmpleadoSerialzers(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields='__all__'


