# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import base64
from datetime import datetime, timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .encript_utils import encrypt_ci4, decrypt_ci4

class Alumno(models.Model):
    pais = models.ForeignKey('Pais', models.DO_NOTHING)
    provincia = models.ForeignKey('Provincia', models.DO_NOTHING)
    ciudad = models.ForeignKey('Ciudad', models.DO_NOTHING)
    parroquia = models.ForeignKey('Parroquia', models.DO_NOTHING)
    religion = models.ForeignKey('Religion', models.DO_NOTHING)
    ruta_evacuacion = models.ForeignKey('RutaEvacuacion', models.DO_NOTHING)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.CharField(max_length=15, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=255, blank=True, null=True)
    nacionalidad = models.CharField(max_length=45, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=1, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=15, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    tiene_enfermedad = models.CharField(max_length=2, blank=True, null=True)
    enfermedad = models.TextField(blank=True, null=True)
    medicamento = models.TextField(blank=True, null=True)
    tiene_discapacidad = models.CharField(max_length=2, blank=True, null=True)
    discapacidad = models.CharField(max_length=255, blank=True, null=True)
    calle_principal = models.CharField(max_length=255, blank=True, null=True)
    calle_secundaria = models.CharField(max_length=255, blank=True, null=True)
    barrio_conjunto_sector = models.CharField(max_length=255, blank=True, null=True)
    numero_casa = models.CharField(max_length=15, blank=True, null=True)
    codigo_cliente = models.CharField(max_length=15, blank=True, null=True)
    responsable_factura = models.CharField(max_length=255, blank=True, null=True)
    tipo_documento_factura = models.CharField(max_length=1, blank=True, null=True)
    numero_identificacion_factura = models.CharField(max_length=15, blank=True, null=True)
    email_factura = models.CharField(max_length=200, blank=True, null=True)
    familiar_zona_segura = models.CharField(max_length=255, blank=True, null=True)
    telefono_fijo_familiar_zona_segura = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular_familiar_zona_segura = models.CharField(max_length=15, blank=True, null=True)
    cuen = models.CharField(max_length=15, blank=True, null=True)
    antecedente_familiar = models.TextField(blank=True, null=True)
    antecedente_prenatal = models.TextField(blank=True, null=True)
    antecedente_natal = models.TextField(blank=True, null=True)
    antecedente_postnatal = models.TextField(blank=True, null=True)
    enfermedad_cronica = models.TextField(blank=True, null=True)
    alergia = models.TextField(blank=True, null=True)
    horas_suenio = models.IntegerField(blank=True, null=True)
    alimenticio = models.CharField(max_length=255, blank=True, null=True)
    miccional = models.CharField(max_length=255, blank=True, null=True)
    tabaquismo = models.CharField(max_length=255, blank=True, null=True)
    menarquia = models.CharField(max_length=255, blank=True, null=True)
    defecatorio = models.CharField(max_length=255, blank=True, null=True)
    alcoholismo = models.CharField(max_length=255, blank=True, null=True)
    ciclos = models.CharField(max_length=255, blank=True, null=True)
    otras_sustancias = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    antecedente_clinico = models.TextField(blank=True, null=True)
    antecedente_farmacologico = models.TextField(blank=True, null=True)
    antecedente_quirurgico = models.TextField(blank=True, null=True)
    antecedente_traumatico = models.TextField(blank=True, null=True)
    antecedente_psiquiatrico = models.TextField(blank=True, null=True)
    fum = models.CharField(max_length=255, blank=True, null=True)
    disminorrea = models.CharField(max_length=15, blank=True, null=True)
    gestas = models.IntegerField(blank=True, null=True)
    partos = models.IntegerField(blank=True, null=True)
    abortos = models.IntegerField(blank=True, null=True)
    cesareas = models.IntegerField(blank=True, null=True)
    hijos_vivos = models.IntegerField(blank=True, null=True)
    planificacion_familiar = models.CharField(max_length=255, blank=True, null=True)
    paptest = models.CharField(max_length=255, blank=True, null=True)
    inmunizaciones = models.TextField(blank=True, null=True)
    cardiovascular = models.CharField(max_length=255, blank=True, null=True)
    respiratorio = models.CharField(max_length=255, blank=True, null=True)
    digestivo = models.CharField(max_length=255, blank=True, null=True)
    genitourinario = models.CharField(max_length=255, blank=True, null=True)
    neurologico = models.CharField(max_length=255, blank=True, null=True)
    dermantologico = models.CharField(max_length=255, blank=True, null=True)
    ocular = models.CharField(max_length=255, blank=True, null=True)
    auditivo = models.CharField(max_length=255, blank=True, null=True)
    osteomuscular = models.CharField(max_length=255, blank=True, null=True)
    endocrino = models.CharField(max_length=255, blank=True, null=True)
    tension_arterial = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_cardiaca = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_respiratoria = models.CharField(max_length=255, blank=True, null=True)
    temperatura = models.CharField(max_length=50, blank=True, null=True)
    saturacion_oxigeno = models.CharField(max_length=50, blank=True, null=True)
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.CharField(max_length=45, blank=True, null=True)
    imc = models.CharField(max_length=45, blank=True, null=True)
    piel = models.CharField(max_length=255, blank=True, null=True)
    ojos = models.CharField(max_length=255, blank=True, null=True)
    oidos = models.CharField(max_length=255, blank=True, null=True)
    nariz = models.CharField(max_length=255, blank=True, null=True)
    boca = models.CharField(max_length=255, blank=True, null=True)
    cuello = models.CharField(max_length=255, blank=True, null=True)
    torax = models.CharField(max_length=255, blank=True, null=True)
    abdomen = models.CharField(max_length=255, blank=True, null=True)
    genitales = models.CharField(max_length=255, blank=True, null=True)
    extremidades = models.CharField(max_length=255, blank=True, null=True)
    neurologico_examen = models.CharField(max_length=255, blank=True, null=True)
    descripcion_examen = models.TextField(blank=True, null=True)
    observacion_examen = models.TextField(blank=True, null=True)
    impresion_diagnostica = models.TextField(blank=True, null=True)
    recomendacion_examen = models.TextField(blank=True, null=True)
    es_bautizado = models.CharField(max_length=2, blank=True, null=True)
    tuvo_covid = models.CharField(max_length=2, blank=True, null=True)
    tiene_vacuna = models.CharField(max_length=2, blank=True, null=True)
    nombre_vacuna = models.CharField(max_length=100, blank=True, null=True)
    dosis_vacuna = models.IntegerField(blank=True, null=True)
    clave_teams = models.CharField(max_length=50, blank=True, null=True)
    solicita_clave_teams = models.CharField(max_length=2, blank=True, null=True)
    pendiente = models.TextField(blank=True, null=True)
    desbloqueo_authenticator = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno'


class AlumnoPariente(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    pariente = models.ForeignKey('Pariente', models.DO_NOTHING)
    es_representante = models.CharField(max_length=1, blank=True, null=True)
    es_facturacion = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno_pariente'


class Ambito(models.Model):
    materia = models.ForeignKey('Materia', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ambito'


class AmbitoProfesor(models.Model):
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor', models.DO_NOTHING)
    ambito = models.ForeignKey(Ambito, models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ambito_profesor'


class Area(models.Model):
    institucion = models.ForeignKey('Institucion', models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class Aseguradora(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aseguradora'


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    asistencia = models.CharField(max_length=1, blank=True, null=True)
    atraso = models.CharField(max_length=1, blank=True, null=True)
    falta_justificada = models.CharField(max_length=1, blank=True, null=True)
    falta_injustificada = models.CharField(max_length=1, blank=True, null=True)
    no_laborado = models.CharField(max_length=1, blank=True, null=True)
    motivo_atraso = models.CharField(max_length=500, blank=True, null=True)
    motivo_justificada = models.CharField(max_length=500, blank=True, null=True)
    motivo_injustificada = models.CharField(max_length=500, blank=True, null=True)
    abreviatura_no_laborado = models.CharField(max_length=5, blank=True, null=True)
    motivo_no_laborado = models.TextField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'


class AsistenciaPersonal(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    asistencia = models.CharField(max_length=1, blank=True, null=True)
    atraso = models.CharField(max_length=1, blank=True, null=True)
    falta_justificada = models.CharField(max_length=1, blank=True, null=True)
    falta_injustificada = models.CharField(max_length=1, blank=True, null=True)
    no_laborado = models.CharField(max_length=1, blank=True, null=True)
    motivo_atraso = models.CharField(max_length=500, blank=True, null=True)
    motivo_justificada = models.CharField(max_length=500, blank=True, null=True)
    motivo_injustificada = models.CharField(max_length=500, blank=True, null=True)
    abreviatura_no_laborado = models.CharField(max_length=5, blank=True, null=True)
    motivo_no_laborado = models.TextField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia_personal'


class AsistenciaTrimestre(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    nota_comportamiento_t1 = models.CharField(max_length=5, blank=True, null=True)
    falta_justificada_t1 = models.CharField(max_length=5, blank=True, null=True)
    falta_injustificada_t1 = models.CharField(max_length=5, blank=True, null=True)
    atraso_t1 = models.CharField(max_length=5, blank=True, null=True)
    nota_comportamiento_t2 = models.CharField(max_length=5, blank=True, null=True)
    falta_justificada_t2 = models.CharField(max_length=5, blank=True, null=True)
    falta_injustificada_t2 = models.CharField(max_length=5, blank=True, null=True)
    atraso_t2 = models.CharField(max_length=5, blank=True, null=True)
    nota_comportamiento_t3 = models.CharField(max_length=5, blank=True, null=True)
    falta_justificada_t3 = models.CharField(max_length=5, blank=True, null=True)
    falta_injustificada_t3 = models.CharField(max_length=5, blank=True, null=True)
    atraso_t3 = models.CharField(max_length=5, blank=True, null=True)
    nota1 = models.CharField(max_length=5, blank=True, null=True)
    nota2 = models.CharField(max_length=5, blank=True, null=True)
    nota3 = models.CharField(max_length=5, blank=True, null=True)
    nota4 = models.CharField(max_length=5, blank=True, null=True)
    nota5 = models.CharField(max_length=5, blank=True, null=True)
    nota6 = models.CharField(max_length=5, blank=True, null=True)
    nota7 = models.CharField(max_length=5, blank=True, null=True)
    nota8 = models.CharField(max_length=5, blank=True, null=True)
    nota9 = models.CharField(max_length=5, blank=True, null=True)
    nota10 = models.CharField(max_length=5, blank=True, null=True)
    nota11 = models.CharField(max_length=5, blank=True, null=True)
    nota12 = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia_trimestre'


class Auditoria(models.Model):
    usuario_id = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    accion = models.CharField(max_length=45, blank=True, null=True)
    instruccion = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria'


class AulaParalelo(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING)
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=1000, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aula_paralelo'


class Baja(models.Model):
    medicamento = models.ForeignKey('Medicamento', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    motivo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'baja'


class Bloque(models.Model):
    bloque_tipo = models.ForeignKey('BloqueTipo', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    indice = models.CharField(max_length=10, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    promedia = models.CharField(max_length=1, blank=True, null=True)
    promedia_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insumo1_etiqueta = models.CharField(max_length=45, blank=True, null=True)
    insumo1_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insumo2_etiqueta = models.CharField(max_length=45, blank=True, null=True)
    insumo2_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insumo3_etiqueta = models.CharField(max_length=45, blank=True, null=True)
    insumo3_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insumo4_etiqueta = models.CharField(max_length=45, blank=True, null=True)
    insumo4_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    insumo5_etiqueta = models.CharField(max_length=45, blank=True, null=True)
    insumo5_porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloque'


class BloqueParaleloFecha(models.Model):
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    bloque = models.ForeignKey(Bloque, models.DO_NOTHING)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloque_paralelo_fecha'


class BloqueTipo(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    nombre = models.CharField(max_length=45)
    indice = models.CharField(max_length=5, blank=True, null=True)
    dias_laborados = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloque_tipo'


class CategoriaMenu(models.Model):
    codigo = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    icono = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria_menu'


class Ciudad(models.Model):
    provincia = models.ForeignKey('Provincia', models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comportamiento(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    nota1 = models.CharField(max_length=5, blank=True, null=True)
    nota2 = models.CharField(max_length=5, blank=True, null=True)
    nota3 = models.CharField(max_length=5, blank=True, null=True)
    nota4 = models.CharField(max_length=5, blank=True, null=True)
    nota5 = models.CharField(max_length=5, blank=True, null=True)
    nota6 = models.CharField(max_length=5, blank=True, null=True)
    nota7 = models.CharField(max_length=5, blank=True, null=True)
    nota8 = models.CharField(max_length=5, blank=True, null=True)
    nota9 = models.CharField(max_length=5, blank=True, null=True)
    nota10 = models.CharField(max_length=5, blank=True, null=True)
    nota11 = models.CharField(max_length=5, blank=True, null=True)
    nota12 = models.CharField(max_length=5, blank=True, null=True)
    nota13 = models.CharField(max_length=5, blank=True, null=True)
    nota14 = models.CharField(max_length=5, blank=True, null=True)
    nota15 = models.CharField(max_length=5, blank=True, null=True)
    nota16 = models.CharField(max_length=5, blank=True, null=True)
    nota17 = models.CharField(max_length=5, blank=True, null=True)
    nota18 = models.CharField(max_length=5, blank=True, null=True)
    nota19 = models.CharField(max_length=5, blank=True, null=True)
    nota20 = models.CharField(max_length=5, blank=True, null=True)
    nota21 = models.CharField(max_length=5, blank=True, null=True)
    nota22 = models.CharField(max_length=5, blank=True, null=True)
    nota23 = models.CharField(max_length=5, blank=True, null=True)
    nota24 = models.CharField(max_length=5, blank=True, null=True)
    nota25 = models.CharField(max_length=5, blank=True, null=True)
    nota26 = models.CharField(max_length=5, blank=True, null=True)
    nota27 = models.CharField(max_length=5, blank=True, null=True)
    nota28 = models.CharField(max_length=5, blank=True, null=True)
    nota29 = models.CharField(max_length=5, blank=True, null=True)
    nota30 = models.CharField(max_length=5, blank=True, null=True)
    nota31 = models.CharField(max_length=5, blank=True, null=True)
    nota32 = models.CharField(max_length=5, blank=True, null=True)
    nota33 = models.CharField(max_length=5, blank=True, null=True)
    nota34 = models.CharField(max_length=5, blank=True, null=True)
    nota35 = models.CharField(max_length=5, blank=True, null=True)
    nota36 = models.CharField(max_length=5, blank=True, null=True)
    nota37 = models.CharField(max_length=5, blank=True, null=True)
    nota38 = models.CharField(max_length=5, blank=True, null=True)
    nota39 = models.CharField(max_length=5, blank=True, null=True)
    nota40 = models.CharField(max_length=5, blank=True, null=True)
    nota41 = models.CharField(max_length=5, blank=True, null=True)
    nota42 = models.CharField(max_length=5, blank=True, null=True)
    nota43 = models.CharField(max_length=5, blank=True, null=True)
    nota44 = models.CharField(max_length=5, blank=True, null=True)
    nota45 = models.CharField(max_length=5, blank=True, null=True)
    nota46 = models.CharField(max_length=5, blank=True, null=True)
    nota47 = models.CharField(max_length=5, blank=True, null=True)
    nota48 = models.CharField(max_length=5, blank=True, null=True)
    nota49 = models.CharField(max_length=5, blank=True, null=True)
    nota50 = models.CharField(max_length=5, blank=True, null=True)
    nota51 = models.CharField(max_length=5, blank=True, null=True)
    nota52 = models.CharField(max_length=5, blank=True, null=True)
    nota53 = models.CharField(max_length=5, blank=True, null=True)
    nota54 = models.CharField(max_length=5, blank=True, null=True)
    nota55 = models.CharField(max_length=5, blank=True, null=True)
    nota56 = models.CharField(max_length=5, blank=True, null=True)
    nota57 = models.CharField(max_length=5, blank=True, null=True)
    nota58 = models.CharField(max_length=5, blank=True, null=True)
    nota59 = models.CharField(max_length=5, blank=True, null=True)
    nota60 = models.CharField(max_length=5, blank=True, null=True)
    nota61 = models.CharField(max_length=5, blank=True, null=True)
    nota62 = models.CharField(max_length=5, blank=True, null=True)
    nota63 = models.CharField(max_length=5, blank=True, null=True)
    nota64 = models.CharField(max_length=5, blank=True, null=True)
    nota65 = models.CharField(max_length=5, blank=True, null=True)
    nota66 = models.CharField(max_length=5, blank=True, null=True)
    nota67 = models.CharField(max_length=5, blank=True, null=True)
    nota68 = models.CharField(max_length=5, blank=True, null=True)
    nota69 = models.CharField(max_length=5, blank=True, null=True)
    nota70 = models.CharField(max_length=5, blank=True, null=True)
    nota71 = models.CharField(max_length=5, blank=True, null=True)
    nota72 = models.CharField(max_length=5, blank=True, null=True)
    quimestral_q1 = models.CharField(max_length=5, blank=True, null=True)
    quimestral_q2 = models.CharField(max_length=5, blank=True, null=True)
    faltas_justificadas_q1 = models.IntegerField(blank=True, null=True)
    faltas_injustificadas_q1 = models.IntegerField(blank=True, null=True)
    atrasos_q1 = models.IntegerField(blank=True, null=True)
    faltas_justificadas_q2 = models.IntegerField(blank=True, null=True)
    faltas_injustificadas_q2 = models.IntegerField(blank=True, null=True)
    atrasos_q2 = models.IntegerField(blank=True, null=True)
    faltas_justificadas_q3 = models.IntegerField(blank=True, null=True)
    faltas_injustificadas_q3 = models.IntegerField(blank=True, null=True)
    atrasos_q3 = models.IntegerField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comportamiento'


class ConsultaMedica(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    motivo_consulta = models.ForeignKey('MotivoConsulta', models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)
    tratamiento = models.CharField(max_length=1000, blank=True, null=True)
    talla = models.CharField(max_length=15, blank=True, null=True)
    peso = models.CharField(max_length=15, blank=True, null=True)
    perimetro_craneal = models.CharField(max_length=15, blank=True, null=True)
    enfermedad_actual = models.CharField(max_length=1000, blank=True, null=True)
    examen_fisico = models.CharField(max_length=2000, blank=True, null=True)
    tension_arterial = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_cardiaca = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_respiratoria = models.CharField(max_length=255, blank=True, null=True)
    temperatura = models.CharField(max_length=50, blank=True, null=True)
    saturacion_oxigeno = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_medica'


class ConsultaMedicaEnfermedad(models.Model):
    consulta_medica = models.OneToOneField(ConsultaMedica, models.DO_NOTHING, primary_key=True)  # The composite primary key (consulta_medica_id, enfermedad_id) found, that is not supported. The first column is selected.
    enfermedad = models.ForeignKey('Enfermedad', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_medica_enfermedad'
        unique_together = (('consulta_medica', 'enfermedad'),)


class ConsultaMedicaPersonal(models.Model):
    motivo_consulta = models.ForeignKey('MotivoConsulta', models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)
    tratamiento = models.CharField(max_length=1000, blank=True, null=True)
    talla = models.CharField(max_length=15, blank=True, null=True)
    peso = models.CharField(max_length=15, blank=True, null=True)
    imc = models.CharField(max_length=15, blank=True, null=True)
    enfermedad_actual = models.CharField(max_length=1000, blank=True, null=True)
    examen_fisico = models.CharField(max_length=2000, blank=True, null=True)
    tension_arterial = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_cardiaca = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_respiratoria = models.CharField(max_length=255, blank=True, null=True)
    temperatura = models.CharField(max_length=50, blank=True, null=True)
    saturacion_oxigeno = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_medica_personal'


class ConsultaMedicaPersonalEnfermedad(models.Model):
    consulta_medica_personal = models.OneToOneField(ConsultaMedicaPersonal, models.DO_NOTHING, primary_key=True)  # The composite primary key (consulta_medica_personal_id, enfermedad_id) found, that is not supported. The first column is selected.
    enfermedad = models.ForeignKey('Enfermedad', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta_medica_personal_enfermedad'
        unique_together = (('consulta_medica_personal', 'enfermedad'),)


class ControlMatricula(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    inscripcion = models.ForeignKey('Inscripcion', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    valor_matricula = models.CharField(max_length=10, blank=True, null=True)
    tiene_seguro = models.CharField(max_length=2, blank=True, null=True)
    cancelado = models.CharField(max_length=2, blank=True, null=True)
    grupo = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_matricula'


class ControlPension(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    matricula = models.ForeignKey('Matricula', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    tiene_seguro = models.CharField(max_length=1, blank=True, null=True)
    tiene_lunch = models.CharField(max_length=1, blank=True, null=True)
    es_becado = models.CharField(max_length=1, blank=True, null=True)
    valor_beca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_seguro = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_lunch = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    septiembre = models.CharField(max_length=1, blank=True, null=True)
    valorseptiembre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    octubre = models.CharField(max_length=1, blank=True, null=True)
    valoroctubre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    noviembre = models.CharField(max_length=1, blank=True, null=True)
    valornoviembre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diciembre = models.CharField(max_length=1, blank=True, null=True)
    valordiciembre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    enero = models.CharField(max_length=1, blank=True, null=True)
    valorenero = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    febrero = models.CharField(max_length=1, blank=True, null=True)
    valorfebrero = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    marzo = models.CharField(max_length=1, blank=True, null=True)
    valormarzo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    abril = models.CharField(max_length=1, blank=True, null=True)
    valorabril = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mayo = models.CharField(max_length=1, blank=True, null=True)
    valormayo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    junio = models.CharField(max_length=1, blank=True, null=True)
    valorjunio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    registrado = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_pension'


class Curso(models.Model):
    seccion = models.ForeignKey('Seccion', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    abreviatura = models.CharField(max_length=45, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class Departamento(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Destreza(models.Model):
    ambito = models.ForeignKey(Ambito, models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=300, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destreza'


class DestrezaProfesor(models.Model):
    ambito_profesor = models.ForeignKey(AmbitoProfesor, models.DO_NOTHING)
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor', models.DO_NOTHING)
    destreza = models.ForeignKey(Destreza, models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    q1 = models.CharField(max_length=1, blank=True, null=True)
    q2 = models.CharField(max_length=1, blank=True, null=True)
    q3 = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'destreza_profesor'


class DetalleIngreso(models.Model):
    ingreso = models.ForeignKey('Ingreso', models.DO_NOTHING)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ingreso'


class DetalleLeccionario(models.Model):
    leccionario = models.ForeignKey('Leccionario', models.DO_NOTHING)
    falta_comportamiento = models.ForeignKey('FaltaComportamiento', models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    horario = models.ForeignKey('Horario', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_leccionario'


class DetalleOrdenTrabajo(models.Model):
    orden_trabajo = models.ForeignKey('OrdenTrabajo', models.DO_NOTHING)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    solucion = models.CharField(max_length=500, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_orden_trabajo'


class EgresoFamiliar(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    egreso_diario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    egreso_semanal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    egreso_mensual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    egreso_anual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'egreso_familiar'


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermedad'


class Equipo(models.Model):
    tipo_equipo = models.ForeignKey('TipoEquipo', models.DO_NOTHING)
    marca = models.ForeignKey('Marca', models.DO_NOTHING)
    tipo_tecnologia = models.ForeignKey('TipoTecnologia', models.DO_NOTHING)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    modelo = models.CharField(max_length=100, blank=True, null=True)
    serie = models.CharField(max_length=50, blank=True, null=True)
    potencia = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    observacion = models.CharField(max_length=1000, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo'


class Escala(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escala'


class EscalaDetalle(models.Model):
    escala = models.ForeignKey(Escala, models.DO_NOTHING)
    orden = models.IntegerField()
    abreviatura = models.CharField(max_length=5)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)
    nota_minima = models.DecimalField(max_digits=10, decimal_places=2)
    nota_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escala_detalle'


class Escolaridad(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escolaridad'


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_civil'


class ExamenMedico(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.CharField(max_length=2000, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examen_medico'


class ExamenMedicoPersonal(models.Model):
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    detalle = models.CharField(max_length=2000, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examen_medico_personal'


class FaltaComportamiento(models.Model):
    nombre = models.CharField(max_length=255)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'falta_comportamiento'


class FichaSocioeconomica(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    institucion_estudia = models.CharField(max_length=200, blank=True, null=True)
    jornada_estudio = models.CharField(max_length=15, blank=True, null=True)
    grado_curso_inscripcion = models.CharField(max_length=100, blank=True, null=True)
    observacion_estudio = models.CharField(max_length=2000, blank=True, null=True)
    tiene_capacidad_especial_beneficiario = models.CharField(max_length=2, blank=True, null=True)
    capacidad_especial_beneficiario = models.CharField(max_length=500, blank=True, null=True)
    tiene_problema_aprendizaje = models.CharField(max_length=2, blank=True, null=True)
    problema_aprendizaje = models.CharField(max_length=100, blank=True, null=True)
    numero_hijos_familia = models.IntegerField(blank=True, null=True)
    hijos_hombres_familia = models.IntegerField(blank=True, null=True)
    hijas_mujeres_familia = models.IntegerField(blank=True, null=True)
    lugar_familia = models.IntegerField(blank=True, null=True)
    tiene_familiar_capacidad_especial = models.CharField(max_length=2, blank=True, null=True)
    capacidad_especial_familiar = models.CharField(max_length=200, blank=True, null=True)
    tiene_enfermedad_catastrofica_familiar = models.CharField(max_length=2, blank=True, null=True)
    enfermedad_catastrofica_familiar = models.CharField(max_length=200, blank=True, null=True)
    tiene_subsidio_economico = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_socioeconomica'


class GrupoServicio(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grupo_servicio'


class Hora(models.Model):
    rango = models.ForeignKey('Rango', models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    hora_desde = models.TimeField(blank=True, null=True)
    hora_hasta = models.TimeField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hora'


class Horario(models.Model):
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    hora = models.ForeignKey(Hora, models.DO_NOTHING)
    lunes = models.CharField(max_length=10, blank=True, null=True)
    martes = models.CharField(max_length=10, blank=True, null=True)
    miercoles = models.CharField(max_length=10, blank=True, null=True)
    jueves = models.CharField(max_length=10, blank=True, null=True)
    viernes = models.CharField(max_length=10, blank=True, null=True)
    lunes_link = models.CharField(max_length=500, blank=True, null=True)
    martes_link = models.CharField(max_length=500, blank=True, null=True)
    miercoles_link = models.CharField(max_length=500, blank=True, null=True)
    jueves_link = models.CharField(max_length=500, blank=True, null=True)
    viernes_link = models.CharField(max_length=500, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class IndicadorInicial(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    desde = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hasta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_inicial'


class IndicadorPreparatoria(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    desde = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hasta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicador_preparatoria'


class Ingreso(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    fecha = models.DateField()
    numero_documento = models.CharField(max_length=45)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso'


class IngresoFamiliar(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ingreso_mensual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso_familiar'


class Inmunizacion(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    inmunizacion1 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion2 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion3 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion4 = models.CharField(max_length=5, blank=True, null=True)
    refuerzo1 = models.CharField(max_length=45, blank=True, null=True)
    refuerzo2 = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmunizacion'


class InmunizacionPersonal(models.Model):
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    inmunizacion1 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion2 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion3 = models.CharField(max_length=5, blank=True, null=True)
    inmunizacion4 = models.CharField(max_length=5, blank=True, null=True)
    refuerzo1 = models.CharField(max_length=45, blank=True, null=True)
    refuerzo2 = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmunizacion_personal'


class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    grupo_servicio = models.ForeignKey(GrupoServicio, models.DO_NOTHING)
    aseguradora = models.ForeignKey(Aseguradora, models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    fecha_activacion = models.DateField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    proviene_de = models.CharField(max_length=200, blank=True, null=True)
    cancelacion_haberes = models.CharField(max_length=2, blank=True, null=True)
    convivencia_padres_familia = models.CharField(max_length=2, blank=True, null=True)
    participacion_estudiante = models.CharField(max_length=200, blank=True, null=True)
    opcion_juvenil = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscripcion'


class Institucion(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    ruc = models.CharField(max_length=45, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    amie = models.CharField(max_length=15, blank=True, null=True)
    escudo = models.CharField(max_length=45, blank=True, null=True)
    rector = models.CharField(max_length=100, blank=True, null=True)
    secretario = models.CharField(max_length=100, blank=True, null=True)
    inspector = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=10, blank=True, null=True)
    web = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institucion'


class Jornada(models.Model):
    institucion = models.ForeignKey(Institucion, models.DO_NOTHING)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jornada'


class Leccionario(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leccionario'


class Marca(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'


class Materia(models.Model):
    area = models.ForeignKey(Area, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    nombre_bi = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    rango_edad = models.CharField(max_length=50, blank=True, null=True)
    nivel = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia'


class MateriaEscala(models.Model):
    materia = models.ForeignKey(Materia, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    escala = models.ForeignKey(Escala, models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia_escala'


class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    aseguradora = models.ForeignKey(Aseguradora, models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    proviene_de = models.CharField(max_length=200, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    fecha_retiro = models.DateField(blank=True, null=True)
    razon_retiro = models.CharField(max_length=500, blank=True, null=True)
    factura = models.CharField(max_length=100, blank=True, null=True)
    solicitud = models.CharField(max_length=100, blank=True, null=True)
    promocion = models.CharField(max_length=100, blank=True, null=True)
    acepta = models.CharField(max_length=2, blank=True, null=True)
    asistencia_presencial = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'


class Medicamento(models.Model):
    nombre = models.CharField(max_length=500)
    stock = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicamento'


class Menu(models.Model):
    categoria_menu = models.ForeignKey(CategoriaMenu, models.DO_NOTHING)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ruta = models.CharField(max_length=200, blank=True, null=True)
    ruta_clave = models.CharField(max_length=100, blank=True, null=True)
    icono = models.CharField(max_length=50, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class MotivoConsulta(models.Model):
    nombre = models.CharField(max_length=500, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motivo_consulta'


class Nivel(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    materia = models.ForeignKey(Materia, models.DO_NOTHING, related_name='materia_nivel')
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel'


class NivelParaleloProfesor(models.Model):
    nivel = models.ForeignKey(Nivel, models.DO_NOTHING)
    curso = models.ForeignKey(Curso, models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_paralelo_profesor'


class NivelParaleloProfesorAlumno(models.Model):
    nivel_paralelo_profesor = models.ForeignKey(NivelParaleloProfesor, models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel_paralelo_profesor_alumno'


class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor', models.DO_NOTHING)
    nota1 = models.CharField(max_length=5, blank=True, null=True)
    nota2 = models.CharField(max_length=5, blank=True, null=True)
    nota3 = models.CharField(max_length=5, blank=True, null=True)
    nota4 = models.CharField(max_length=5, blank=True, null=True)
    nota5 = models.CharField(max_length=5, blank=True, null=True)
    nota6 = models.CharField(max_length=5, blank=True, null=True)
    nota7 = models.CharField(max_length=5, blank=True, null=True)
    nota8 = models.CharField(max_length=5, blank=True, null=True)
    nota9 = models.CharField(max_length=5, blank=True, null=True)
    nota10 = models.CharField(max_length=5, blank=True, null=True)
    nota11 = models.CharField(max_length=5, blank=True, null=True)
    nota12 = models.CharField(max_length=5, blank=True, null=True)
    nota13 = models.CharField(max_length=5, blank=True, null=True)
    nota14 = models.CharField(max_length=5, blank=True, null=True)
    nota15 = models.CharField(max_length=5, blank=True, null=True)
    nota16 = models.CharField(max_length=5, blank=True, null=True)
    nota17 = models.CharField(max_length=5, blank=True, null=True)
    nota18 = models.CharField(max_length=5, blank=True, null=True)
    nota19 = models.CharField(max_length=5, blank=True, null=True)
    nota20 = models.CharField(max_length=5, blank=True, null=True)
    nota21 = models.CharField(max_length=5, blank=True, null=True)
    nota22 = models.CharField(max_length=5, blank=True, null=True)
    nota23 = models.CharField(max_length=5, blank=True, null=True)
    nota24 = models.CharField(max_length=5, blank=True, null=True)
    nota25 = models.CharField(max_length=5, blank=True, null=True)
    nota26 = models.CharField(max_length=5, blank=True, null=True)
    nota27 = models.CharField(max_length=5, blank=True, null=True)
    nota28 = models.CharField(max_length=5, blank=True, null=True)
    nota29 = models.CharField(max_length=5, blank=True, null=True)
    nota30 = models.CharField(max_length=5, blank=True, null=True)
    examen_q1 = models.CharField(max_length=5, blank=True, null=True)
    examen_q2 = models.CharField(max_length=5, blank=True, null=True)
    examen_q3 = models.CharField(max_length=5, blank=True, null=True)
    examen_mejora = models.CharField(max_length=5, blank=True, null=True)
    examen_supletorio = models.CharField(max_length=5, blank=True, null=True)
    examen_remedial = models.CharField(max_length=5, blank=True, null=True)
    examen_gracia = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota'


class NotaAmbito(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    ambito_profesor = models.ForeignKey(AmbitoProfesor, models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    promedio_q1 = models.CharField(max_length=5, blank=True, null=True)
    examen_q1 = models.CharField(max_length=5, blank=True, null=True)
    informe_q1 = models.TextField(blank=True, null=True)
    promedio_q2 = models.CharField(max_length=5, blank=True, null=True)
    examen_q2 = models.CharField(max_length=5, blank=True, null=True)
    informe_q2 = models.TextField(blank=True, null=True)
    examen_q3 = models.CharField(max_length=5, blank=True, null=True)
    informe_q3 = models.TextField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_ambito'


class NotaComportamiento(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor', models.DO_NOTHING)
    nota1 = models.CharField(max_length=5, blank=True, null=True)
    nota2 = models.CharField(max_length=5, blank=True, null=True)
    nota3 = models.CharField(max_length=5, blank=True, null=True)
    nota4 = models.CharField(max_length=5, blank=True, null=True)
    nota5 = models.CharField(max_length=5, blank=True, null=True)
    nota6 = models.CharField(max_length=5, blank=True, null=True)
    nota7 = models.CharField(max_length=5, blank=True, null=True)
    nota8 = models.CharField(max_length=5, blank=True, null=True)
    nota9 = models.CharField(max_length=5, blank=True, null=True)
    nota10 = models.CharField(max_length=5, blank=True, null=True)
    nota11 = models.CharField(max_length=5, blank=True, null=True)
    nota12 = models.CharField(max_length=5, blank=True, null=True)
    nota13 = models.CharField(max_length=5, blank=True, null=True)
    nota14 = models.CharField(max_length=5, blank=True, null=True)
    nota15 = models.CharField(max_length=5, blank=True, null=True)
    nota16 = models.CharField(max_length=5, blank=True, null=True)
    nota17 = models.CharField(max_length=5, blank=True, null=True)
    nota18 = models.CharField(max_length=5, blank=True, null=True)
    nota19 = models.CharField(max_length=5, blank=True, null=True)
    nota20 = models.CharField(max_length=5, blank=True, null=True)
    nota21 = models.CharField(max_length=5, blank=True, null=True)
    nota22 = models.CharField(max_length=5, blank=True, null=True)
    nota23 = models.CharField(max_length=5, blank=True, null=True)
    nota24 = models.CharField(max_length=5, blank=True, null=True)
    nota25 = models.CharField(max_length=5, blank=True, null=True)
    nota26 = models.CharField(max_length=5, blank=True, null=True)
    nota27 = models.CharField(max_length=5, blank=True, null=True)
    nota28 = models.CharField(max_length=5, blank=True, null=True)
    nota29 = models.CharField(max_length=5, blank=True, null=True)
    nota30 = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_comportamiento'


class NotaDestreza(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    destreza_profesor = models.ForeignKey(DestrezaProfesor, models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    septiembre = models.CharField(max_length=5, blank=True, null=True)
    octubre = models.CharField(max_length=5, blank=True, null=True)
    noviembre = models.CharField(max_length=5, blank=True, null=True)
    diciembre = models.CharField(max_length=5, blank=True, null=True)
    enero = models.CharField(max_length=5, blank=True, null=True)
    febrero = models.CharField(max_length=5, blank=True, null=True)
    marzo = models.CharField(max_length=5, blank=True, null=True)
    abril = models.CharField(max_length=5, blank=True, null=True)
    mayo = models.CharField(max_length=5, blank=True, null=True)
    junio = models.CharField(max_length=5, blank=True, null=True)
    nota1 = models.CharField(max_length=5, blank=True, null=True)
    nota2 = models.CharField(max_length=5, blank=True, null=True)
    nota3 = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_destreza'


class Notificacion(models.Model):
    titulo = models.CharField(max_length=45)
    mensaje = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField()
    fecha_revision = models.DateTimeField()
    tiempo_bucle = models.IntegerField(blank=True, null=True)
    cantidad_mesaje = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=45, blank=True, null=True)
    visto = models.IntegerField()
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'


class NotificacionAlumno(models.Model):
    tipo_notificacion = models.ForeignKey('TipoNotificacion', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    notificacion_paralelo_id = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tema = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    archivo1 = models.CharField(max_length=45, blank=True, null=True)
    archivo2 = models.CharField(max_length=45, blank=True, null=True)
    archivo3 = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=1, blank=True, null=True)
    whatsapp = models.CharField(max_length=1, blank=True, null=True)
    sms = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion_alumno'


class NotificacionParalelo(models.Model):
    tipo_notificacion = models.ForeignKey('TipoNotificacion', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)
    tema = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    archivo1 = models.CharField(max_length=45, blank=True, null=True)
    archivo2 = models.CharField(max_length=45, blank=True, null=True)
    archivo3 = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=1, blank=True, null=True)
    whatsapp = models.CharField(max_length=1, blank=True, null=True)
    sms = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion_paralelo'


class NotificacionPariente(models.Model):
    tipo_notificacion = models.ForeignKey('TipoNotificacion', models.DO_NOTHING)
    pariente = models.ForeignKey('Pariente', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)
    tema = models.CharField(max_length=255, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    archivo1 = models.CharField(max_length=45, blank=True, null=True)
    archivo2 = models.CharField(max_length=45, blank=True, null=True)
    archivo3 = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion_pariente'


class Ocupacion(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocupacion'


class OrdenTrabajo(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    fecha = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    prioridad = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orden_trabajo'


class Pais(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    nacionalidad = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Paralelo(models.Model):
    curso = models.ForeignKey(Curso, models.DO_NOTHING)
    jornada = models.ForeignKey(Jornada, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    abreviatura = models.CharField(max_length=45, blank=True, null=True)
    aula = models.CharField(max_length=45, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    cupo = models.IntegerField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paralelo'


class ParaleloMateriaProfesor(models.Model):
    paralelo = models.ForeignKey(Paralelo, models.DO_NOTHING)
    materia = models.ForeignKey(Materia, models.DO_NOTHING)
    personal = models.ForeignKey('Personal', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    materia_padre = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    promedia = models.CharField(max_length=1, blank=True, null=True)
    promedia_comportamiento = models.CharField(max_length=1, blank=True, null=True)
    bloque = models.CharField(max_length=15, blank=True, null=True)
    clase = models.CharField(max_length=20, blank=True, null=True)
    personal_secundario_id = models.IntegerField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paralelo_materia_profesor'


class ParametroComportamiento(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    tipo = models.CharField(max_length=1, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametro_comportamiento'


class ParametroInicial(models.Model):
    periodo_academico = models.ForeignKey('PeriodoAcademico', models.DO_NOTHING)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    condicion_desde = models.CharField(max_length=5, blank=True, null=True)
    valor_desde = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    condicion_hasta = models.CharField(max_length=5, blank=True, null=True)
    valor_hasta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametro_inicial'


class Parentesco(models.Model):
    orden = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parentesco'


class Pariente(models.Model):
    estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING)
    profesion = models.ForeignKey('Profesion', models.DO_NOTHING)
    ocupacion = models.ForeignKey(Ocupacion, models.DO_NOTHING)
    parentesco = models.ForeignKey(Parentesco, models.DO_NOTHING)
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    escolaridad = models.ForeignKey(Escolaridad, models.DO_NOTHING)
    religion = models.ForeignKey('Religion', models.DO_NOTHING)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=1, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=15, blank=True, null=True)
    direccion_domicilio = models.CharField(max_length=200, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular = models.CharField(max_length=15, blank=True, null=True)
    lugar_ocupacion = models.CharField(max_length=500, blank=True, null=True)
    cargo_ocupacion = models.CharField(max_length=100, blank=True, null=True)
    direccion_ocupacion = models.CharField(max_length=200, blank=True, null=True)
    telefono_ocupacion = models.CharField(max_length=15, blank=True, null=True)
    es_facturacion = models.CharField(max_length=1, blank=True, null=True)
    es_representante = models.CharField(max_length=1, blank=True, null=True)
    vive_con_alumno = models.CharField(max_length=1, blank=True, null=True)
    ingreso_rol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)
    matrimonio_eclesiastico = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    @property
    def is_active(self):
        return True  
    
    @is_active.setter
    def is_active(self, value):
        pass
    
    @property
    def is_authenticated(self):
        return True  # Required for Django's authentication system

    @property
    def is_anonymous(self):
        return False

    @property
    def is_staff(self):
        return False  # Or implement actual staff logic if needed

    class Meta:
        managed = False
        db_table = 'pariente'
        db_table_comment = 'empleado'


class Parroquia(models.Model):
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)
    nombre = models.CharField(max_length=100)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquia'


class Perfil(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    skin = models.CharField(max_length=10, blank=True, null=True)
    generar = models.CharField(max_length=2, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'


class PerfilMenu(models.Model):
    menu = models.ForeignKey(Menu, models.DO_NOTHING)
    perfil = models.ForeignKey(Perfil, models.DO_NOTHING)
    escritura = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_menu'


class PerfilSeccion(models.Model):
    perfil = models.OneToOneField(Perfil, models.DO_NOTHING, primary_key=True)  # The composite primary key (perfil_id, seccion_id) found, that is not supported. The first column is selected.
    seccion = models.ForeignKey('Seccion', models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_seccion'
        unique_together = (('perfil', 'seccion'),)


class PeriodoAcademico(models.Model):
    institucion = models.ForeignKey(Institucion, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    abreviatura = models.CharField(max_length=45, blank=True, null=True)
    desde = models.DateTimeField(blank=True, null=True)
    hasta = models.DateTimeField(blank=True, null=True)
    valor_pension = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mes_control_pension = models.CharField(max_length=15, blank=True, null=True)
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_lunch = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dias_laborados_q1 = models.IntegerField(blank=True, null=True)
    dias_laborados_q2 = models.IntegerField(blank=True, null=True)
    nota_nacional = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nota_bi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    aportes_bloque = models.CharField(max_length=1, blank=True, null=True)
    activo = models.CharField(max_length=1, blank=True, null=True)
    activo_docente = models.CharField(max_length=1, blank=True, null=True)
    activo_pariente = models.CharField(max_length=1, blank=True, null=True)
    aportes_bloque_comportamiento = models.CharField(max_length=5, blank=True, null=True)
    califica_comportamiento = models.CharField(max_length=1, blank=True, null=True)
    tiene_inscripcion = models.CharField(max_length=1, blank=True, null=True)
    mostrar_notas = models.CharField(max_length=1, blank=True, null=True)
    insumo_quimestre = models.IntegerField(blank=True, null=True)
    esquema = models.CharField(max_length=1, blank=True, null=True)
    nota_academica_minima = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    nota_comportamiento_minima = models.CharField(max_length=5, blank=True, null=True)
    fecha_inicio_matricula = models.DateTimeField(blank=True, null=True)
    fecha_fin_matricula = models.DateTimeField(blank=True, null=True)
    calculo_promedio_anual = models.CharField(max_length=1, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_academico'


class Personal(models.Model):
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    provincia = models.ForeignKey('Provincia', models.DO_NOTHING)
    ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING)
    parroquia = models.ForeignKey(Parroquia, models.DO_NOTHING)
    escolaridad = models.ForeignKey(Escolaridad, models.DO_NOTHING)
    ruta_evacuacion = models.ForeignKey('RutaEvacuacion', models.DO_NOTHING)
    estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    apellido = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    tipo_identificacion = models.CharField(max_length=1, blank=True, null=True)
    numero_identificacion = models.CharField(max_length=15, blank=True, null=True)
    direccion_domicilio = models.CharField(max_length=255, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    telefono_celular = models.CharField(max_length=15, blank=True, null=True)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    antecedente_familiar = models.CharField(max_length=1000, blank=True, null=True)
    antecedente_personal = models.CharField(max_length=1000, blank=True, null=True)
    antecedente_quirurgico = models.TextField(blank=True, null=True)
    antecedente_ginecoobstetrico = models.TextField(blank=True, null=True)
    enfermedad_ocupacional = models.TextField(blank=True, null=True)
    alergia = models.TextField(blank=True, null=True)
    horas_suenio = models.IntegerField(blank=True, null=True)
    alimenticio = models.CharField(max_length=255, blank=True, null=True)
    miccional = models.CharField(max_length=255, blank=True, null=True)
    tabaquismo = models.CharField(max_length=45, blank=True, null=True)
    menarquia = models.CharField(max_length=45, blank=True, null=True)
    defecatorio = models.CharField(max_length=45, blank=True, null=True)
    alcoholismo = models.CharField(max_length=45, blank=True, null=True)
    ciclos = models.CharField(max_length=45, blank=True, null=True)
    otras_sustancias = models.CharField(max_length=45, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    antecedente_clinico = models.TextField(blank=True, null=True)
    antecedente_farmacologico = models.TextField(blank=True, null=True)
    antecedente_traumatico = models.TextField(blank=True, null=True)
    antecedente_psiquiatrico = models.TextField(blank=True, null=True)
    fum = models.CharField(max_length=255, blank=True, null=True)
    disminorrea = models.CharField(max_length=15, blank=True, null=True)
    gestas = models.IntegerField(blank=True, null=True)
    partos = models.IntegerField(blank=True, null=True)
    abortos = models.IntegerField(blank=True, null=True)
    cesareas = models.IntegerField(blank=True, null=True)
    hijos_vivos = models.IntegerField(blank=True, null=True)
    planificacion_familiar = models.CharField(max_length=255, blank=True, null=True)
    paptest = models.CharField(max_length=255, blank=True, null=True)
    inmunizaciones = models.TextField(blank=True, null=True)
    cardiovascular = models.CharField(max_length=255, blank=True, null=True)
    respiratorio = models.CharField(max_length=255, blank=True, null=True)
    digestivo = models.CharField(max_length=255, blank=True, null=True)
    genitourinario = models.CharField(max_length=255, blank=True, null=True)
    neurologico = models.CharField(max_length=255, blank=True, null=True)
    dermantologico = models.CharField(max_length=255, blank=True, null=True)
    ocular = models.CharField(max_length=255, blank=True, null=True)
    auditivo = models.CharField(max_length=255, blank=True, null=True)
    osteomuscular = models.CharField(max_length=255, blank=True, null=True)
    endocrino = models.CharField(max_length=255, blank=True, null=True)
    tension_arterial = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_cardiaca = models.CharField(max_length=255, blank=True, null=True)
    frecuencia_respiratoria = models.CharField(max_length=255, blank=True, null=True)
    temperatura = models.CharField(max_length=50, blank=True, null=True)
    saturacion_oxigeno = models.CharField(max_length=50, blank=True, null=True)
    talla = models.CharField(max_length=45, blank=True, null=True)
    peso = models.CharField(max_length=45, blank=True, null=True)
    imc = models.CharField(max_length=45, blank=True, null=True)
    piel = models.CharField(max_length=255, blank=True, null=True)
    ojos = models.CharField(max_length=255, blank=True, null=True)
    oidos = models.CharField(max_length=255, blank=True, null=True)
    nariz = models.CharField(max_length=255, blank=True, null=True)
    boca = models.CharField(max_length=255, blank=True, null=True)
    cuello = models.CharField(max_length=255, blank=True, null=True)
    torax = models.CharField(max_length=255, blank=True, null=True)
    abdomen = models.CharField(max_length=255, blank=True, null=True)
    genitales = models.CharField(max_length=255, blank=True, null=True)
    extremidades = models.CharField(max_length=255, blank=True, null=True)
    neurologico_examen = models.CharField(max_length=255, blank=True, null=True)
    descripcion_examen = models.TextField(blank=True, null=True)
    observacion_examen = models.TextField(blank=True, null=True)
    impresion_diagnostica = models.TextField(blank=True, null=True)
    recomendacion_examen = models.TextField(blank=True, null=True)
    antecedente_enfermedad_ocupacional = models.TextField(blank=True, null=True)
    informacion_ocupacional = models.TextField(blank=True, null=True)
    calle_principal = models.CharField(max_length=255, blank=True, null=True)
    calle_secundaria = models.CharField(max_length=255, blank=True, null=True)
    numero_casa = models.CharField(max_length=45, blank=True, null=True)
    referencia_domicilio = models.CharField(max_length=255, blank=True, null=True)
    email_institucional = models.CharField(max_length=255, blank=True, null=True)
    barrio = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    numero_hijos = models.IntegerField(blank=True, null=True)
    fecha_ingreso_institucion = models.DateField(blank=True, null=True)
    fecha_ingreso_docencia = models.DateField(blank=True, null=True)
    funcion = models.CharField(max_length=255, blank=True, null=True)
    tiene_discapacidad = models.CharField(max_length=2, blank=True, null=True)
    discapacidad = models.TextField(blank=True, null=True)
    link_evaluacion = models.TextField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal'
        db_table_comment = 'empleado'


class Profesion(models.Model):
    escolaridad = models.ForeignKey(Escolaridad, models.DO_NOTHING)
    nombre = models.CharField(max_length=250, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    abreviatura = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesion'


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    web = models.CharField(max_length=45, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=10, blank=True, null=True)
    telefono_movil = models.CharField(max_length=10, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Provincia(models.Model):
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincia'


class Rango(models.Model):
    periodo_academico = models.ForeignKey(PeriodoAcademico, models.DO_NOTHING)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rango'


class RecordAcademico(models.Model):
    alumno = models.ForeignKey(Alumno, models.DO_NOTHING)
    periodo_2do_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_2do_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_2do_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_3ro_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_3ro_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_3ro_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_4to_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_4to_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_4to_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_5to_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_5to_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_5to_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_6to_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_6to_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_6to_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_7mo_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_7mo_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_7mo_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_8vo_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_8vo_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_8vo_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_9no_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_9no_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_9no_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_10mo_basica = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_10mo_basica = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_10mo_basica = models.CharField(max_length=5, blank=True, null=True)
    periodo_1ro_bachillerato = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_1ro_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_1ro_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    periodo_2do_bachillerato = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_2do_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_2do_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    periodo_3ro_bachillerato = models.CharField(max_length=15, blank=True, null=True)
    aprovechamiento_3ro_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    comportamiento_3ro_bachillerato = models.CharField(max_length=5, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record_academico'


class Religion(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religion'


class RutaEvacuacion(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta_evacuacion'


class Seccion(models.Model):
    periodo_academico = models.ForeignKey(PeriodoAcademico, models.DO_NOTHING)
    orden = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    alias = models.CharField(max_length=45, blank=True, null=True)
    grupo = models.CharField(max_length=45, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seccion'


class SeccionEscala(models.Model):
    escala = models.ForeignKey(Escala, models.DO_NOTHING)
    seccion = models.ForeignKey(Seccion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seccion_escala'


class System(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=5)
    owner = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'system'


class TareaComunicado(models.Model):
    horario = models.ForeignKey(Horario, models.DO_NOTHING)
    leccionario = models.ForeignKey(Leccionario, models.DO_NOTHING)
    detalle = models.TextField()
    tipo = models.CharField(max_length=10)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_comunicado'


class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_equipo'


class TipoNotificacion(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_notificacion'


class TipoTecnologia(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_tecnologia'


class Titulo(models.Model):
    personal = models.ForeignKey(Personal, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    institucion = models.CharField(max_length=255, blank=True, null=True)
    origen = models.CharField(max_length=1, blank=True, null=True)
    tipo = models.CharField(max_length=2, blank=True, null=True)
    reconocido_por = models.CharField(max_length=255, blank=True, null=True)
    numero_registro_senescyt = models.CharField(max_length=45, blank=True, null=True)
    fecha_registro_senescyt = models.DateField(blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulo'


class Tutoria(models.Model):
    periodo_academico = models.ForeignKey(PeriodoAcademico, models.DO_NOTHING)
    paralelo = models.ForeignKey(Paralelo, models.DO_NOTHING)
    personal = models.ForeignKey(Personal, models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tutoria'


"""
Cambio por la autenticación
"""

BASE_KEY = b"Edu4trol@.#"

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, password=None, **extra_fields):
        if not usuario:
            raise ValueError("El usuario debe tener un nombre de usuario")
        user = self.model(usuario=usuario, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('es_superadmin', 'S')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('es_superadmin') != 'S':
            raise ValueError("El superusuario debe tener es_superadmin='S'")
        return self.create_user(usuario, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    
    personal = models.ForeignKey('Personal', models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.CharField(max_length=45, unique=True, blank=True, null=True)
    clave = models.CharField(max_length=200, blank=True, null=True)
    es_superadmin = models.CharField(max_length=1, blank=True, null=True)
    estado = models.CharField(max_length=1, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.pk} {self.nombre} {self.apellido}"

    @property
    def password(self):
        return self.clave

    @password.setter
    def password(self, raw_password):
        # Aquí puedes aplicar la lógica de encriptación que desees (o, en este caso, almacenar directamente el valor)
        # Si usas la lógica de CI4 para cifrar la contraseña, asegúrate de llamar a esa función aquí.
        self.clave = raw_password
    
    @property
    def is_active(self):
        return self.estado == 'A'
    
    @property
    def is_staff(self):
        return self.es_superadmin == 'S'
    
    @property
    def is_superuser(self):
        return self.es_superadmin == 'S'
    
    @property
    def last_login(self):
        return self.updated_at
        
    class Meta:
        #managed = False
        db_table = 'usuario'
        
    def set_password(self, raw_password):
        """
        Encripta la contraseña utilizando la función encrypt_ci4 y la almacena en 'clave'
        en formato base64.
        """
        encrypted = encrypt_ci4(raw_password.encode('utf-8'), BASE_KEY, raw_data=True)
        self.clave = base64.b64encode(encrypted).decode('utf-8')
        
    def check_password(self, raw_password):
        """
        Desencripta la contraseña almacenada y la compara con la contraseña sin procesar.
        """
        try:
            stored_encrypted = base64.b64decode(self.clave)
            decrypted = decrypt_ci4(stored_encrypted, BASE_KEY, raw_data=True).decode('utf-8')
        except Exception:
            return False
        return decrypted == raw_password


class UsuarioInstitucion(models.Model):
    usuario = models.OneToOneField(Usuario, models.DO_NOTHING, primary_key=True)  # The composite primary key (usuario_id, institucion_id) found, that is not supported. The first column is selected.
    institucion = models.ForeignKey(Institucion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_institucion'
        unique_together = (('usuario', 'institucion'),)


class UsuarioPerfil(models.Model):
    usuario = models.OneToOneField(Usuario, models.DO_NOTHING, primary_key=True)  # The composite primary key (usuario_id, perfil_id) found, that is not supported. The first column is selected.
    perfil = models.ForeignKey(Perfil, models.DO_NOTHING)
    created_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_id = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_perfil'
        unique_together = (('usuario', 'perfil'),)


"""
CONTROL DE ATRASOS
"""

class Atraso(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('J', 'Justificado'),
        ('I', 'Injustificado')
    ]

    alumno = models.ForeignKey('Alumno', 
                              on_delete=models.CASCADE,
                              related_name='atrasos')
    
    paralelo_materia_profesor = models.ForeignKey('ParaleloMateriaProfesor',
                                                on_delete=models.CASCADE,
                                                related_name='atrasos')
    
    periodo_academico = models.ForeignKey('PeriodoAcademico',
                                        on_delete=models.CASCADE,
                                        related_name='atrasos')
    
    fecha = models.DateField()
    hora = models.TimeField()
    minutos_atraso = models.PositiveIntegerField(default=0)
    
    estado = models.CharField(max_length=1,
                            choices=ESTADO_CHOICES,
                            default='P')
    
    observacion = models.TextField(blank=True, null=True)
    justificacion = models.TextField(blank=True, null=True)
    documento_justificacion = models.FileField(upload_to='justificaciones/', 
                                             blank=True, 
                                             null=True)
    
    created_by = models.ForeignKey('Usuario',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='atrasos_registrados')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'atraso'
        verbose_name = 'Atraso'
        verbose_name_plural = 'Atrasos'
        ordering = ['-fecha', '-hora']
        # Índices para mejorar consultas frecuentes
        indexes = [
            models.Index(fields=['alumno', 'fecha']),
            models.Index(fields=['estado']),
            models.Index(fields=['periodo_academico', 'paralelo_materia_profesor'])
        ]

    def __str__(self):
        return f"Atraso de {self.alumno} - {self.fecha} {self.hora}"

    def save(self, *args, **kwargs):
        # Calcular minutos de atraso basado en horario
        if not self.minutos_atraso:
            hora_actual = datetime.combine(self.fecha, self.hora)
            # Aquí podrías obtener la hora de inicio de la clase desde Horario
            # hora_clase = self.paralelo_materia_profesor.horario.hora_desde
            # self.minutos_atraso = (hora_actual - hora_clase).minutes
        super().save(*args, **kwargs)

    @property
    def is_justificado(self):
        return self.estado == 'J'

    def justificar(self, justificacion, usuario):
        self.estado = 'J'
        self.justificacion = justificacion
        self.updated_at = timezone.now()
        self.save()
