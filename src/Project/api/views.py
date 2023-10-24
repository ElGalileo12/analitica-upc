from django.http.response import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import InfoAcademica, SocioEconomica, Estudiante, Egresados , EgreMotivacion ,EgreAcademica, EgreLaboral 
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status
from .serializer import EstudianteAgrupadoSerializer, EgresadosAgrupadoSerializer, EstudianteSerializer
import json
# Create your views here.

class studentViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.select_related('socioeconomica', 'infoacademica').all()
    serializer_class = EstudianteAgrupadoSerializer

class EgresadoViewSet(viewsets.ModelViewSet):
    queryset = Egresados.objects.select_related('info_academica', 'info_laboral', 'info_motivacion').all()
    serializer_class = EgresadosAgrupadoSerializer

    
def registrar_Estudiante(request):
    #informacion personal
    if request.method == 'POST':
        try:
        # Obtener y analizar el cuerpo de la solicitud como JSON
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)
        
        # Obtener los datos enviados en la solicitud POST
        concat_info = data.get('concatInfo', {})
        estudiantes_info = concat_info.get('datosEstudiante', {})  
        ID_DOCUMENTO = estudiantes_info.get('ID_DOCUMENTO')
        ID_TIPO_DOCUMENTO = estudiantes_info.get('ID_TIPO_DOCUMENTO')
        ID_NOMBRE = estudiantes_info.get('ID_NOMBRE')
        ID_EDAD = estudiantes_info.get('ID_EDAD')
        ID_NUM_CONTACTO = estudiantes_info.get('ID_NUM_CONTACTO')
        ID_GENERO = estudiantes_info.get('ID_GENERO')
        ID_VIC_CONFLICTO = estudiantes_info.get('ID_VIC_CONFLICTO')
        ID_ESTADO_CIVIL = estudiantes_info.get('ID_ESTADO_CIVIL')
        ID_DPTO_NAC = estudiantes_info.get('ID_DPTO_NAC')
        ID_MUN_NAC = estudiantes_info.get('ID_MUN_NAC')
        ID_TIPO_DISC = estudiantes_info.get('ID_TIPO_DISC')
        ID_ETNIA = estudiantes_info.get('ID_ETNIA')
        ID_EMAIL = estudiantes_info.get('ID_EMAIL')
        ID_MAD_CAB_HOGAR = estudiantes_info.get('ID_MAD_CAB_HOGAR')
        ID_EDAD_MAYOR = estudiantes_info.get('ID_EDAD_MAYOR')
        ID_EDAD_MENOR = estudiantes_info.get('ID_EDAD_MENOR')
        ID_CANT_HIJOS = estudiantes_info.get('ID_CANT_HIJOS')
        ID_OCUP_MADRE = estudiantes_info.get('ID_OCUP_MADRE')
        ID_OCUP_PADRE = estudiantes_info.get('ID_OCUP_PADRE')
        ID_CANT_HERMANOS = estudiantes_info.get('ID_CANT_HERMANOS')
        ID_POS_HERMANO = estudiantes_info.get('ID_POS_HERMANO')
        ID_INTEGRANTES = estudiantes_info.get('ID_INTEGRANTES')
        ID_TALENTO = estudiantes_info.get('ID_TALENTO')
        ID_EPS = estudiantes_info.get('ID_EPS')
        ID_SISBEN = estudiantes_info.get('ID_SISBEN')
        ID_LENTES = estudiantes_info.get('ID_LENTES')

        #Tabla socio economica
        socioeco_info = concat_info.get('socioeconomica', {})
        ID_OCUPACION = socioeco_info.get('ID_OCUPACION')
        ID_ESTRATO = socioeco_info.get('ID_ESTRATO')
        ID_TIPO_VIVIENDA = socioeco_info.get('ID_TIPO_VIVIENDA')
        ID_RECIBE_INGRESOS = socioeco_info.get('ID_RECIBE_INGRESOS')
        ID_ACUDIENTE = socioeco_info.get('ID_ACUDIENTE')
        ID_NIVEL_ACADEMICO = socioeco_info.get('ID_NIVEL_ACADEMICO')
        ID_INGRESO_FAMILIAR = socioeco_info.get('ID_INGRESO_FAMILIAR')
        ID_TIENE_PC = socioeco_info.get('ID_TIENE_PC')
        ID_TIENE_INTERNET = socioeco_info.get('ID_TIENE_INTERNET')
        ID_CEL_SMART = socioeco_info.get('ID_CEL_SMART')
        ID_PLAN_DATOS = socioeco_info.get('ID_PLAN_DATOS')
        ID_INGRESO_TRABAJA = socioeco_info.get('ID_INGRESO_TRABAJA')
        #Tabla Academica
        acade_info = concat_info.get('infoacademica', {})
        ID_PROGR_ACTUAL = acade_info.get('ID_PROGR_ACTUAL')
        ID_HERMANOS_IES = acade_info.get('ID_HERMANOS_IES')
        ID_INGRESO_UPC = acade_info.get('ID_INGRESO_UPC')
        ID_INGRESO_OFERTA = acade_info.get('ID_INGRESO_OFERTA')
        ID_MOTIVACION = acade_info.get('ID_MOTIVACION')
        ID_VALIDO_BACH = acade_info.get('ID_VALIDO_BACH')
        ID_TIPO_COLEGIO = acade_info.get('ID_TIPO_COLEGIO')
        ID_SEMESTRE_INICIO = acade_info.get('ID_SEMESTRE_INICIO')
        ID_REPITIO_ICFES = acade_info.get('ID_REPITIO_ICFES')
        ID_PUNTAJE_ICFES = acade_info.get('ID_PUNTAJE_ICFES')
        ID_PUESTO_ICFES = acade_info.get('ID_PUESTO_ICFES')
        ID_LECTURA_CRITICA = acade_info.get('ID_LECTURA_CRITICA')
        ID_MATEMATICA = acade_info.get('ID_MATEMATICA')
        ID_CIUDADANOS = acade_info.get('ID_CIUDADANOS')
        ID_CIENCIAS = acade_info.get('ID_CIENCIAS')
        ID_INGLES = acade_info.get('ID_INGLES')
        ID_SEMESTRES_CURSADOS = acade_info.get('ID_SEMESTRES_CURSADOS')
        ID_UBICACION_SEMESTRE = acade_info.get('ID_UBICACION_SEMESTRE')
        ID_CREDITOS_APROBADOS = acade_info.get('ID_CREDITOS_APROBADOS')
        ID_PROMEDIO_ACUMULADO = acade_info.get('ID_PROMEDIO_ACUMULADO')
        ID_PROMEDIO_SEMESTRE_ANT = acade_info.get('ID_PROMEDIO_SEMESTRE_ANT')
        ID_CREDITOS_NO_APROBADOS = acade_info.get('ID_CREDITOS_NO_APROBADOS')
        ID_CREDITOS_MATRIC = acade_info.get('ID_CREDITOS_MATRIC')
        ID_MATERIAS_CANCELADAS = acade_info.get('ID_MATERIAS_CANCELADAS')
        ID_ASIGNATURA_ENCUESTA = acade_info.get('ID_ASIGNATURA_ENCUESTA')
        ID_JORNADA_ACAD = acade_info.get('ID_JORNADA_ACAD')
        ID_NOTA_ACTUAL = acade_info.get('ID_NOTA_ACTUAL')
        ID_RENDIMIENTO_ACTUAL = acade_info.get('ID_RENDIMIENTO_ACTUAL')
        ID_NIVEL_SATISFACION_ASIG = acade_info.get('ID_NIVEL_SATISFACION_ASIG')

        Std = Estudiante.objects.create(
                ID_DOCUMENTO=ID_DOCUMENTO,
                ID_TIPO_DOCUMENTO=ID_TIPO_DOCUMENTO,
                ID_NOMBRE=ID_NOMBRE,
                ID_EDAD=ID_EDAD,
                ID_NUM_CONTACTO=ID_NUM_CONTACTO,
                ID_GENERO=ID_GENERO,
                ID_VIC_CONFLICTO=ID_VIC_CONFLICTO,
                ID_ESTADO_CIVIL=ID_ESTADO_CIVIL,
                ID_DPTO_NAC=ID_DPTO_NAC,
                ID_MUN_NAC=ID_MUN_NAC,
                ID_TIPO_DISC=ID_TIPO_DISC,
                ID_ETNIA=ID_ETNIA,
                ID_EMAIL=ID_EMAIL,
                ID_MAD_CAB_HOGAR=ID_MAD_CAB_HOGAR,
                ID_EDAD_MAYOR=ID_EDAD_MAYOR,
                ID_EDAD_MENOR=ID_EDAD_MENOR,
                ID_CANT_HIJOS=ID_CANT_HIJOS,
                ID_OCUP_MADRE=ID_OCUP_MADRE,
                ID_OCUP_PADRE=ID_OCUP_PADRE,
                ID_CANT_HERMANOS=ID_CANT_HERMANOS,
                ID_POS_HERMANO=ID_POS_HERMANO,
                ID_INTEGRANTES=ID_INTEGRANTES,
                ID_TALENTO=ID_TALENTO,
                ID_EPS=ID_EPS,
                ID_SISBEN=ID_SISBEN,
                ID_LENTES=ID_LENTES )
        socioeco = SocioEconomica.objects.create(
                ID_ESTUDIANTE=Std,
                ID_OCUPACION=ID_OCUPACION,
                ID_ESTRATO=ID_ESTRATO,
                ID_TIPO_VIVIENDA=ID_TIPO_VIVIENDA,
                ID_RECIBE_INGRESOS=ID_RECIBE_INGRESOS,
                ID_ACUDIENTE=ID_ACUDIENTE,
                ID_NIVEL_ACADEMICO=ID_NIVEL_ACADEMICO,
                ID_INGRESO_FAMILIAR=ID_INGRESO_FAMILIAR,
                ID_TIENE_PC=ID_TIENE_PC,
                ID_TIENE_INTERNET=ID_TIENE_INTERNET,
                ID_CEL_SMART=ID_CEL_SMART,
                ID_PLAN_DATOS=ID_PLAN_DATOS,
                ID_INGRESO_TRABAJA=ID_INGRESO_TRABAJA
         )
    
        aca = InfoAcademica.objects.create(
                ID_ESTUDIANTE=Std,
                ID_PROGR_ACTUAL=ID_PROGR_ACTUAL,
                ID_HERMANOS_IES=ID_HERMANOS_IES,
                ID_INGRESO_UPC=ID_INGRESO_UPC,
                ID_INGRESO_OFERTA=ID_INGRESO_OFERTA,
                ID_MOTIVACION=ID_MOTIVACION,
                ID_VALIDO_BACH=ID_VALIDO_BACH,
                ID_TIPO_COLEGIO=ID_TIPO_COLEGIO,
                ID_SEMESTRE_INICIO=ID_SEMESTRE_INICIO,
                ID_REPITIO_ICFES=ID_REPITIO_ICFES,
                ID_PUNTAJE_ICFES=ID_PUNTAJE_ICFES,
                ID_PUESTO_ICFES=ID_PUESTO_ICFES,
                ID_LECTURA_CRITICA=ID_LECTURA_CRITICA,
                ID_MATEMATICA=ID_MATEMATICA,
                ID_CIUDADANOS=ID_CIUDADANOS,
                ID_CIENCIAS=ID_CIENCIAS,
                ID_INGLES=ID_INGLES,
                ID_SEMESTRES_CURSADOS=ID_SEMESTRES_CURSADOS,
                ID_UBICACION_SEMESTRE=ID_UBICACION_SEMESTRE,
                ID_CREDITOS_APROBADOS=ID_CREDITOS_APROBADOS,
                ID_PROMEDIO_ACUMULADO=ID_PROMEDIO_ACUMULADO,
                ID_PROMEDIO_SEMESTRE_ANT=ID_PROMEDIO_SEMESTRE_ANT,
                ID_CREDITOS_NO_APROBADOS=ID_CREDITOS_NO_APROBADOS,
                ID_CREDITOS_MATRIC=ID_CREDITOS_MATRIC,
                ID_MATERIAS_CANCELADAS=ID_MATERIAS_CANCELADAS,
                ID_ASIGNATURA_ENCUESTA=ID_ASIGNATURA_ENCUESTA,
                ID_JORNADA_ACAD=ID_JORNADA_ACAD,
                ID_NOTA_ACTUAL=ID_NOTA_ACTUAL,
                ID_RENDIMIENTO_ACTUAL=ID_RENDIMIENTO_ACTUAL,
                ID_NIVEL_SATISFACION_ASIG=ID_NIVEL_SATISFACION_ASIG
        )

        return HttpResponse("Registrado correctamente")
    else:
        return HttpResponseNotAllowed(['POST'])


def change_std(request):

    #informacion personal
    if request.method == 'POST':
        try:
        # Obtener y analizar el cuerpo de la solicitud como JSON
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)
        
        # Obtener los datos enviados en la solicitud POST
        concat_info = data.get('concatInfo', {})
        estudiantes_info = concat_info.get('datosEstudiante', {})  
        ID_c_DOCUMENTO = estudiantes_info.get('ID_DOCUMENTO')
        ID_TIPO_DOCUMENTO = estudiantes_info.get('ID_TIPO_DOCUMENTO')
        ID_NOMBRE = estudiantes_info.get('ID_NOMBRE')
        ID_EDAD = estudiantes_info.get('ID_EDAD')
        ID_NUM_CONTACTO = estudiantes_info.get('ID_NUM_CONTACTO')
        ID_GENERO = estudiantes_info.get('ID_GENERO')
        ID_VIC_CONFLICTO = estudiantes_info.get('ID_VIC_CONFLICTO')
        ID_ESTADO_CIVIL = estudiantes_info.get('ID_ESTADO_CIVIL')
        ID_DPTO_NAC = estudiantes_info.get('ID_DPTO_NAC')
        ID_MUN_NAC = estudiantes_info.get('ID_MUN_NAC')
        ID_TIPO_DISC = estudiantes_info.get('ID_TIPO_DISC')
        ID_ETNIA = estudiantes_info.get('ID_ETNIA')
        ID_EMAIL = estudiantes_info.get('ID_EMAIL')
        ID_MAD_CAB_HOGAR = estudiantes_info.get('ID_MAD_CAB_HOGAR')
        ID_EDAD_MAYOR = estudiantes_info.get('ID_EDAD_MAYOR')
        ID_EDAD_MENOR = estudiantes_info.get('ID_EDAD_MENOR')
        ID_CANT_HIJOS = estudiantes_info.get('ID_CANT_HIJOS')
        ID_OCUP_MADRE = estudiantes_info.get('ID_OCUP_MADRE')
        ID_OCUP_PADRE = estudiantes_info.get('ID_OCUP_PADRE')
        ID_CANT_HERMANOS = estudiantes_info.get('ID_CANT_HERMANOS')
        ID_POS_HERMANO = estudiantes_info.get('ID_POS_HERMANO')
        ID_INTEGRANTES = estudiantes_info.get('ID_INTEGRANTES')
        ID_TALENTO = estudiantes_info.get('ID_TALENTO')
        ID_EPS = estudiantes_info.get('ID_EPS')
        ID_SISBEN = estudiantes_info.get('ID_SISBEN')
        ID_LENTES = estudiantes_info.get('ID_LENTES')

        #Tabla socio economica
        socioeco_info = concat_info.get('socioeconomica', {})
        ID_OCUPACION = socioeco_info.get('ID_OCUPACION')
        ID_ESTRATO = socioeco_info.get('ID_ESTRATO')
        ID_TIPO_VIVIENDA = socioeco_info.get('ID_TIPO_VIVIENDA')
        ID_RECIBE_INGRESOS = socioeco_info.get('ID_RECIBE_INGRESOS')
        ID_ACUDIENTE = socioeco_info.get('ID_ACUDIENTE')
        ID_NIVEL_ACADEMICO = socioeco_info.get('ID_NIVEL_ACADEMICO')
        ID_INGRESO_FAMILIAR = socioeco_info.get('ID_INGRESO_FAMILIAR')
        ID_TIENE_PC = socioeco_info.get('ID_TIENE_PC')
        ID_TIENE_INTERNET = socioeco_info.get('ID_TIENE_INTERNET')
        ID_CEL_SMART = socioeco_info.get('ID_CEL_SMART')
        ID_PLAN_DATOS = socioeco_info.get('ID_PLAN_DATOS')
        ID_INGRESO_TRABAJA = socioeco_info.get('ID_INGRESO_TRABAJA')
        #Tabla Academica
        acade_info = concat_info.get('infoacademica', {})
        ID_PROGR_ACTUAL = acade_info.get('ID_PROGR_ACTUAL')
        ID_HERMANOS_IES = acade_info.get('ID_HERMANOS_IES')
        ID_INGRESO_UPC = acade_info.get('ID_INGRESO_UPC')
        ID_INGRESO_OFERTA = acade_info.get('ID_INGRESO_OFERTA')
        ID_MOTIVACION = acade_info.get('ID_MOTIVACION')
        ID_VALIDO_BACH = acade_info.get('ID_VALIDO_BACH')
        ID_TIPO_COLEGIO = acade_info.get('ID_TIPO_COLEGIO')
        ID_SEMESTRE_INICIO = acade_info.get('ID_SEMESTRE_INICIO')
        ID_REPITIO_ICFES = acade_info.get('ID_REPITIO_ICFES')
        ID_PUNTAJE_ICFES = acade_info.get('ID_PUNTAJE_ICFES')
        ID_PUESTO_ICFES = acade_info.get('ID_PUESTO_ICFES')
        ID_LECTURA_CRITICA = acade_info.get('ID_LECTURA_CRITICA')
        ID_MATEMATICA = acade_info.get('ID_MATEMATICA')
        ID_CIUDADANOS = acade_info.get('ID_CIUDADANOS')
        ID_CIENCIAS = acade_info.get('ID_CIENCIAS')
        ID_INGLES = acade_info.get('ID_INGLES')
        ID_SEMESTRES_CURSADOS = acade_info.get('ID_SEMESTRES_CURSADOS')
        ID_UBICACION_SEMESTRE = acade_info.get('ID_UBICACION_SEMESTRE')
        ID_CREDITOS_APROBADOS = acade_info.get('ID_CREDITOS_APROBADOS')
        ID_PROMEDIO_ACUMULADO = acade_info.get('ID_PROMEDIO_ACUMULADO')
        ID_PROMEDIO_SEMESTRE_ANT = acade_info.get('ID_PROMEDIO_SEMESTRE_ANT')
        ID_CREDITOS_NO_APROBADOS = acade_info.get('ID_CREDITOS_NO_APROBADOS')
        ID_CREDITOS_MATRIC = acade_info.get('ID_CREDITOS_MATRIC')
        ID_MATERIAS_CANCELADAS = acade_info.get('ID_MATERIAS_CANCELADAS')
        ID_ASIGNATURA_ENCUESTA = acade_info.get('ID_ASIGNATURA_ENCUESTA')
        ID_JORNADA_ACAD = acade_info.get('ID_JORNADA_ACAD')
        ID_NOTA_ACTUAL = acade_info.get('ID_NOTA_ACTUAL')
        ID_RENDIMIENTO_ACTUAL = acade_info.get('ID_RENDIMIENTO_ACTUAL')
        ID_NIVEL_SATISFACION_ASIG = acade_info.get('ID_NIVEL_SATISFACION_ASIG')
    
    
        Std_S = Estudiante.objects.get(ID_DOCUMENTO=ID_c_DOCUMENTO)
        
        Std_S.ID_TIPO_DOCUMENTO=ID_TIPO_DOCUMENTO
        Std_S.ID_NOMBRE=ID_NOMBRE
        Std_S.ID_EDAD=ID_EDAD
        Std_S.ID_NUM_CONTACTO=ID_NUM_CONTACTO
        Std_S.ID_GENERO=ID_GENERO
        Std_S.ID_VIC_CONFLICTO=ID_VIC_CONFLICTO
        Std_S.ID_ESTADO_CIVIL=ID_ESTADO_CIVIL
        Std_S.ID_DPTO_NAC=ID_DPTO_NAC
        Std_S.ID_MUN_NAC=ID_MUN_NAC
        Std_S.ID_TIPO_DISC=ID_TIPO_DISC
        Std_S.ID_ETNIA=ID_ETNIA
        Std_S.ID_EMAIL=ID_EMAIL
        Std_S.ID_MAD_CAB_HOGAR=ID_MAD_CAB_HOGAR
        Std_S.ID_EDAD_MAYOR=ID_EDAD_MAYOR
        Std_S.ID_EDAD_MENOR=ID_EDAD_MENOR
        Std_S.ID_CANT_HIJOS=ID_CANT_HIJOS
        Std_S.ID_OCUP_MADRE=ID_OCUP_MADRE
        Std_S.ID_OCUP_PADRE=ID_OCUP_PADRE
        Std_S.ID_CANT_HERMANOS=ID_CANT_HERMANOS
        Std_S.ID_POS_HERMANO=ID_POS_HERMANO
        Std_S.ID_INTEGRANTES=ID_INTEGRANTES
        Std_S.ID_TALENTO=ID_TALENTO
        Std_S.ID_EPS=ID_EPS
        Std_S.ID_SISBEN=ID_SISBEN
        Std_S.ID_LENTES=ID_LENTES 
        Std_S.save()
        
        socioeco_S = SocioEconomica.objects.get(ID_ESTUDIANTE=Std_S)
        
        socioeco_S.ID_OCUPACION=ID_OCUPACION
        socioeco_S.ID_ESTRATO=ID_ESTRATO
        socioeco_S.ID_TIPO_VIVIENDA=ID_TIPO_VIVIENDA
        socioeco_S.ID_RECIBE_INGRESOS=ID_RECIBE_INGRESOS
        socioeco_S.ID_ACUDIENTE=ID_ACUDIENTE
        socioeco_S.ID_NIVEL_ACADEMICO=ID_NIVEL_ACADEMICO
        socioeco_S.ID_INGRESO_FAMILIAR=ID_INGRESO_FAMILIAR
        socioeco_S.ID_TIENE_PC=ID_TIENE_PC
        socioeco_S.ID_TIENE_INTERNET=ID_TIENE_INTERNET
        socioeco_S.ID_CEL_SMART=ID_CEL_SMART
        socioeco_S.ID_PLAN_DATOS=ID_PLAN_DATOS
        socioeco_S.ID_INGRESO_TRABAJA=ID_INGRESO_TRABAJA
        
        socioeco_S.save()
        
        aca_S = InfoAcademica.objects.get(ID_ESTUDIANTE=Std_S)
        aca_S.ID_PROGR_ACTUAL=ID_PROGR_ACTUAL
        aca_S.ID_HERMANOS_IES=ID_HERMANOS_IES
        aca_S.ID_INGRESO_UPC=ID_INGRESO_UPC
        aca_S.ID_INGRESO_OFERTA=ID_INGRESO_OFERTA
        aca_S.ID_MOTIVACION=ID_MOTIVACION
        aca_S.ID_VALIDO_BACH=ID_VALIDO_BACH
        aca_S.ID_TIPO_COLEGIO=ID_TIPO_COLEGIO
        aca_S.ID_SEMESTRE_INICIO=ID_SEMESTRE_INICIO
        aca_S.ID_REPITIO_ICFES=ID_REPITIO_ICFES
        aca_S.ID_PUNTAJE_ICFES=ID_PUNTAJE_ICFES
        aca_S.ID_PUESTO_ICFES=ID_PUESTO_ICFES
        aca_S.ID_LECTURA_CRITICA=ID_LECTURA_CRITICA
        aca_S.ID_MATEMATICA=ID_MATEMATICA
        aca_S.ID_CIUDADANOS=ID_CIUDADANOS
        aca_S.ID_CIENCIAS=ID_CIENCIAS
        aca_S.ID_INGLES=ID_INGLES
        aca_S.ID_SEMESTRES_CURSADOS=ID_SEMESTRES_CURSADOS
        aca_S.ID_UBICACION_SEMESTRE=ID_UBICACION_SEMESTRE
        aca_S.ID_CREDITOS_APROBADOS=ID_CREDITOS_APROBADOS
        aca_S.ID_PROMEDIO_ACUMULADO=ID_PROMEDIO_ACUMULADO
        aca_S.ID_PROMEDIO_SEMESTRE_ANT=ID_PROMEDIO_SEMESTRE_ANT
        aca_S.ID_CREDITOS_NO_APROBADOS=ID_CREDITOS_NO_APROBADOS
        aca_S.ID_CREDITOS_MATRIC=ID_CREDITOS_MATRIC
        aca_S.ID_MATERIAS_CANCELADAS=ID_MATERIAS_CANCELADAS
        aca_S.ID_ASIGNATURA_ENCUESTA=ID_ASIGNATURA_ENCUESTA
        aca_S.ID_JORNADA_ACAD=ID_JORNADA_ACAD
        aca_S.ID_NOTA_ACTUAL=ID_NOTA_ACTUAL
        aca_S.ID_RENDIMIENTO_ACTUAL=ID_RENDIMIENTO_ACTUAL
        aca_S.ID_NIVEL_SATISFACION_ASIG=ID_NIVEL_SATISFACION_ASIG
        aca_S.save()

        return HttpResponse("Registrado correctamente")
    else:
        return HttpResponseNotAllowed(['POST'])

def registrar_Egresados(request):
    #informacion personal
    if request.method == 'POST':
        try:
        # Obtener y analizar el cuerpo de la solicitud como JSON
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)
        
        # Obtener los datos enviados en la solicitud POST
        concat_info = data.get('concatInfo', {})
        egresados_info = concat_info.get('datosEgresado', {})  
        ID_DOCUMENTO = egresados_info.get('ID_DOCUMENTO')
        ID_TIPO_DOCUMENTO = egresados_info.get('ID_TIPO_DOCUMENTO')
        ID_NOMBRE = egresados_info.get('ID_NOMBRE')
        ID_NUM_CONTACTO = egresados_info.get('ID_NUM_CONTACTO')
        ID_GENERO = egresados_info.get('ID_GENERO')
        ID_EDAD = egresados_info.get('ID_EDAD')
        ID_ESTADO_CIVIL = egresados_info.get('ID_ESTADO_CIVIL')
        ID_ETNIA = egresados_info.get('ID_ETNIA')
        ID_DISCAPACIDAD = egresados_info.get('ID_DISCAPACIDAD')
        ID_EMAIL = egresados_info.get('ID_EMAIL')
        ID_ESTRATO = egresados_info.get('ID_ESTRATO')


        #Tabla academica
        infoaca_info = concat_info.get('infoacademica', {})
        ID_TITULO = infoaca_info.get('ID_TITULO')
        ID_SEMESTRE_INICIO = infoaca_info.get('ID_SEMESTRE_INICIO')
        ID_SEMESTRES_CURSADOS = infoaca_info.get('ID_SEMESTRES_CURSADOS')
        ID_PROMEDIO_ACUMULADO = infoaca_info.get('ID_PROMEDIO_ACUMULADO')
        ID_SEMESTRE_FIN = infoaca_info.get('ID_SEMESTRE_FIN')
        ID_FECHA_GRADO = infoaca_info.get('ID_FECHA_GRADO')
        ID_SEGNDALENGUA = infoaca_info.get('ID_SEGNDALENGUA')
        ID_NIVEL = infoaca_info.get('ID_NIVEL')
        ID_PRACTICAS = infoaca_info.get('ID_PRACTICAS')
        ID_POSTGRADO = infoaca_info.get('ID_POSTGRADO')
        ID_POSTGRADO_NIVEL = infoaca_info.get('ID_POSTGRADO_NIVEL')
        ID_POSTGRADO_LUGAR = infoaca_info.get('ID_POSTGRADO_LUGAR')


        #Tabla Laboral
        labo_info = concat_info.get('infolaboral', {})
        ID_TRABAJA = labo_info.get('ID_TRABAJA')
        ID_TRABAJA_NOMBRE_EMPRESA = labo_info.get('ID_TRABAJA_NOMBRE_EMPRESA')
        ID_EXP_ACOMU = labo_info.get('ID_EXP_ACOMU')
        ID_TRABAJA_PAIS = labo_info.get('ID_TRABAJA_PAIS')
        ID_TRABAJA_CIUDAD = labo_info.get('ID_TRABAJA_CIUDAD')
        ID_TRABAJA_SITUACION = labo_info.get('ID_TRABAJA_SITUACION')
        ID_TRABAJA_PERFIL = labo_info.get('ID_TRABAJA_PERFIL')
        ID_TRABAJA_SECTOR = labo_info.get('ID_TRABAJA_SECTOR')
        ID_TRABAJA_TIEMPO = labo_info.get('ID_TRABAJA_TIEMPO')
        ID_TRABAJA_NIVEL = labo_info.get('ID_TRABAJA_NIVEL')
        ID_TRABAJA_TIEMPO_PRIMER = labo_info.get('ID_TRABAJA_TIEMPO_PRIMER')
        ID_TRABAJA_MEDIO = labo_info.get('ID_TRABAJA_MEDIO')
        ID_TRABAJA_SECTOR_DOS = labo_info.get('ID_TRABAJA_SECTOR_DOS')
        ID_TRABAJA_SECTOR_TRES = labo_info.get('ID_TRABAJA_SECTOR_TRES')
        ID_TRABAJA_REQUISITOS = labo_info.get('ID_TRABAJA_REQUISITOS')
        ID_TRABAJA_RANGO = labo_info.get('ID_TRABAJA_RANGO')
        ID_TRABAJA_RECONOCIMIENTO = labo_info.get('ID_TRABAJA_RECONOCIMIENTO')
        ID_EMPRESA = labo_info.get('ID_EMPRESA')
        ID_NOMBRE_EMPRESA = labo_info.get('ID_NOMBRE_EMPRESA')
        ID_UBICACION_EMPRESA = labo_info.get('ID_UBICACION_EMPRESA')
        ID_EMPRESA_ANTES = labo_info.get('ID_EMPRESA_ANTES')
        ID_EMPRESA_SECTOR = labo_info.get('ID_EMPRESA_SECTOR')

        #Tabla Motivacional
        Mot_info = concat_info.get('infomotivacion', {})
        ID_MOT_PREGRADO = Mot_info.get('ID_MOT_PREGRADO')
        ID_MOT_VOLUMEN = Mot_info.get('ID_MOT_VOLUMEN')
        ID_MOT_NIVELS = Mot_info.get('ID_MOT_NIVELS')
        ID_MOT_AMBIENTE = Mot_info.get('ID_MOT_AMBIENTE')
        ID_MOT_FORTALECER = Mot_info.get('ID_MOT_FORTALECER')
        ID_MOT_MATERIAS = Mot_info.get('ID_MOT_MATERIAS')
        ID_MOT_APOYO = Mot_info.get('ID_MOT_APOYO')
        ID_MOT_SERVICIO = Mot_info.get('ID_MOT_SERVICIO')
        ID_MOT_SERVICIO_DESEADO = Mot_info.get('ID_MOT_SERVICIO_DESEADO')
        ID_MOT_CARNET = Mot_info.get('ID_MOT_CARNET')
        ID_MOT_RECURSOS = Mot_info.get('ID_MOT_RECURSOS')
        ID_MOT_MODALIDAD = Mot_info.get('ID_MOT_MODALIDAD')
        ID_MOT_MODALIDAD_P = Mot_info.get('ID_MOT_MODALIDAD_P')
        ID_MOT_MODALIDAD_T = Mot_info.get('ID_MOT_MODALIDAD_T')
        ID_MOT_PROFUNDIZACION = Mot_info.get('ID_MOT_PROFUNDIZACION')
        ID_MOT_INGRESAR = Mot_info.get('ID_MOT_INGRESAR')
        ID_MOT_CONOCIMIENTOS = Mot_info.get('ID_MOT_CONOCIMIENTOS')
        ID_MOT_CONTRIBUCION = Mot_info.get('ID_MOT_CONTRIBUCION')
        ID_MOT_CALIDAD = Mot_info.get('ID_MOT_CALIDAD')
        ID_MOT_FAVORECIDO = Mot_info.get('ID_MOT_FAVORECIDO')
        ID_MOT_POST_CONT = Mot_info.get('ID_MOT_POST_CONT')


        Std = Egresados.objects.create(
            # Modelo Egresados
            ID_DOCUMENTO = ID_DOCUMENTO,
            ID_TIPO_DOCUMENTO = ID_TIPO_DOCUMENTO,
            ID_NOMBRE = ID_NOMBRE,
            ID_NUM_CONTACTO = ID_NUM_CONTACTO,
            ID_GENERO = ID_GENERO,
            ID_EDAD = ID_EDAD,
            ID_ESTADO_CIVIL = ID_ESTADO_CIVIL,
            ID_ETNIA = ID_ETNIA,
            ID_DISCAPACIDAD = ID_DISCAPACIDAD,
            ID_EMAIL = ID_EMAIL,
            ID_ESTRATO = ID_ESTRATO )

            # Modelo EgreAcademica
        Academica = EgreAcademica.objects.create(
            ID_EGRESADO = Std,
            ID_TITULO = ID_TITULO,
            ID_SEMESTRE_INICIO = ID_SEMESTRE_INICIO,
            ID_SEMESTRES_CURSADOS = ID_SEMESTRES_CURSADOS,
            ID_PROMEDIO_ACUMULADO = ID_PROMEDIO_ACUMULADO,
            ID_SEMESTRE_FIN = ID_SEMESTRE_FIN,
            ID_FECHA_GRADO = ID_FECHA_GRADO,
            ID_SEGNDALENGUA = ID_SEGNDALENGUA,
            ID_NIVEL = ID_NIVEL,
            ID_PRACTICAS = ID_PRACTICAS,
            ID_POSTGRADO = ID_POSTGRADO,
            ID_POSTGRADO_NIVEL = ID_POSTGRADO_NIVEL,
            ID_POSTGRADO_LUGAR = ID_POSTGRADO_LUGAR )

            # Modelo EgreLaboral
        Laboral = EgreLaboral.objects.create(
            ID_EGRESADO = Std,
            ID_TRABAJA = ID_TRABAJA,
            ID_TRABAJA_NOMBRE_EMPRESA = ID_TRABAJA_NOMBRE_EMPRESA,
            ID_EXP_ACOMU = ID_EXP_ACOMU,
            ID_TRABAJA_PAIS = ID_TRABAJA_PAIS,
            ID_TRABAJA_CIUDAD = ID_TRABAJA_CIUDAD,
            ID_TRABAJA_SITUACION = ID_TRABAJA_SITUACION,
            ID_TRABAJA_PERFIL = ID_TRABAJA_PERFIL,
            ID_TRABAJA_SECTOR = ID_TRABAJA_SECTOR,
            ID_TRABAJA_TIEMPO = ID_TRABAJA_TIEMPO,
            ID_TRABAJA_NIVEL = ID_TRABAJA_NIVEL,
            ID_TRABAJA_TIEMPO_PRIMER = ID_TRABAJA_TIEMPO_PRIMER,
            ID_TRABAJA_MEDIO = ID_TRABAJA_MEDIO,
            ID_TRABAJA_SECTOR_DOS = ID_TRABAJA_SECTOR_DOS,
            ID_TRABAJA_SECTOR_TRES = ID_TRABAJA_SECTOR_TRES,
            ID_TRABAJA_REQUISITOS = ID_TRABAJA_REQUISITOS,
            ID_TRABAJA_RANGO = ID_TRABAJA_RANGO,
            ID_TRABAJA_RECONOCIMIENTO = ID_TRABAJA_RECONOCIMIENTO,
            ID_EMPRESA = ID_EMPRESA,
            ID_NOMBRE_EMPRESA = ID_NOMBRE_EMPRESA,
            ID_UBICACION_EMPRESA = ID_UBICACION_EMPRESA,
            ID_EMPRESA_ANTES = ID_EMPRESA_ANTES,
            ID_EMPRESA_SECTOR = ID_EMPRESA_SECTOR)

            # Modelo EgreMotivacion
        mot = EgreMotivacion.objects.create(
            ID_EGRESADO = Std,
            ID_MOT_PREGRADO = ID_MOT_PREGRADO,
            ID_MOT_VOLUMEN = ID_MOT_VOLUMEN,
            ID_MOT_NIVELS = ID_MOT_NIVELS,
            ID_MOT_AMBIENTE = ID_MOT_AMBIENTE,
            ID_MOT_FORTALECER = ID_MOT_FORTALECER,
            ID_MOT_MATERIAS = ID_MOT_MATERIAS,
            ID_MOT_APOYO = ID_MOT_APOYO,
            ID_MOT_SERVICIO = ID_MOT_SERVICIO,
            ID_MOT_SERVICIO_DESEADO = ID_MOT_SERVICIO_DESEADO,
            ID_MOT_CARNET = ID_MOT_CARNET,
            ID_MOT_RECURSOS = ID_MOT_RECURSOS,
            ID_MOT_MODALIDAD = ID_MOT_MODALIDAD,
            ID_MOT_MODALIDAD_P = ID_MOT_MODALIDAD_P,
            ID_MOT_MODALIDAD_T = ID_MOT_MODALIDAD_T,
            ID_MOT_PROFUNDIZACION = ID_MOT_PROFUNDIZACION,
            ID_MOT_INGRESAR = ID_MOT_INGRESAR,
            ID_MOT_CONOCIMIENTOS = ID_MOT_CONOCIMIENTOS,
            ID_MOT_CONTRIBUCION = ID_MOT_CONTRIBUCION,
            ID_MOT_CALIDAD = ID_MOT_CALIDAD,
            ID_MOT_FAVORECIDO = ID_MOT_FAVORECIDO,
            ID_MOT_POST_CONT = ID_MOT_POST_CONT)

        

        return HttpResponse("Registrado correctamente")
    else:
        return HttpResponseNotAllowed(['POST'])

def change_egre(request):

        #informacion personal
    if request.method == 'POST':
        try:
        # Obtener y analizar el cuerpo de la solicitud como JSON
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON no válido'}, status=400)
        
        # Obtener los datos enviados en la solicitud POST
        concat_info = data.get('concatInfo', {})
        egresados_info = concat_info.get('datosEgresado', {})  
        ID_c_DOCUMENTO = egresados_info.get('ID_DOCUMENTO')
        ID_TIPO_DOCUMENTO = egresados_info.get('ID_TIPO_DOCUMENTO')
        ID_NOMBRE = egresados_info.get('ID_NOMBRE')
        ID_NUM_CONTACTO = egresados_info.get('ID_NUM_CONTACTO')
        ID_GENERO = egresados_info.get('ID_GENERO')
        ID_EDAD = egresados_info.get('ID_EDAD')
        ID_ESTADO_CIVIL = egresados_info.get('ID_ESTADO_CIVIL')
        ID_ETNIA = egresados_info.get('ID_ETNIA')
        ID_DISCAPACIDAD = egresados_info.get('ID_DISCAPACIDAD')
        ID_EMAIL = egresados_info.get('ID_EMAIL')
        ID_ESTRATO = egresados_info.get('ID_ESTRATO')

        #Tabla academica
        infoaca_info = concat_info.get('infoacademica', {})
        ID_TITULO = infoaca_info.get('ID_TITULO')
        ID_SEMESTRE_INICIO = infoaca_info.get('ID_SEMESTRE_INICIO')
        ID_SEMESTRES_CURSADOS = infoaca_info.get('ID_SEMESTRES_CURSADOS')
        ID_PROMEDIO_ACUMULADO = infoaca_info.get('ID_PROMEDIO_ACUMULADO')
        ID_SEMESTRE_FIN = infoaca_info.get('ID_SEMESTRE_FIN')
        ID_FECHA_GRADO = infoaca_info.get('ID_FECHA_GRADO')
        ID_SEGNDALENGUA = infoaca_info.get('ID_SEGNDALENGUA')
        ID_NIVEL = infoaca_info.get('ID_NIVEL')
        ID_PRACTICAS = infoaca_info.get('ID_PRACTICAS')
        ID_POSTGRADO = infoaca_info.get('ID_POSTGRADO')
        ID_POSTGRADO_NIVEL = infoaca_info.get('ID_POSTGRADO_NIVEL')
        ID_POSTGRADO_LUGAR = infoaca_info.get('ID_POSTGRADO_LUGAR')

        #Tabla Laboral
        labo_info = concat_info.get('infolaboral', {})
        ID_TRABAJA = labo_info.get('ID_TRABAJA')
        ID_TRABAJA_NOMBRE_EMPRESA = labo_info.get('ID_TRABAJA_NOMBRE_EMPRESA')
        ID_EXP_ACOMU = labo_info.get('ID_EXP_ACOMU')
        ID_TRABAJA_PAIS = labo_info.get('ID_TRABAJA_PAIS')
        ID_TRABAJA_CIUDAD = labo_info.get('ID_TRABAJA_CIUDAD')
        ID_TRABAJA_SITUACION = labo_info.get('ID_TRABAJA_SITUACION')
        ID_TRABAJA_PERFIL = labo_info.get('ID_TRABAJA_PERFIL')
        ID_TRABAJA_SECTOR = labo_info.get('ID_TRABAJA_SECTOR')
        ID_TRABAJA_TIEMPO = labo_info.get('ID_TRABAJA_TIEMPO')
        ID_TRABAJA_NIVEL = labo_info.get('ID_TRABAJA_NIVEL')
        ID_TRABAJA_TIEMPO_PRIMER = labo_info.get('ID_TRABAJA_TIEMPO_PRIMER')
        ID_TRABAJA_MEDIO = labo_info.get('ID_TRABAJA_MEDIO')
        ID_TRABAJA_SECTOR_DOS = labo_info.get('ID_TRABAJA_SECTOR_DOS')
        ID_TRABAJA_SECTOR_TRES = labo_info.get('ID_TRABAJA_SECTOR_TRES')
        ID_TRABAJA_REQUISITOS = labo_info.get('ID_TRABAJA_REQUISITOS')
        ID_TRABAJA_RANGO = labo_info.get('ID_TRABAJA_RANGO')
        ID_TRABAJA_RECONOCIMIENTO = labo_info.get('ID_TRABAJA_RECONOCIMIENTO')
        ID_EMPRESA = labo_info.get('ID_EMPRESA')
        ID_NOMBRE_EMPRESA = labo_info.get('ID_NOMBRE_EMPRESA')
        ID_UBICACION_EMPRESA = labo_info.get('ID_UBICACION_EMPRESA')
        ID_EMPRESA_ANTES = labo_info.get('ID_EMPRESA_ANTES')
        ID_EMPRESA_SECTOR = labo_info.get('ID_EMPRESA_SECTOR')

        #Tabla Motivacional
        Mot_info = concat_info.get('infomotivacion', {})
        ID_MOT_PREGRADO = Mot_info.get('ID_MOT_PREGRADO')
        ID_MOT_VOLUMEN = Mot_info.get('ID_MOT_VOLUMEN')
        ID_MOT_NIVELS = Mot_info.get('ID_MOT_NIVELS')
        ID_MOT_AMBIENTE = Mot_info.get('ID_MOT_AMBIENTE')
        ID_MOT_FORTALECER = Mot_info.get('ID_MOT_FORTALECER')
        ID_MOT_MATERIAS = Mot_info.get('ID_MOT_MATERIAS')
        ID_MOT_APOYO = Mot_info.get('ID_MOT_APOYO')
        ID_MOT_SERVICIO = Mot_info.get('ID_MOT_SERVICIO')
        ID_MOT_SERVICIO_DESEADO = Mot_info.get('ID_MOT_SERVICIO_DESEADO')
        ID_MOT_CARNET = Mot_info.get('ID_MOT_CARNET')
        ID_MOT_RECURSOS = Mot_info.get('ID_MOT_RECURSOS')
        ID_MOT_MODALIDAD = Mot_info.get('ID_MOT_MODALIDAD')
        ID_MOT_MODALIDAD_P = Mot_info.get('ID_MOT_MODALIDAD_P')
        ID_MOT_MODALIDAD_T = Mot_info.get('ID_MOT_MODALIDAD_T')
        ID_MOT_PROFUNDIZACION = Mot_info.get('ID_MOT_PROFUNDIZACION')
        ID_MOT_INGRESAR = Mot_info.get('ID_MOT_INGRESAR')
        ID_MOT_CONOCIMIENTOS = Mot_info.get('ID_MOT_CONOCIMIENTOS')
        ID_MOT_CONTRIBUCION = Mot_info.get('ID_MOT_CONTRIBUCION')
        ID_MOT_CALIDAD = Mot_info.get('ID_MOT_CALIDAD')
        ID_MOT_FAVORECIDO = Mot_info.get('ID_MOT_FAVORECIDO')
        ID_MOT_POST_CONT = Mot_info.get('ID_MOT_POST_CONT')
    
    
        Std_S = Egresados.objects.get(ID_DOCUMENTO=ID_c_DOCUMENTO)
        Std_S.ID_TIPO_DOCUMENTO = ID_TIPO_DOCUMENTO
        Std_S.ID_NOMBRE = ID_NOMBRE
        Std_S.ID_NUM_CONTACTO = ID_NUM_CONTACTO
        Std_S.ID_GENERO = ID_GENERO
        Std_S.ID_EDAD = ID_EDAD
        Std_S.ID_ESTADO_CIVIL = ID_ESTADO_CIVIL
        Std_S.ID_ETNIA = ID_ETNIA
        Std_S.ID_DISCAPACIDAD = ID_DISCAPACIDAD
        Std_S.ID_EMAIL = ID_EMAIL
        Std_S.ID_ESTRATO = ID_ESTRATO 
        Std_S.save()

        aca = EgreAcademica.objects.get(ID_EGRESADO=Std_S)
        
        aca.ID_TITULO = ID_TITULO
        aca.ID_SEMESTRE_INICIO = ID_SEMESTRE_INICIO
        aca.ID_SEMESTRES_CURSADOS = ID_SEMESTRES_CURSADOS
        aca.ID_PROMEDIO_ACUMULADO = ID_PROMEDIO_ACUMULADO
        aca.ID_SEMESTRE_FIN = ID_SEMESTRE_FIN
        aca.ID_FECHA_GRADO = ID_FECHA_GRADO
        aca.ID_SEGNDALENGUA = ID_SEGNDALENGUA
        aca.ID_NIVEL = ID_NIVEL
        aca.ID_PRACTICAS = ID_PRACTICAS
        aca.ID_POSTGRADO = ID_POSTGRADO
        aca.ID_POSTGRADO_NIVEL = ID_POSTGRADO_NIVEL
        aca.ID_POSTGRADO_LUGAR = ID_POSTGRADO_LUGAR
        aca.save()
        
        lab= EgreLaboral.objects.get(ID_EGRESADO=Std_S)
        lab.ID_TRABAJA = ID_TRABAJA
        lab.ID_TRABAJA_NOMBRE_EMPRESA = ID_TRABAJA_NOMBRE_EMPRESA
        lab.ID_EXP_ACOMU = ID_EXP_ACOMU
        lab.ID_TRABAJA_PAIS = ID_TRABAJA_PAIS
        lab.ID_TRABAJA_CIUDAD = ID_TRABAJA_CIUDAD
        lab.ID_TRABAJA_SITUACION = ID_TRABAJA_SITUACION
        lab.ID_TRABAJA_PERFIL = ID_TRABAJA_PERFIL
        lab.ID_TRABAJA_SECTOR = ID_TRABAJA_SECTOR
        lab.ID_TRABAJA_TIEMPO = ID_TRABAJA_TIEMPO
        lab.ID_TRABAJA_NIVEL = ID_TRABAJA_NIVEL
        lab.ID_TRABAJA_TIEMPO_PRIMER = ID_TRABAJA_TIEMPO_PRIMER
        lab.ID_TRABAJA_MEDIO = ID_TRABAJA_MEDIO
        lab.ID_TRABAJA_SECTOR_DOS = ID_TRABAJA_SECTOR_DOS
        lab.ID_TRABAJA_SECTOR_TRES = ID_TRABAJA_SECTOR_TRES
        lab.ID_TRABAJA_REQUISITOS = ID_TRABAJA_REQUISITOS
        lab.ID_TRABAJA_RANGO = ID_TRABAJA_RANGO
        lab.ID_TRABAJA_RECONOCIMIENTO = ID_TRABAJA_RECONOCIMIENTO
        lab.ID_EMPRESA = ID_EMPRESA
        lab.ID_NOMBRE_EMPRESA = ID_NOMBRE_EMPRESA
        lab.ID_UBICACION_EMPRESA = ID_UBICACION_EMPRESA
        lab.ID_EMPRESA_ANTES = ID_EMPRESA_ANTES
        lab.ID_EMPRESA_SECTOR = ID_EMPRESA_SECTOR
        lab.save()
        
        mot= EgreMotivacion.objects.get(ID_EGRESADO=Std_S)
        mot.ID_MOT_PREGRADO = ID_MOT_PREGRADO
        mot.ID_MOT_VOLUMEN = ID_MOT_VOLUMEN
        mot.ID_MOT_NIVELS = ID_MOT_NIVELS
        mot.ID_MOT_AMBIENTE = ID_MOT_AMBIENTE
        mot.ID_MOT_FORTALECER = ID_MOT_FORTALECER
        mot.ID_MOT_MATERIAS = ID_MOT_MATERIAS
        mot.ID_MOT_APOYO = ID_MOT_APOYO
        mot.ID_MOT_SERVICIO = ID_MOT_SERVICIO
        mot.ID_MOT_SERVICIO_DESEADO = ID_MOT_SERVICIO_DESEADO
        mot.ID_MOT_CARNET = ID_MOT_CARNET
        mot.ID_MOT_RECURSOS = ID_MOT_RECURSOS
        mot.ID_MOT_MODALIDAD = ID_MOT_MODALIDAD
        mot.ID_MOT_MODALIDAD_P = ID_MOT_MODALIDAD_P
        mot.ID_MOT_MODALIDAD_T = ID_MOT_MODALIDAD_T
        mot.ID_MOT_PROFUNDIZACION = ID_MOT_PROFUNDIZACION
        mot.ID_MOT_INGRESAR = ID_MOT_INGRESAR
        mot.ID_MOT_CONOCIMIENTOS = ID_MOT_CONOCIMIENTOS
        mot.ID_MOT_CONTRIBUCION = ID_MOT_CONTRIBUCION
        mot.ID_MOT_CALIDAD = ID_MOT_CALIDAD
        mot.ID_MOT_FAVORECIDO = ID_MOT_FAVORECIDO
        mot.ID_MOT_POST_CONT = ID_MOT_POST_CONT
        mot.save()
        return HttpResponse("Registrado correctamente")
    else:
        return HttpResponseNotAllowed(['POST'])
@api_view(['GET'])      
def dashboard(request):
    Total=Estudiante.objects.count()
    context = {'total_estudiantes': Total}
    print(context)
    return render(request, "fp.html",context)

@api_view(['GET'])         
def get_chart(_request):  
        A=len(Estudiante.objects.filter(ID_GENERO=2))
        B=len(Estudiante.objects.filter(ID_GENERO=1))
        C=len(Estudiante.objects.filter(ID_GENERO=0))
        Total=Estudiante.objects.count()
        chart = {
            'a' : A,
            'b' : B,
            'c' : C,
            't' : Total,
        }
        return Response(chart)
    
@api_view(['GET'])
def get_chart_2(_request): 
    sixy = Estudiante.objects.filter(ID_GENERO=2)
    A = InfoAcademica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy])
    A = A.filter(ID_SEMESTRE_INICIO__lte=12)      
    sixy_m = Estudiante.objects.filter(ID_GENERO=1)
    B = InfoAcademica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy_m])
    B = B.filter(ID_SEMESTRE_INICIO__lte=12) 
    chart_2 = {
            'a' : len(A),
            'b' : len(B),
        }
    return Response(chart_2)

@api_view(['GET'])
def get_chart_3(_request): 
    sixy = Estudiante.objects.filter(ID_GENERO=2,ID_CANT_HIJOS__gt=0)  
    sixy_m = Estudiante.objects.filter(ID_GENERO=1,ID_CANT_HIJOS__gt=0)
    chart_3 = {
            'a' : len(sixy),
            'b' : len(sixy_m ),
        }
    return Response(chart_3)
@api_view(['GET'])
def get_chart_4(_request): 
    sixy = Estudiante.objects.filter(ID_GENERO=2)
    A = SocioEconomica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy])
    A = A.exclude(ID_OCUPACION=1)      
    sixy_m = Estudiante.objects.filter(ID_GENERO=1)
    B = SocioEconomica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy_m])
    B = B.exclude(ID_OCUPACION=1)
    sixy_o = Estudiante.objects.filter(ID_GENERO=0)
    C = SocioEconomica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy_o])
    C = C.exclude(ID_OCUPACION=1)  
    chart_4 = {
            'a' : len(A),
            'b' : len(B),
            'c' : len(C)
        }
    return Response(chart_4)

@api_view(['GET'])
def get_chart_5(_request): 
    #Extraigo los estudiantes con motivaciones bajo,medio,alto,exc
    Bajo = InfoAcademica.objects.filter(ID_MOTIVACION=1) 
    Medio = InfoAcademica.objects.filter(ID_MOTIVACION=2) 
    Alto = InfoAcademica.objects.filter(ID_MOTIVACION=3) 
    Excelente = InfoAcademica.objects.filter(ID_MOTIVACION=4)
    #Relaciono los estudiantes con motivaciones de la tabla academica con la tabla estudiante
    
    A = Estudiante.objects.filter(ID_DOCUMENTO__in=[estudiante.pk for estudiante in Bajo])
    B = Estudiante.objects.filter(ID_DOCUMENTO__in=[estudiante.pk for estudiante in Medio])
    C = Estudiante.objects.filter(ID_DOCUMENTO__in=[estudiante.pk for estudiante in Alto])
    D = Estudiante.objects.filter(ID_DOCUMENTO__in=[estudiante.pk for estudiante in Excelente])
    #Filtro por genero cada motivacion
    #Bajo
    A1 = A.filter(ID_GENERO=1)
    A2 = A.filter(ID_GENERO=2)
    A3 = A.filter(ID_GENERO=0)
    #Medio
    B1 = B.filter(ID_GENERO=1)
    B2 = B.filter(ID_GENERO=2)
    B3 = B.filter(ID_GENERO=0)
    #Alto
    C1 = C.filter(ID_GENERO=1)
    C2 = C.filter(ID_GENERO=2)
    C3 = C.filter(ID_GENERO=0)
    #EXC
    D1 = D.filter(ID_GENERO=1)
    D2 = D.filter(ID_GENERO=2)
    D3 = D.filter(ID_GENERO=0)
    chart_5 = {
            'a1' : len(A1),
            'a2' : len(A2),
            'b1' : len(B1),
            'b2' : len(B2),
            'c1' : len(C1),
            'c2' : len(C2),
            'c3' : len(C3),
            'd1' : len(D1),
            'd2' : len(D2)
        }
    return Response(chart_5)

@api_view(['GET'])
def get_chart_6(_request): 
    YF =  Estudiante.objects.filter(ID_VIC_CONFLICTO=1,ID_GENERO=2) 
    NF =  Estudiante.objects.filter(ID_VIC_CONFLICTO=2,ID_GENERO=2)
    YM =  Estudiante.objects.filter(ID_VIC_CONFLICTO=1,ID_GENERO=1) 
    NM =  Estudiante.objects.filter(ID_VIC_CONFLICTO=2,ID_GENERO=1) 
    YO =  Estudiante.objects.filter(ID_VIC_CONFLICTO=1,ID_GENERO=0)
    NO =  Estudiante.objects.filter(ID_VIC_CONFLICTO=2,ID_GENERO=0)
    chart_6 = {
            'yf' : len(YF),
            'nf' : len(NF),
            'ym' : len(YM),
            'nm' : len(NM),
            'yo' : len(YO),
            'no' : len(NO),
        }
    return Response(chart_6)

@api_view(['GET'])
def get_chart_7(_request): 
    YF =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=1,ID_GENERO=2) 
    NF =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=2,ID_GENERO=2)
    YM =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=1,ID_GENERO=1) 
    NM =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=2,ID_GENERO=1) 
    YO =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=1,ID_GENERO=0)
    NO =  Estudiante.objects.filter(ID_MAD_CAB_HOGAR=2,ID_GENERO=0)
    chart_7 = {
            'yf' : len(YF),
            'nf' : len(NF),
            'ym' : len(YM),
            'nm' : len(NM),
            'yo' : len(YO),
            'no' : len(NO),
        }
    return Response(chart_7)