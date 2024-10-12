from rest_framework import serializers
from apps.Solicitudes.models import Solicitud, Empleado, CategoriaServicio


class SolicitudSerializers(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class CategoriaServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServicio
        fields = '__all__'
