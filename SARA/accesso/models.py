from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password,check_password

class Estado(models.TextChoices):
    ACTIVO = 'AC', 'Activo'
    INACTIVO = 'IN', 'Inactivo'

Errores={'unique': 'Este nombre de usuario  en uso.',
        'blank': 'El campo usuario no puede estar vacío.',
        'max_length': 'El nombre de usuario no puede tener más de 100 caracteres.',
        }

class Convenios(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    nit = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.ACTIVO)

    def __str__(self):
        return self.nombre

class Sucursales(models.Model):
    nombre=models.CharField(max_length=100)
    ciudad=models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    estado= models.CharField(max_length=2,choices=Estado.choices, default=Estado.ACTIVO)
    convenio= models.ForeignKey(Convenios, on_delete=models.CASCADE,null=False)

    class Meta:
        ordering= ['-nombre']

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombres= models.CharField(max_length=100, error_messages=Errores  )
    apellidos=models.CharField(max_length=100)
    cedula= models.IntegerField(unique=True,error_messages=Errores)
    correo= models.EmailField(max_length=50,unique=True)
    estado= models.CharField(max_length=2,choices=Estado.choices, default=Estado.ACTIVO)
    id_sucursal= models.ForeignKey(Sucursales, on_delete= models.CASCADE)

    def __int(self):
        return self.cedula

class Usuarios(models.Model):

    class Roles(models.TextChoices):
        administrador= 'AD',"Adminitrador"
        perito='PR', 'Perito'
        recepcionista='RC','Recepcionista'
        adconvenio='CA','Administardor Convenio'
        convenioc='CC','Consultor Convenio'

    usuario=models.CharField(max_length=100,unique=True)
    contraseña= models.CharField(max_length=150)
    rol= models.CharField(max_length=2,choices=Roles.choices)
    estado=models.CharField(max_length=2,choices=Estado.choices,default=Estado.ACTIVO)
    id_empleado= models.ForeignKey(Empleados,on_delete= models.CASCADE)
#funcion para encriptar contraseña 
    def save(self, *args, **kwargs):
        if not self.pk: 
            self.contraseña = make_password(self.contraseña)
        super(Usuarios, self).save(*args, **kwargs)
    def Verificar_contraseña(self,contarseña_pana):
        return check_password(contarseña_pana,self.contraseña)

    def __str__(self):
        return self.usuario
# Create your models here.
