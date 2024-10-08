from rest_framework import serializers,generics
from apps.Access.models import Convenio,Sucursal,Empleado,Usuario
from .Validaciones import logitud_minima,validate_positive,validate_number,validate_text
from django.contrib.auth.models import Group,Permission



class ConvenioSerializers(serializers.ModelSerializer):
    class Meta:
        model=Convenio
        fields= '__all__'

    def validate_telefono(self, value):
        return validate_positive(value)

    def validate_nit(self, value):
        if logitud_minima(value):
            return validate_number(value)

class SucursalSeralizers(serializers.ModelSerializer):
    class Meta:
        model=Sucursal
        fields= '__all__'

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        exclude=['is_active','is_staff','is_superuser','last_login']
        
    def validate_usuario(self, value):
        if logitud_minima(value):
            return validate_text(value)


class EmpleadoSerialzers(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields='__all__'


