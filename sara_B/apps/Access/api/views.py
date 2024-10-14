from rest_framework.views import APIView
from rest_framework import status,generics
from apps.Access.api.serializers import UsuarioSerializers,SolicitudRestablecerPassSerializers,RestablecerPasswordSerializers
from apps.Access.models import Usuario
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
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
            return Response({'error':'usuario y contarseña Requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        
        user=get_object_or_404(Usuario,usuario=request.data['usuario'])
        
        if user.estado == 'AC':
            if not user.Verificar_contraseña(request.data['password']):
                return Response({'error':'Contraseña Erronea'}, status=status.HTTP_401_UNAUTHORIZED)
            token, created= Token.objects.get_or_create(user=user)
            serialiizers= UsuarioSerializers(instance=user)
            return Response({'token':token.key,'usuario':serialiizers.data['usuario']}, status.HTTP_200_OK)
        else:
            return Response({'error' :'Usuario inactivo. Contactar con el administrador de SARA'}, status=status.HTTP_403_FORBIDDEN)

#Se realiza el envio de la dirrecion para restablecer contraseña
class SolicitudRestablecerPass(generics.GenericAPIView):
    serializer_class = SolicitudRestablecerPassSerializers

    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            try:
                correo = serializer.validated_data['correo']
                usuario = serializer.validated_data['usuario']

                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(usuario)
                uid = urlsafe_base64_encode(force_bytes(usuario.pk))
                reset_link = f"http://127.0.0.1:8000/access/restablecerpassword/{uid}/{token}/"

                send_mail('Restablecer Contarseña SARA',f'link de restablecimineto  {reset_link}',None, [correo])
                return Response({'message':'Se realizo el envio correo para el restablecimiento de contarseña'}, status=status.HTTP_200_OK)
            except Exception as e:
                error = str(e)
                return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Serealiza el cambio de contarseña 
class ContraseñaRestablecida(APIView):
    serializer_class =RestablecerPasswordSerializers
    
    def post(self, request, uidb64, token):
        print("UIDB64:", uidb64)
        print("token: ",token)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(uid=uidb64, token=token)
                return Response({'msg': 'Contraseña restablecida correctamente'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)