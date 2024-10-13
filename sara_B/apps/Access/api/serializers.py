from rest_framework import serializers
from apps.Access.models import Convenio,Sucursal,Empleado,Usuario
from .Validaciones import logitud_minima,validate_positive,validate_number,validate_text

class ConvenioSerializers(serializers.ModelSerializer):
    class Meta:
        model=Convenio
        fields= '__all__'
    # Funciones que hacen validacion de Cada campo 
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


class RestablecerPasswordSerializers(serializers.Serializer):
    correo = serializers.EmailField(max_length=100)
    class Meta:
        fields= ['correo']

        