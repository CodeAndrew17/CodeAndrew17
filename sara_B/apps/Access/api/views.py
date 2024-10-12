from rest_framework.views import APIView
from rest_framework import status
from apps.Access.api.serializers import UsuarioSerializers
from apps.Access.models import Usuario
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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
        user=get_object_or_404(Usuario,usuario=request.data['usuario'])

        if not user.Verificar_contraseña(request.data['password']):
            return Response({'error':'invalid password '})
        token, created= Token.objects.get_or_create(user=user)
        serialiizers= UsuarioSerializers(instance=user)
        return Response({'token':token.key,'usuario':serialiizers.data}, status.HTTP_200_OK)