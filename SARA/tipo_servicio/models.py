from django.db import models
from django_mysql.models import EnumField
from django.db.models import ImageField

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    id_pmv  = models.ForeignKey('PMV', on_delete=models.CASCADE)
    id_pmc = models.ForeignKey('PMC',on_delete=models.CASCADE)
    id_novedades = models.ForeignKey('Novedades',on_delete=models.CASCADE)
    id_improntas = models.ForeignKey('Improntas',on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 
    

class PMV(models.Model):
    nombre = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre    


class PMC(models.Model):
    n_cilindro = models.CharField(max_length=100) 
    resultado = models.CharField(max_length=100)

    def __str__(self):
        return self.n_cilindro



class Novedades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre 


class Improntas(models.Model):
    ESTADO_CHOICES=[ 
    ('original', 'Original'),
    ('regrabado', 'Regrabado'),
    ('grabado', 'Grabado'),
    ('no_aplica', 'No Aplica')
    ]
    nombre = models.CharField(max_length=100)
    estado = EnumField(choices=ESTADO_CHOICES)
    fotos = models.ImageField(upload_to='fotos/')
    observaciones = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre 


