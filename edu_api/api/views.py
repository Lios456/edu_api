import base64
from .encript_utils import decrypt_ci4
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .permissions import UsuarioActivoOPariente
from rest_framework import viewsets, filters
from .middleware import ParienteJWTAuthentication
from rest_framework.permissions import AllowAny


BASE_KEY = b"Edu4trol@.#"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = [AllowAny]
    def validate(self, attrs):
        print(f"Datos recibidos en serializer: {attrs}")
        
        username = attrs.get("usuario")
        password = attrs.get("password")
        
        try:
            # Se asume que el campo para identificar al usuario es 'usuario'
            usuario = Usuario.objects.get(usuario=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Credenciales inválidas")
        
        try:
            # Se asume que la contraseña cifrada se guarda en 'clave' en base64
            stored_encrypted = base64.b64decode(usuario.clave)
            decrypted_password = decrypt_ci4(stored_encrypted, BASE_KEY, raw_data=True).decode("utf-8")
        except Exception as e:
            raise serializers.ValidationError("Error en la verificación de credenciales")
        
        if decrypted_password != password:
            raise serializers.ValidationError("Credenciales inválidas")
        
        # Asignamos el usuario y generamos el token
        self.user = usuario
        refresh = self.get_token(self.user)
        # Forzamos que el token incluya el identificador correcto
        refresh['user_id'] = str(self.user.pk)
        
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# Usuarios
class UsuarioDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            usuario = request.user
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Parientes
class RepresentadosView(APIView):
    permission_classes = [UsuarioActivoOPariente]

    def get(self, request, id_pariente=None):
        if id_pariente:
            try:
                representados = AlumnoPariente.objects.filter(pariente_id=id_pariente)
                serializer = AlumnoParienteSerializer(representados, many=True)
                return Response(serializer.data)
            except AlumnoPariente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "No se ha especificado un ID de pariente"}, status=status.HTTP_400_BAD_REQUEST)

class DetalleEstudianteView(APIView):
    permission_classes = [UsuarioActivoOPariente]

    def get(self, request, id_estudiante):
        try:
            estudiante = Alumno.objects.get(pk=id_estudiante)
            serializer = AlumnoSerializer(estudiante)
            return Response(serializer.data)
        except Alumno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Tutores
class PeriodosView(APIView):
    authentication_classes = [JWTAuthentication, ParienteJWTAuthentication]
    permission_classes = [UsuarioActivoOPariente]  # Changed from AllowAny

    def get(self, request):
        periodos = PeriodoAcademico.objects.filter(activo='S').order_by('-id')
        serializer = PeriodoAcademicoSerializer(periodos, many=True)
        return Response(serializer.data)

class CursosView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id_periodo):
        paralelos = Paralelo.objects.filter(curso__seccion__periodo_academico__id=id_periodo)
        paralelos = ParaleloSerializer(paralelos, many=True)
        return Response(paralelos.data)

class EstudiantesCursoView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id_curso):
        
        estudiantes = Alumno.objects.filter(matricula__paralelo__id=id_curso).order_by('apellido')
        serializer = AlumnoSerializer(estudiantes, many=True)
        return Response(serializer.data)

class AtrasosView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AsistenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id_atraso=None):
        if id_atraso:
            try:
                atraso = Asistencia.objects.get(pk=id_atraso)
                serializer = AsistenciaSerializer(atraso)
                return Response(serializer.data)
            except Asistencia.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            atrasos = Asistencia.objects.all()
            serializer = AsistenciaSerializer(atrasos, many=True)
            return Response(serializer.data)

    def delete(self, request, id_atraso):
        try:
            atraso = Asistencia.objects.get(pk=id_atraso)
            atraso.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Asistencia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Notificaciones
class NotificacionesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notificaciones = Notificacion.objects.all()
        serializer = NotificacionSerializer(notificaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NotificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificacionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            notificacion = Notificacion.objects.get(pk=id)
            serializer = NotificacionSerializer(notificacion)
            return Response(serializer.data)
        except Notificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            notificacion = Notificacion.objects.get(pk=id)
            serializer = NotificacionSerializer(notificacion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Notificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            notificacion = Notificacion.objects.get(pk=id)
            notificacion.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Notificacion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
"""
Atrasos
"""

class AtrasoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = AtrasoSerializer
    
    queryset = Atraso.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return AtrasoCreateSerializer
        return AtrasoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class ParaleloViewSet(APIView):
    permission_classes = [UsuarioActivoOPariente]
    serializer_class = ParaleloSerializer
    
    def get(self, request):
        paralelos = Paralelo.objects.all()
        serializer = ParaleloSerializer(paralelos, many=True)
        return Response(serializer.data)

"""
Parientes
"""    

class ParienteLoginView(APIView):
    def post(self, request):
        serializer = ParienteLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    