from rest_framework import serializers
import re

pattern = r'^[\d-]+$' # Solo numeros y guio para el NIT


"""
Ejemplo una exprexion regular de usos de los Verificiaion de terminos para las validacions Estudialar
pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'
if not re.fullmatch(pattern, data):
raise ValidationError("El número de teléfono no es válido")
    return data

"""

r'^\+?\d{1,9}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'

def validaciones_positive(value):
    if value <= 0:
        raise serializers.ValidationError("Los campos no pueden pueden Ser negativos")
    return value

def logitud_minima(value):
    if len(value) < 5:
        raise serializers.ValidationError("debe tener mas caracteres")
    return value