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
        


class CrearEmpleadoUsuarioView(APIView):
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
        # Extraer datos del request
        empleado_data = request.data.get('empleado')
        usuario_data = request.data.get('usuario')

        if not empleado_data or not usuario_data:
            return Response(
                {'error': 'Se requieren tanto los datos de empleado como de usuario.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validar y crear Empleado
        empleado_serializer = EmpleadosSerialzers(data=empleado_data)

        if empleado_serializer.is_valid():
            empleado = empleado_serializer.save()
            usuario_serializer = UsuariosSerializers(data=usuario_data)
            if usuario_serializer.is_valid():
                usuario = usuario_serializer.save(empleado=empleado)  # Relacionamos empleado con usuario

                return Response(
                    {
                        'empleado': EmpleadosSerialzers(empleado).data,
                        'usuario': UsuariosSerializers(usuario).data
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Retornar errores de validación
            errores = {
                'empleado': empleado_serializer.errors,
                'usuario': usuario_serializer.errors if 'usuario_serializer' in locals() else {}
            }
            return Response(errores, status=status.HTTP_400_BAD_REQUEST)