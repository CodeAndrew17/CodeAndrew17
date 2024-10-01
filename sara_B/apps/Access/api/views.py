from rest_framework.views import APIView
from rest_framework import generics,status
from apps.Access.api.serializers import EmpleadosSerialzers,UsuariosSerializers
from apps.Access.models import Empleados, Usuarios
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

"""
class ConvenioAPIViws(APIView):

    def get(self,request):
        convenios= Convenios.objects.all()
        Convenios_serialixers= ConveniosSerializers(convenios,many=True)
        return Response(Convenios_serialixers.data)
"""

class GeneralCrear_listar(generics.GenericAPIView):
    serializer_class=None
    model=None
    
    def get_queryset(self):
        return self.model.objects.all()

    def get(self,request):
        try:
            modelos= self.model.objects.all()
            model_serializers=self.serializer_class(modelos,many=True)
            return Response(model_serializers.data,status=status.HTTP_200_OK )
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_503_SERVICE_UNAVAILABLE)


    def post(self,resquest):
        modelos=self.serializer_class(data=resquest.data)
        if modelos.is_valid():
            modelos.save()
            return Response(modelos.data,status=status.HTTP_200_OK)
        return Response(modelos.errors,status=status.HTTP_400_BAD_REQUEST)
        

class General_eliminar_modificiar(generics.GenericAPIView):
    serializer_class= None
    model= None

    def get_object(self, pk):
        """Helper method to get the object."""
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, resquest,pk):
        try:
            modelos= self.get_object(pk)
            model_serializers=self.serializer_class(modelos)
            return Response(model_serializers.data,status=status.HTTP_200_OK )
        except self.model.DoesNotExist:
            raise NotFound(detail="Objeto no encontrado.", code=404)
        except:
            return Response(self.modelos.errors,status=status.HTTP_400_BAD_REQUEST) 
        
    def put(self,request,pk):
        modelos=self.get_object(pk)
        model_serializars=self.serializer_class(modelos,data=request.data)
        if model_serializars.is_valid():
            model_serializars.save()
            return Response(model_serializars.data, status=status.HTTP_200_OK)
        return Response(model_serializars.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            modelos= self.get_object(pk)
            modelos.delete()
            return Response({"detail": "Eliminado"}, status=status.HTTP_204_NO_CONTENT)
        except self.model.DoesNotExist:
            return Response({"detail": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
""""
class EmpleadosUsuarios(generics.GenericAPIView):
    model = Empleados
    serializer_class = EmpleadosSerialzers

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request):
        try:
            modelos = self.model.objects.all()
            model_serializers = self.serializer_class(modelos, many=True)
            return Response(model_serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, request):
        # Serializar los datos del empleado
        empleado_serializer = self.serializer_class(data=request.data)
        if empleado_serializer.is_valid():
            empleado = empleado_serializer.save()

            usuario_data = {'id_empleado': empleado.id}
            
            usuario_serializer = UsuariosSerializers(data=usuario_data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response({'message': 'Empleado and usuario created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class RegistrarUsuarios(APIView):
    model = Empleados
    serializer_class = EmpleadosSerialzers

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request):
        try:
            modelos = self.model.objects.all()
            model_serializers = self.serializer_class(modelos, many=True)
            return Response(model_serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    def post(self, request):
        usuario_serializer = UsuariosSerializers(data=request.data)
        if usuario_serializer.is_valid():
            empleado_serializer = EmpleadosSerialzers(data=request.data)
            if empleado_serializer.is_valid():
                empleado = empleado_serializer.save()
                usuario = usuario_serializer.save(commit=False)
                usuario.id_empleado = Empleados.objects.order_by('-id').first()
                usuario.save()
                return Response({'empleado': empleado_serializer.data, 'usuario': usuario_serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmpleadosUsuarios(generics.CreateAPIView):
    model = Empleados
    serializer_class = EmpleadosSerialzers

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request):
        try:
            modelos = self.model.objects.all()
            model_serializers = self.serializer_class(modelos, many=True)
            return Response(model_serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    def post(self, request):
        # Serializar los datos del empleado
        empleado_serializer = EmpleadosSerialzers(data=request.data)
        
        if empleado_serializer.is_valid():
            # Guardar el empleado
            empleado = empleado_serializer.save()

            # Crear una copia de los datos del request para el usuario
            usuario_data = request.data.copy()
            # Añadir el ID del empleado al diccionario de datos del usuario
            usuario_data['id_empleado'] =  Empleados.objects.order_by('-id').first()


            # Serializar los datos del usuario con la referencia al empleado creado
            usuario_serializer = UsuariosSerializers(data=usuario_data)
            
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(
                    {
                        'empleado': empleado_serializer.data,
                        'usuario': usuario_serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                # Si hay un error con el usuario, eliminar el empleado creado
                empleado.delete()
                return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Si los datos del empleado no son válidos
        return Response(empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
