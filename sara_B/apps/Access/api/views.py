from rest_framework.views import APIView
from rest_framework import generics,status
from apps.Access.api.serializers import UsuarioSerializers
from apps.Access.models import Usuario
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from .Permisos import RolePermission
from rest_framework.permissions import IsAuthenticated


#Api General para la creaacion y visualizacion de los objetos segun el model Selcionado Dinamicamnete en la URL
class SEF_POST_General(generics.GenericAPIView):
    serializer_class=None
    model=None
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, RolePermission]
    allowed_roles = ['AD','CA'] 
    """
    #Realiza el llamado del  ultimo objeto Creado
    def get_queryset(self):
        return self.model.objects.all()

    #Realia  el listado de todos los objetos Creados en el Model
    def get(self,request):
        try:
            modelos= self.model.objects.all()
            model_serializers=self.serializer_class(modelos,many=True)
            return Response(model_serializers.data,status=status.HTTP_200_OK )
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_503_SERVICE_UNAVAILABLE)

    #Realiza la Creacion de un nuevo objetos Segun las validaciones y Model correspondiente 

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            objeto = serializers.save()
            if isinstance(objeto, Usuario):
                token, created = Token.objects.get_or_create(user=objeto)
                return Response({'token': token.key, **serializers.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Api General para la Actualizacion y eliminacion de objetos Segun el model Selcionado dinamicamente el URl
class PUT_DELETE_General(generics.GenericAPIView):
    serializer_class= None
    model= None
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, RolePermission]
    allowed_roles = ['AD','CA'] 
    """

    # Realiza el llamado y verificacion que la PK sea correcta
    def get_object(self, pk):
        try:
            return self.model.objects.get(id=pk)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # Llama al Objetos despues de la Validacion  
    def get(self, resquest,pk):
        try:
            modelos= self.get_object(pk)
            model_serializers=self.serializer_class(modelos)
            return Response(model_serializers.data,status=status.HTTP_200_OK )
        except self.model.DoesNotExist:
            raise NotFound(detail="Objeto no encontrado.", code=404)
        except:
            return Response(modelos.errors,status=status.HTTP_400_BAD_REQUEST) 

    # Realiza la revision de los  nuevos datos para el objeto y realiza la actualizacion
    def put(self,request,pk):
        try:
            modelos=self.get_object(pk)
            model_serializars=self.serializer_class(modelos,data=request.data)
            if model_serializars.is_valid():
                model_serializars.save()
                return Response(model_serializars.data, status=status.HTTP_200_OK)
        except self.model.DoesNotExist:
            return Response(model_serializars.errors,status=status.HTTP_400_BAD_REQUEST)

    #Realiza la eliminacion del objetos indicado.
    def delete(self,request,pk):
        try:
            modelos= self.get_object(pk)
            modelos.delete()
            return Response({"detail": "Eliminado"}, status=status.HTTP_204_NO_CONTENT)
        except self.model.DoesNotExist:
            return Response({"detail": "Objeto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

#Clase para realiza la Creacion del usuarios con la asignacion de toekn para verificaicon      
class CreateUser(APIView):
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, RolePermission]
    allowed_roles = ['AD','CA'] 
    """
    model = Usuario
    serializer_class = UsuarioSerializers

    def get(self, request):
        usuario = self.model.objects.all()
        serializers = self.serializer_class(usuario, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            objet = serializers.save()
            if isinstance(objet, Usuario):
                token, created = Token.objects.get_or_create(user=objet)
                return Response({'token': token.key, **serializers.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# clase que hace la verificacion de Credenciales y trae el token del usuario correspodiente 
class login(APIView):

    def post(self,request):
        user=get_object_or_404(Usuario,usuario=request.data['usuario'])

        if not user.Verificar_contraseña(request.data['password']):
            return Response({'error':'invalid password '})
        token, created= Token.objects.get_or_create(user=user)
        serialiizers= UsuarioSerializers(instance=user)
        return Response({'token':token.key,'usuario':serialiizers.data}, status.HTTP_200_OK)