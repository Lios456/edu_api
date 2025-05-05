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
from .permissions import *
from rest_framework import viewsets, filters
from .middleware import ParienteJWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from .utils import create_jwt_tokens
from django.contrib.auth import authenticate
from .authentication import CustomJWTAuthentication



BASE_KEY = b"Edu4trol@.#"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = [AllowAny]
    
    def validate(self, attrs):
        print(f"Datos recibidos en serializer: {attrs}")
        
        username = attrs.get("usuario")
        password = attrs.get("password")
        
        try:
            usuario = Usuario.objects.get(usuario=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Credenciales inválidas")
        
        try:
            stored_encrypted = base64.b64decode(usuario.clave)
            decrypted_password = decrypt_ci4(stored_encrypted, BASE_KEY, raw_data=True).decode("utf-8")
        except Exception as e:
            raise serializers.ValidationError("Error en la verificación de credenciales")
        
        if decrypted_password != password:
            raise serializers.ValidationError("Credenciales inválidas")
        
        # Asignamos el usuario y generamos el token
        self.user = usuario
        # After successful validation
        refresh = self.get_token(self.user)
        
        # Add standard claims expected by authentication
        refresh['user_id'] = str(self.user.pk)
        refresh['user_type'] = 'usuario'
        refresh.access_token['user_type'] = 'usuario'

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# ============================== USUARIOS ==============================
class UsuarioDetailView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            usuario = request.user
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ============================== PARIENTES ==============================
class RepresentadosView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_pariente=None):
        if id_pariente:
            try:
                alumnos = []
                representados = AlumnoPariente.objects.filter(pariente_id=id_pariente)
                for representado in representados:
                    alumno = Alumno.objects.get(pk=representado.alumno_id)
                    alumnos.append(alumno)
                serializer = AlumnoSerializer(alumnos, many=True)
                return Response(serializer.data)
            except AlumnoPariente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "No se ha especificado un ID de pariente"}, status=status.HTTP_400_BAD_REQUEST)

class DetalleEstudianteView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_estudiante):
        try:
            estudiante = Alumno.objects.get(pk=id_estudiante)
            serializer = AlumnoSerializer(estudiante)
            return Response(serializer.data)
        except Alumno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ParienteLoginView(APIView):
    authentication_classes = []  # Disable default authentication
    permission_classes = [AllowAny]  # Add this line

    def post(self, request):
        numero_identificacion = request.data.get('numero_identificacion')
        password = request.data.get('password')
        
        user = authenticate(
            request,
            username=numero_identificacion,
            password=password,
            backend='api.backends.ParienteAuthBackend'
        )
        
        if user and isinstance(user, Pariente):
            tokens = create_jwt_tokens(user)
            return Response(tokens)
        return Response({'error': 'Credenciales inválidas'}, status=400)
    
class HorarioEstudianteView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_estudiante):
        try:
            periodo_activo = PeriodoAcademico.objects.get(activo_pariente='S')
            matricula = Matricula.objects.get(alumno_id=id_estudiante, periodo_academico=periodo_activo)
            if not matricula:
                return Response({"message": "El estudiante no tiene una matricula asignada"}, status=status.HTTP_400_BAD_REQUEST)
            
            if not matricula.paralelo:
                return Response({"message": "El estudiante no tiene un paralelo asignado"}, status=status.HTTP_400_BAD_REQUEST)
            
            paralelo = matricula.paralelo
            
            materias = []
            
            paralelo_materia_profesor = ParaleloMateriaProfesor.objects.filter(paralelo_id=paralelo.id)
            
            for pm in paralelo_materia_profesor:
                materia = pm.materia
                if materias.count(materia) == 0:
                    materias.append(materia)
            
            serializer = MateriaSerializer(materias, many=True)
            return Response(serializer.data)
        except Horario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

# ============================== INSPECTOR ==============================
class PeriodosView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        periodos = PeriodoAcademico.objects.order_by('-id')
        serializer = PeriodoAcademicoSerializer(periodos, many=True)
        return Response(serializer.data)

class UsuarioDetailView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            usuario = request.user
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CursosView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_periodo):
        paralelos = Paralelo.objects.filter(curso__seccion__periodo_academico__id=id_periodo)
        paralelos = ParaleloSerializer(paralelos, many=True)
        return Response(paralelos.data)

class EstudiantesCursoView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_curso):
        
        estudiantes = Alumno.objects.filter(matricula__paralelo__id=id_curso).order_by('apellido')
        serializer = AlumnoSerializer(estudiantes, many=True)
        return Response(serializer.data)

class AtrasosView(APIView):
    authentication_classes = [CustomJWTAuthentication]
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


# ============================== NOTIFICACIONES ==============================
class NotificacionesView(APIView):
    authentication_classes = [CustomJWTAuthentication]
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
    authentication_classes = [CustomJWTAuthentication]
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
        
# ============================== ATRASOS ==============================
class AtrasoViewSet(viewsets.ModelViewSet):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = AtrasoSerializer
    
    queryset = Atraso.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return AtrasoCreateSerializer
        return AtrasoSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class ParaleloViewSet(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ParaleloSerializer
    
    def get(self, request):
        paralelos = Paralelo.objects.all()
        serializer = ParaleloSerializer(paralelos, many=True)
        return Response(serializer.data)

# ============================== NOTAS ==============================
class NotasAlumnoView(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_alumno, id_periodo=None):
        """
        Obtiene las notas de un alumno para un periodo académico específico.
        Si no se especifica el periodo, devuelve las notas de todos los periodos.
        """
        try:
            # Verificar que el alumno existe
            alumno = Alumno.objects.get(pk=id_alumno)
            
            # Filtrar notas por alumno y opcionalmente por periodo
            if id_periodo:
                notas = Nota.objects.filter(
                    alumno_id=id_alumno,
                    periodo_academico_id=id_periodo
                ).select_related('paralelo_materia_profesor__materia')
            else:
                notas = Nota.objects.filter(
                    alumno_id=id_alumno
                ).select_related('paralelo_materia_profesor__materia')
            
            # Serializar los resultados
            serializer = NotaSerializer(notas, many=True)
            return Response(serializer.data)
            
        except Alumno.DoesNotExist:
            return Response(
                {"error": "Estudiante no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
  


    
    