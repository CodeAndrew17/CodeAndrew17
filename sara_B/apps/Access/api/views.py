from rest_framework.views import APIView
from rest_framework import status,generics
from apps.Access.api.serializers import UsuarioSerializers,RestablecerPasswordSerializers
from apps.Access.models import Usuario,Empleado
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from ...Seguridad.Permisos import RolePermission
from apps.Seguridad.Permisos import RolePermission
from rest_framework.permissions import IsAuthenticated


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

        usuario = request.data.get('usuario')
        password = request.data.get('password')

        if not usuario or not password:
            return Response({'error':'usuario y contarseña Requeridos'})
        
        user=get_object_or_404(Usuario,usuario=request.data['usuario'])
        
        if user.estado == 'AC':
            if not user.Verificar_contraseña(request.data['password']):
                return Response({'error':'Contraseña Erronea'})
            token, created= Token.objects.get_or_create(user=user)
            serialiizers= UsuarioSerializers(instance=user)
            return Response({'token':token.key,'usuario':serialiizers.data['usuario']}, status.HTTP_200_OK)
        else:
            return Response({'error' :'Usuario inactivo. Contactar con el administrador de SARA'}, status=status.HTTP_403_FORBIDDEN)


class RestablecerPassword(generics.GenericAPIView):
    serializer_class = RestablecerPasswordSerializers

    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            correo_empleado= Empleado.objects.filter(correo=correo_empleado).exists()
            if correo_empleado:
                pass

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        