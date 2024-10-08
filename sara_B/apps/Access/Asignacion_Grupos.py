from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import  Group,Permission
from .models import Usuario

"""
# 1. Crear el grupo si no existe
grupo, created = Group.objects.get_or_create(name='Grupo_Gerentes')

# 2. Asignar permisos (opcional)
# Obtener los permisos necesarios, por ejemplo, permiso para agregar empleados
permiso_agregar = Permission.objects.get(codename='add_empleado')
permiso_editar = Permission.objects.get(codename='change_empleado')

# Asignar permisos al grupo
grupo.permissions.add(permiso_agregar, permiso_editar

"""
    

@receiver(post_save, sender=Usuario)
def AgregarGrupo(sender,instance,created, **karkwargs):
    if created:
        match instance.rol:
            case 'AD': #administrador
                grupo = Group.objects.get(name='Administrador')  # Obtiene el grupo
                instance.groups.add(grupo)  
            case 'PR': #perito
                grupo = Group.objects.get(name='Perito')  # Obtiene el grupo
                instance.groups.add(grupo) 
            case 'RC':#recepcionista
                grupo = Group.objects.get(name='Recepcionista')  # Obtiene el grupo
                instance.groups.add(grupo)  
            case 'CA':#Administardor Convenio
                grupo = Group.objects.get(name='AdministradorConvenio')  # Obtiene el grupo
                instance.groups.add(grupo)  
            case 'CC':#Consultor Convenio
                grupo = Group.objects.get(name='ConsultorConvenio')  # Obtiene el grupo
                instance.groups.add(grupo)  



