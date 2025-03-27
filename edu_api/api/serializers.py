from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id','nombre','nacionalidad']
        depth = 1

class ProvinciaSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()
    class Meta:
        model = Provincia
        fields = ['id','nombre','pais']
        depth = 3

class CiudadSerializer(serializers.ModelSerializer):
    provincia = ProvinciaSerializer()
    class Meta:
        model = Ciudad
        fields = ['id','nombre','provincia']
        depth = 1

class ParroquiaSerializer(serializers.ModelSerializer):
    ciudad = CiudadSerializer()
    class Meta:
        ciudad = CiudadSerializer()
        model = Parroquia
        fields = ['id','nombre','ciudad']
        depth = 1

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = '__all__'
        depth = 1

class RutaEvacuacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutaEvacuacion
        fields = '__all__'
        depth = 1

class AlumnoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()
    provincia = ProvinciaSerializer()
    ciudad = CiudadSerializer()
    parroquia = ParroquiaSerializer()
    
    class Meta:
        model = Alumno
        fields = ['id','nombre','apellido',
                  'genero','codigo','estado',
                  'lugar_nacimiento','nacionalidad','fecha_nacimiento',
                  'numero_identificacion','telefono_celular','email',
                  'foto','tipo_sangre','calle_principal','calle_secundaria',
                  'pais','provincia','ciudad','parroquia','religion',
                  ]
        depth = 2

class AlumnoParienteSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer()
    class Meta:
        model = AlumnoPariente
        fields = ['id', 'alumno', 'pariente']
        depth = 2

class AmbitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambito
        fields = '__all__'
        depth = 2

class AmbitoProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbitoProfesor
        fields = '__all__'
        depth = 2

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','nombre']
        depth = 2

class AseguradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aseguradora
        fields = '__all__'
        depth = 1

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'
        depth = 2

class AsistenciaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaPersonal
        fields = '__all__'
        depth = 2

class AsistenciaTrimestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsistenciaTrimestre
        fields = '__all__'
        depth = 2

class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = '__all__'
        depth = 1

class AulaParaleloSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaParalelo
        fields = '__all__'
        depth = 2

class BajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baja
        fields = '__all__'
        depth = 1

class BloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque
        fields = '__all__'
        depth = 1

class BloqueParaleloFechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloqueParaleloFecha
        fields = '__all__'
        depth = 2

class BloqueTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloqueTipo
        fields = '__all__'
        depth = 1

class CategoriaMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMenu
        fields = '__all__'
        depth = 1

class ComportamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comportamiento
        fields = '__all__'
        depth = 2

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'
        depth = 2

class ConsultaMedicaEnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedicaEnfermedad
        fields = '__all__'
        depth = 2

class ConsultaMedicaPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedicaPersonal
        fields = '__all__'
        depth = 2

class ConsultaMedicaPersonalEnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedicaPersonalEnfermedad
        fields = '__all__'
        depth = 2

class ControlMatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlMatricula
        fields = '__all__'
        depth = 2

class ControlPensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlPension
        fields = '__all__'
        depth = 2
class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'
        depth = 1
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id','orden','nombre','abreviatura','seccion',]
        depth = 1

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        depth = 1

class DestrezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destreza
        fields = '__all__'
        depth = 2

class DestrezaProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestrezaProfesor
        fields = '__all__'
        depth = 2

class DetalleIngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleIngreso
        fields = '__all__'
        depth = 2

class DetalleLeccionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleLeccionario
        fields = '__all__'
        depth = 2

class DetalleOrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleOrdenTrabajo
        fields = '__all__'
        depth = 2

class EgresoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EgresoFamiliar
        fields = '__all__'
        depth = 2

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'
        depth = 1

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
        depth = 1

class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'
        depth = 1

class EscalaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaDetalle
        fields = '__all__'
        depth = 2

class EscolaridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escolaridad
        fields = '__all__'
        depth = 1

class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'
        depth = 1

class ExamenMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenMedico
        fields = '__all__'
        depth = 2

class ExamenMedicoPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenMedicoPersonal
        fields = '__all__'
        depth = 2

class FaltaComportamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaltaComportamiento
        fields = '__all__'
        depth = 2

class FichaSocioeconomicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaSocioeconomica
        fields = '__all__'
        depth = 2

class GrupoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoServicio
        fields = '__all__'
        depth = 1

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = '__all__'
        depth = 1

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
        depth = 2

class IndicadorInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadorInicial
        fields = '__all__'
        depth = 2

class IndicadorPreparatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicadorPreparatoria
        fields = '__all__'
        depth = 2

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'
        depth = 2

class IngresoFamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngresoFamiliar
        fields = '__all__'
        depth = 2

class InmunizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmunizacion
        fields = '__all__'
        depth = 1

class InmunizacionPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InmunizacionPersonal
        fields = '__all__'
        depth = 2

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        depth = 2

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'
        depth = 1

class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada
        fields = ['id','orden','nombre']
        depth = 1

class LeccionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccionario
        fields = '__all__'
        depth = 2

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
        depth = 1

class MateriaSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    class Meta:
        model = Materia
        fields = ['id','nombre','tipo','area']
        depth = 1

class MateriaEscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaEscala
        fields = '__all__'
        depth = 2

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        depth = 2

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'
        depth = 1

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        depth = 1

class MotivoConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoConsulta
        fields = '__all__'
        depth = 1

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'
        depth = 1

class NivelParaleloProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelParaleloProfesor
        fields = '__all__'
        depth = 2

class NivelParaleloProfesorAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelParaleloProfesorAlumno
        fields = '__all__'
        depth = 2

class NotaSerializer(serializers.ModelSerializer):
    materia = serializers.SerializerMethodField()
    
    class Meta:
        model = Nota
        fields = [
            'id', 'materia', 'nota1', 'nota2', 'nota3', 'nota4', 'nota5',
            'nota6', 'nota7', 'nota8', 'nota9', 'nota10', 'nota11', 'nota12',
            'nota13', 'nota14', 'nota15', 'nota16', 'nota17', 'nota18',
            'nota19', 'nota20', 'nota21', 'nota22', 'nota23', 'nota24',
            'nota25', 'nota26', 'nota27', 'nota28', 'nota29', 'nota30',
            'examen_q1', 'examen_q2', 'examen_q3',
            'examen_mejora', 'examen_supletorio', 'examen_remedial', 'examen_gracia'
        ]
    
    def get_materia(self, obj):
        if obj.paralelo_materia_profesor and hasattr(obj.paralelo_materia_profesor, 'materia'):
            return obj.paralelo_materia_profesor.materia.nombre
        return "Sin materia asignada"

class NotaAmbitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaAmbito
        fields = '__all__'
        depth = 2

class NotaComportamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaComportamiento
        fields = '__all__'
        depth = 2

class NotaDestrezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaDestreza
        fields = '__all__'
        depth = 2

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'
        depth = 2

class NotificacionAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacionAlumno
        fields = '__all__'
        depth = 2

class NotificacionParaleloSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacionParalelo
        fields = '__all__'
        depth = 2

class NotificacionParienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificacionPariente
        fields = '__all__'
        depth = 2

class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = '__all__'
        depth = 1

class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = '__all__'
        depth = 2

class ParaleloSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    jornada = JornadaSerializer()
    class Meta:
        model = Paralelo
        fields = ['id','nombre','abreviatura','curso','jornada',]
        depth = 2

class PeriodoAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoAcademico
        fields = ['id','nombre','abreviatura',]
        depth = 1

class PersonalSerializer(serializers.ModelSerializer):
    pais = PaisSerializer()
    provincia = ProvinciaSerializer()
    ciudad = CiudadSerializer()
    parroquia = ParroquiaSerializer()
    class Meta:
        model = Personal
        fields = ['id', 'nombre', 'apellido',
                  'genero','email','foto',
                  'fecha_nacimiento','tipo_sangre',
                  'numero_identificacion','direccion_domicilio',
                  'telefono_celular', 'nacionalidad',
                  'calle_principal', 'calle_secundaria',
                  'numero_casa','referencia_domicilio',
                  'email_institucional','pais',
                  'provincia','ciudad','parroquia',
                  ]
        depth = 2

class ParaleloMateriaProfesorSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()
    materia = MateriaSerializer()
    periodo_academico = PeriodoAcademicoSerializer()
    paralelo = ParaleloSerializer()
    class Meta:
        model = ParaleloMateriaProfesor
        fields = ['id','personal','materia','periodo_academico','paralelo']
        depth = 2

class ParametroComportamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroComportamiento
        fields = '__all__'
        depth = 2

class ParametroInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametroInicial
        fields = '__all__'
        depth = 2

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = '__all__'
        depth = 1

class ParienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pariente
        fields = '__all__'
        depth = 2

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
        depth = 1

class PerfilMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilMenu
        fields = '__all__'
        depth = 2

class PerfilSeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilSeccion
        fields = '__all__'
        depth = 2


class ProfesionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesion
        fields = '__all__'
        depth = 1

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        depth = 1

class RangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rango
        fields = '__all__'
        depth = 1

class RecordAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordAcademico
        fields = '__all__'
        depth = 2



class SeccionEscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeccionEscala
        fields = '__all__'
        depth = 2

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = '__all__'
        depth = 1

class TareaComunicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaComunicado
        fields = '__all__'
        depth = 2

class TipoEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipo
        fields = '__all__'
        depth = 1

class TipoNotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNotificacion
        fields = '__all__'
        depth = 1

class TipoTecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTecnologia
        fields = '__all__'
        depth = 1

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'
        depth = 1

class TutoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutoria
        fields = '__all__'
        depth = 2

class UsuarioSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()
    class Meta:
        model = Usuario
        fields = ['id','nombre','apellido','email','usuario','clave','es_superadmin','estado','personal']
        depth = 2

class UsuarioInstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioInstitucion
        fields = '__all__'
        depth = 2

class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPerfil
        fields = '__all__'
        depth = 2
        
"""
Atraso
"""

class AtrasoSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer()
    paralelo_materia_profesor = ParaleloMateriaProfesorSerializer()
    periodo_academico = PeriodoAcademicoSerializer()
    created_by = UsuarioSerializer()
    
    alumno_nombre = serializers.CharField(source='alumno.nombre', read_only=True)
    materia_nombre = serializers.CharField(
        source='paralelo_materia_profesor.materia.nombre', 
        read_only=True
    )
    profesor_nombre = serializers.CharField(
        source='paralelo_materia_profesor.personal.nombre',
        read_only=True
    )

    class Meta:
        model = Atraso
        fields = ['id','alumno','paralelo_materia_profesor','periodo_academico','fecha','hora','observacion','created_by','alumno_nombre','materia_nombre','profesor_nombre']
        depth = 2
        
class AtrasoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atraso
        fields = [
            'alumno',
            'paralelo_materia_profesor',
            'periodo_academico',
            'fecha',
            'hora',
            'observacion'
        ]

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    
    
"""
AUTENTICACIÓN PARA REPRESENTANTES
"""

class ParienteLoginSerializer(serializers.Serializer):
    numero_identificacion = serializers.CharField()
    password = serializers.CharField(required=False)

    def validate(self, attrs):
        numero_identificacion = attrs.get('numero_identificacion')
        
        try:
            pariente = Pariente.objects.get(numero_identificacion=numero_identificacion)
        except Pariente.DoesNotExist:
            raise serializers.ValidationError("Número de identificación no registrado")

        # Si necesitas validar contraseña (ej: últimos 4 dígitos del teléfono)
        if attrs.get('password') != numero_identificacion:  # Ajustar según tu lógica
            raise serializers.ValidationError("Credenciales incorrectas")

        return {
            'pariente': pariente,
            'pariente_id': pariente.id,
            'nombre': f"{pariente.nombre} {pariente.apellido}",
        }
        
        # Generamos un token JWT manualmente (sin vincularlo a un User de Django)
        refresh = RefreshToken.for_user(pariente)  # Necesitamos adaptar esto (ver Paso 2)
        
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
            'pariente_id': pariente.id,
            'nombre': f"{pariente.nombre} {pariente.apellido}",
        }