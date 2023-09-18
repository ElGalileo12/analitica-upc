from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Estudiante , SocioEconomica, InfoAcademica
from django.views.generic import ListView
from random import randrange

from rest_framework import viewsets
from .serializer import EstudianteAgrupadoSerializer

# Create your views here.

class studentViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.select_related('socioeconomica', 'infoacademica').all()
    serializer_class = EstudianteAgrupadoSerializer

class EstdListView(ListView):
    model = Estudiante
    template_name = 'home.html'

    def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
        return Estudiante.objects.all()

   
    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
       
        print(context)
        return context 


#class homelist(ListView):
 #   model = Curso
  #  template_name = 'home.html'

   # def get_queryset(self):
        # return Curso.objects.filter(creditos__lte=4)
    #    return Curso.objects.all()

    #def get_context_data(self, **kwargs):
       # context = super().get_context_data(**kwargs)
       # print(context)
        #return context
    
def registrar_Estudiante(request):
    #informacion personal
    ID_DOCUMENTO = request.POST['ID_DOCUMENTO']
    ID_TIPO_DOCUMENTO = request.POST['ID_TIPO_DOCUMENTO']
    ID_NOMBRE = request.POST['ID_NOMBRE']
    ID_EDAD = request.POST['ID_EDAD']
    ID_NUM_CONTACTO = request.POST['ID_NUM_CONTACTO']
    ID_GENERO = request.POST['ID_GENERO']
    ID_VIC_CONFLICTO = request.POST['ID_VIC_CONFLICTO']
    ID_ESTADO_CIVIL = request.POST['ID_ESTADO_CIVIL']
    ID_DPTO_NAC = request.POST['ID_DPTO_NAC']
    ID_MUN_NAC = request.POST['ID_MUN_NAC']
    ID_TIPO_DISC = request.POST['ID_TIPO_DISC']
    ID_ETNIA = request.POST['ID_ETNIA']
    ID_EMAIL = request.POST['ID_EMAIL']
    ID_MAD_CAB_HOGAR = request.POST['ID_MAD_CAB_HOGAR']
    ID_EDAD_MAYOR = request.POST['ID_EDAD_MAYOR']
    ID_EDAD_MENOR = request.POST['ID_EDAD_MENOR']
    ID_CANT_HIJOS = request.POST['ID_CANT_HIJOS']
    ID_OCUP_MADRE = request.POST['ID_OCUP_MADRE']
    ID_OCUP_PADRE = request.POST['ID_OCUP_PADRE']
    ID_CANT_HERMANOS = request.POST['ID_CANT_HERMANOS']
    ID_POS_HERMANO = request.POST['ID_POS_HERMANO']
    ID_INTEGRANTES = request.POST['ID_INTEGRANTES']
    ID_TALENTO = request.POST['ID_TALENTO']
    ID_EPS = request.POST['ID_EPS']
    ID_SISBEN = request.POST['ID_SISBEN']
    ID_LENTES = request.POST['ID_LENTES']
    #Tabla socio economica
    ID_OCUPACION = request.POST['ID_OCUPACION']
    ID_ESTRATO = request.POST['ID_ESTRATO']
    ID_TIPO_VIVIENDA = request.POST['ID_TIPO_VIVIENDA']
    ID_RECIBE_INGRESOS = request.POST['ID_RECIBE_INGRESOS']
    ID_ACUDIENTE = request.POST['ID_ACUDIENTE']
    ID_NIVEL_ACADEMICO = request.POST['ID_NIVEL_ACADEMICO']
    ID_INGRESO_FAMILIAR = request.POST['ID_INGRESO_FAMILIAR']
    ID_TIENE_PC = request.POST['ID_TIENE_PC']
    ID_TIENE_INTERNET = request.POST['ID_TIENE_INTERNET']
    ID_CEL_SMART = request.POST['ID_CEL_SMART']
    ID_PLAN_DATOS = request.POST['ID_PLAN_DATOS']
    ID_INGRESO_TRABAJA = request.POST['ID_INGRESO_TRABAJA']
    #Tabla Academica
    ID_PROGR_ACTUAL = request.POST['ID_PROGR_ACTUAL']
    ID_HERMANOS_IES = request.POST['ID_HERMANOS_IES']
    ID_INGRESO_UPC = request.POST['ID_INGRESO_UPC']
    ID_INGRESO_OFERTA = request.POST['ID_INGRESO_OFERTA']
    ID_MOTIVACION = request.POST['ID_MOTIVACION']
    ID_VALIDO_BACH = request.POST['ID_VALIDO_BACH']
    ID_TIPO_COLEGIO = request.POST['ID_TIPO_COLEGIO']
    ID_SEMESTRE_INICIO = request.POST['ID_SEMESTRE_INICIO']
    ID_REPITIO_ICFES = request.POST['ID_REPITIO_ICFES']
    ID_PUNTAJE_ICFES = request.POST['ID_PUNTAJE_ICFES']
    ID_PUESTO_ICFES = request.POST['ID_PUESTO_ICFES']
    ID_LECTURA_CRITICA = request.POST['ID_LECTURA_CRITICA']
    ID_MATEMATICA = request.POST['ID_MATEMATICA']
    ID_CIUDADANOS = request.POST['ID_CIUDADANOS']
    ID_CIENCIAS = request.POST['ID_CIENCIAS']
    ID_INGLES = request.POST['ID_INGLES']
    ID_SEMESTRES_CURSADOS = request.POST['ID_SEMESTRES_CURSADOS']
    ID_UBICACION_SEMESTRE = request.POST['ID_UBICACION_SEMESTRE']
    ID_CREDITOS_APROBADOS = request.POST['ID_CREDITOS_APROBADOS']
    ID_PROMEDIO_ACUMULADO = request.POST['ID_PROMEDIO_ACUMULADO']
    ID_PROMEDIO_SEMESTRE_ANT = request.POST['ID_PROMEDIO_SEMESTRE_ANT']
    ID_CREDITOS_NO_APROBADOS = request.POST['ID_CREDITOS_NO_APROBADOS']
    ID_CREDITOS_MATRIC = request.POST['ID_CREDITOS_MATRIC']
    ID_MATERIAS_CANCELADAS = request.POST['ID_MATERIAS_CANCELADAS']
    ID_ASIGNATURA_ENCUESTA = request.POST['ID_ASIGNATURA_ENCUESTA']
    ID_JORNADA_ACAD = request.POST['ID_JORNADA_ACAD']
    ID_NOTA_ACTUAL = request.POST['ID_NOTA_ACTUAL']
    ID_RENDIMIENTO_ACTUAL = request.POST['ID_RENDIMIENTO_ACTUAL']
    ID_NIVEL_SATISFACION_ASIG = request.POST['ID_NIVEL_SATISFACION_ASIG']
    
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
    return redirect('/api/home')

def consultas_p(request):
    return render(request, "consulta.html")
    
def consultastd(request):
    if request.method == 'POST':
        ID_C_DOCUMENTO = request.POST['ID_C_DOCUMENTO']
        try:
                Std_c = Estudiante.objects.get(ID_DOCUMENTO=ID_C_DOCUMENTO)
                Std_s = SocioEconomica.objects.get(ID_ESTUDIANTE=ID_C_DOCUMENTO)
                Std_a = InfoAcademica.objects.get(ID_ESTUDIANTE=ID_C_DOCUMENTO)
                
                #TRADUCCIONES TABLA ESTUDIANTES
                Genero = {0:'otro',1:'Masculino',2:'Femenino'}
                Std_c.ID_GENERO = Genero.get(Std_c.ID_GENERO)

                Victima_con = {1:'Si',2:'No'}
                Std_c.ID_VIC_CONFLICTO = Victima_con.get(Std_c.ID_VIC_CONFLICTO)
                
                # Diccionario para ESTADO_CIVIL
                ESTADO_CIVIL = {
                    1: 'Casado',
                    2: 'Separado',
                    3: 'Soltero',
                    4: 'Unión libre',
                    5: 'Viudo'
                }
                Std_c.ID_ESTADO_CIVIL = ESTADO_CIVIL.get(Std_c.ID_ESTADO_CIVIL)
                # Diccionario para TIPO_DISC
                TIPO_DISC = {
                    1: 'Movilidad reducida',
                    2: 'Ninguna',
                    3: 'Auditiva',
                    4: 'Visual'
                }
                Std_c.ID_TIPO_DISC = TIPO_DISC.get(Std_c.ID_TIPO_DISC)
                # Diccionario para ETNIA
                ETNIA = {
                    1: 'Indigena',
                    2: 'Palenquero',
                    3: 'Sin distincion racial',
                    4: 'Negro, mulato, afrodescendiente, afrocolombiano',
                    5: 'Raizal'
                }
                Std_c.ID_ETNIA = ETNIA.get(Std_c.ID_ETNIA)
                # Diccionario para MAD_CAB_HOGAR
                MAD_CAB_HOGAR = {
                    0: 'nRegistra',
                    1: 'Sí',
                    2: 'No'
                }
                Std_c.ID_MAD_CAB_HOGAR = MAD_CAB_HOGAR.get(Std_c.ID_MAD_CAB_HOGAR)
                # Diccionario para OCUP_MADRE
                OCUP_MADRE = {
                    0: 'nRegistra',
                    1: 'amaCasa',
                    2: 'Estudiante',
                    3: 'Fallecida',
                    4: 'Independiente',
                    5: 'Labora',
                    6: 'MadreCabezaHogar',
                    7: 'Pensionada'
                }
                Std_c.ID_OCUP_MADRE = OCUP_MADRE.get(Std_c.ID_OCUP_MADRE)
                # Diccionario para OCUP_PADRE
                OCUP_PADRE = {
                    0: 'nRegistra',
                    1: 'PadreCabezaHogar',
                    2: 'Pensionado',
                    3: 'Fallecido',
                    4: 'Independiente',
                    5: 'Labora'
                }
                Std_c.ID_OCUP_PADRE = OCUP_PADRE.get(Std_c.ID_OCUP_PADRE)
                # Diccionario para TALENTO
                TALENTO = {
                    0: 'nRegistra',
                    1: 'Actor',
                    2: 'Atletismo',
                    3: 'Bailarin',
                    4: 'Baloncesto',
                    5: 'Fútbol',
                    6: 'Fútbol sala',
                    7: 'Músico',
                    8: 'Natación',
                    9: 'Softbol',
                    10: 'Taewondo',
                    11: 'Tenis de mesa',
                    12: 'Voleibol'
                }
                Std_c.ID_TALENTO = TALENTO.get(Std_c.ID_TALENTO)
                # Diccionario para EPS
                EPS = {
                    0: 'nRegistra',
                    1: 'Sí',
                    2: 'No'
                }
                Std_c.ID_EPS = EPS.get(Std_c.ID_EPS)
                # Diccionario para LENTES
                LENTES = {
                    0: 'nRegistra',
                    1: 'Sí',
                    2: 'No'
                }
                Std_c.ID_LENTES = LENTES.get(Std_c.ID_LENTES)
                #TRADUCCIONES TABLA SOCIO-ECONOMICAS
                # Diccionario para OCUPACION
                OCUPACION = {
                    1: 'Únicamente estudiante',
                    2: 'Empleado',
                    3: 'Independiente',
                    4: 'Trabaja medio tiempo',
                    5: 'Trabaja tiempo completo'
                }
                Std_s.ID_OCUPACION = OCUPACION.get(Std_s.ID_OCUPACION)
                # Diccionario para TIPO_VIVIENDA
                TIPO_VIVIENDA = {
                    1: 'Familiar',
                    2: 'Propia',
                    3: 'Arrendada',
                    4: 'Otra'
                }
                Std_s.ID_TIPO_VIVIENDA = TIPO_VIVIENDA.get(Std_s.ID_TIPO_VIVIENDA)
                # Diccionario para RECIBE_INGRESOS
                RECIBE_INGRESOS = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_RECIBE_INGRESOS = RECIBE_INGRESOS.get(Std_s.ID_RECIBE_INGRESOS)
                # Diccionario para ACUDIENTE
                ACUDIENTE = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_ACUDIENTE = ACUDIENTE.get(Std_s.ID_ACUDIENTE)
                # Diccionario para NIVEL_ACADEMICO
                NIVEL_ACADEMICO = {
                    1: 'Bachiller',
                    2: 'Tecnico',
                    3: 'Tecnico Bachiller',
                    4: 'Tecnologo',
                    5: 'Universitario'
                }
                Std_s.ID_NIVEL_ACADEMICO = NIVEL_ACADEMICO.get(Std_s.ID_NIVEL_ACADEMICO)
                # Diccionario para TIENE_PC
                TIENE_PC = {
                    0: 'No Registra',
                    1: 'Sí',
                    2: 'No'
                }   
                Std_s.ID_TIENE_PC = TIENE_PC.get(Std_s.ID_TIENE_PC)
                # Diccionario para TIENE_INTERNET
                TIENE_INTERNET = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_TIENE_INTERNET = TIENE_INTERNET.get(Std_s.ID_TIENE_INTERNET)
                # Diccionario para CEL_SMART
                CEL_SMART = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_CEL_SMART = CEL_SMART.get(Std_s.ID_CEL_SMART)
                # Diccionario para PLAN_DATOS
                PLAN_DATOS = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_PLAN_DATOS = PLAN_DATOS.get(Std_s.ID_PLAN_DATOS)
                # Diccionario para INGRESO_TRABAJA
                INGRESO_TRABAJA = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_s.ID_INGRESO_TRABAJA = INGRESO_TRABAJA.get(Std_s.ID_INGRESO_TRABAJA)
                #TRADUCCIONES TABLA ACADEMICA
                # Diccionario para PROGR_ACTUAL
                PROGR_ACTUAL = {
                    22: 'Lic. en Arte',
                    21: 'Lic. Ciencias naturales',
                    20: 'Lic. Educacion Fisica',
                    19: 'Musica',
                    18: 'Lic. en Castellano',
                    17: 'Lic. Español e ingles',
                    16: 'Administracion de empresas',
                    15: 'Ing. de Sistemas',
                    14: 'Ing. Ambiental',
                    13: 'Ing. Agroindustrial',
                    12: 'Comercio Internacional',
                    11: 'Instrumentacion',
                    10: 'Enfermeria',
                    9: 'Sociologia',
                    8: 'Administracion Turistica',
                    7: 'Derecho',
                    6: 'Economia',
                    5: 'Contaduria publica',
                    4: 'No registra',
                    3: 'Psicologia',
                    2: 'Microbiologia',
                    1: 'Ing. Electronica'
                }
                Std_a.ID_PROGR_ACTUAL = PROGR_ACTUAL.get(Std_a.ID_PROGR_ACTUAL)
                # Diccionario para INGRESO_UPC
                INGRESO_UPC = {
                    1: 'Preuniversitario',
                    2: 'Aspirante regular',
                    3: 'Perteneciente a cabildo indigena',
                    4: 'Reintegro',
                    5: 'ReservaCupo',
                    6: 'TransExterna',
                    7: 'TransInterna',
                    8: 'Otro',
                    9: 'Deportista destacado'
                }
                Std_a.ID_INGRESO_UPC = INGRESO_UPC.get(Std_a.ID_INGRESO_UPC)
                # Diccionario para INGRESO_OFERTA
                INGRESO_OFERTA = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_a.ID_INGRESO_OFERTA= INGRESO_OFERTA.get(Std_a.ID_INGRESO_OFERTA)
                # Diccionario para MOTIVACION
                MOTIVACION = {
                    1: 'Bajo',
                    2: 'Medio',
                    3: 'Alto',
                    4: 'Excelente'
                }
                Std_a.ID_MOTIVACION= MOTIVACION.get(Std_a.ID_MOTIVACION)
                # Diccionario para VALIDO_BACH
                VALIDO_BACH = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_a.ID_VALIDO_BACH= VALIDO_BACH.get(Std_a.ID_VALIDO_BACH)
                # Diccionario para TIPO_COLEGIO
                TIPO_COLEGIO = {
                    1: 'Privado',
                    2: 'Público'
                }
                Std_a.ID_TIPO_COLEGIO= TIPO_COLEGIO.get(Std_a.ID_TIPO_COLEGIO)
                # Diccionario para SEMESTRE_INICIO
                SEMESTRE_INICIO = {
                    1: '2012-1',
                    2: '2013-1',
                    3: '2013-2',
                    4: '2014-1',
                    5: '2014-2',
                    6: '2015-1',
                    7: '2015-2',
                    8: '2016-1',
                    9: '2016-2',
                    10: '2017-1',
                    11: '2017-2',
                    12: '2018-1',
                    13: '2018-2',
                    14: '2019-1',
                    15: '2019-2',
                    16: '2020-1',
                    17: '2020-2',
                    18: '2021-1',
                    19: '2021-2',
                    20: '2022-1',
                    21: '2022-2',
                    22: '2023-1',
                    23: '2012-2',
                    24: '2010-1',
                    25: '2010-2',
                    26: '2011-1',
                    27: '2011-2'
                }
                Std_a.ID_SEMESTRE_INICIO= SEMESTRE_INICIO.get(Std_a.ID_SEMESTRE_INICIO)
                # Diccionario para REPITIO_ICFES
                REPITIO_ICFES = {
                    1: 'Sí',
                    2: 'No'
                }
                Std_a.ID_REPITIO_ICFES= REPITIO_ICFES.get(Std_a.ID_REPITIO_ICFES)
                # Diccionario para ASIGNATURA_ENCUESTA
                ASIGNATURA_ENCUESTA = {
                    0: 'nRegistra',
                    1: 'Algebra lineal, código MT301B',
                    2: 'Algoritmos y fundamentos de programación, Código SS407',
                    3: 'Analisis de señales, código EL431',
                    4: 'Calculo integral, código MT303B',
                    5: 'Circuitos en corriente directa, código EL300',
                    6: 'Circuitos I, código EL401',
                    7: 'Circuitos II, código EL408',
                    8: 'Circuitos III, código EL411',
                    9: 'Comunicaciones I, código EL420',
                    10: 'Comunicaciones II, código EL425',
                    11: 'Control I, código EL417',
                    12: 'Control II, código EL422',
                    13: 'Digitales I, código EL409',
                    14: 'Electiva I Procesamiento de señales',
                    15: 'Electiva II Procesamiento de señales',
                    16: 'Electiva III Procesamiento de señales',
                    17: 'Electrónica de potencia, código EL419',
                    18: 'Electrónica I, código EL402',
                    19: 'Electrónica II, código EL412',
                    20: 'Gestion empresarial y emprendimiento, código MB322',
                    21: 'Herramientas de software, código EL436',
                    22: 'Instrumentacion, código EL424',
                    23: 'Introducción a la ingenieria electrónica, código EL435',
                    24: 'Lógica digital, código EL502',
                    25: 'Medios de transmisión, código EL445',
                    26: 'Modelamiento y simulación, código EL432',
                    27: 'Ondas electrómagneticas, código FS315E',
                    28: 'Profundización, código EL444',
                    29: 'Psicometría, código PS505',
                    30: 'Semillero de investigación, código EL437',
                    31: 'Semillero de procesamiento de señales TRIAC',
                    32: 'Seminario de investigación, código EL439',
                    33: 'Tratamiento de señales, código EL433',
                    34: 'CATEDRA UPECISTA COD: UPC01',
                    35: 'HUMANIDADES I COD: HM301',
                    36: 'CALCULO DIFERENCIAL COD: MT302B',
                    37: 'TECNICAS DE AUTOAPRENDIZAJE COD: PG312',
                    38: 'HUMANIDADES II COD: HM302',
                    39: 'LENGUA EXTRANJERA-GRAMATICA COD: UPC04',
                    40: 'MECANICA COD: FS314',
                    41: 'PROGRAMACION DE COMPUTADORES I COD: SS401',
                    42: 'CALCULO MULTIVARIABLE COD: MT304B',
                    43: 'ELECTROMAGNETISMO COD: FS311',
                    44: 'ESTADISTICA DESCRIPTIVA E INFERENCIAL COD: MT307B',
                    45: 'LENGUA EXTRANJERA-LECTURA COD: UPC05',
                    46: 'METODOLOGIA DE LA INVESTIGACION COD: EL438',
                    47: 'ANALISIS NUMERICO COD: MT309B',
                    48: 'ECUACIONES DIFERENCIALES ORDINARIAS COD: MT305B',
                    49: 'LENGUA EXTRANJERA-ESCRITURA COD: UPC06',
                    50: 'ACTIVIDAD DEPORTIVA COD: UPC08',
                    51: 'FISICA MODERNA Y OPTICA COD: FS328',
                    52: 'FUNCIONES ESPECIALES Y ECUACIONES DIFERENCIALES COD: MT306B',
                    53: 'SEMINARIO DE INVESTIGACION COD: EL439',
                    54: 'ACTIVIDAD CULTURAL COD: UPC09',
                    55: 'DIGITALES II COD: EL410',
                    56: 'ELECTRONICA III COD: EL416',
                    57: 'INGENIERIA ECONOMICA COD: AI420',
                    58: 'LENGUA EXTRANJERA CONVERSACION COD: UPC07',
                    59: 'MAQUINAS ELECTRICAS COD: EL440',
                    60: 'DIGITALES III COD: EL403',
                    61: 'GERENCIA COD: AE118',
                    62: 'LABORATORIO DE DISEÑO INTEGRAL COD: EL441',
                    63: 'FORMULACION Y EVALU DE PROYEC EN INGENIERIA COD: FC407',
                    64: 'OPTATIVA VIRTUAL COD: EL801',
                    65: 'TELEMATICA I COD: EL443',
                    66: 'DISEÑO EXPERIMENTAL COD: FC403',
                    67: 'PROYECTO I COD: EL447',
                    68: 'TELEMATICA II COD: EL446',
                    69: 'COMPETENCIAS PEDAGOGICAS COD: PG013',
                    70: 'LEGISLACION COD: DR556',
                    71: 'PROYECTO II COD: EL448'
                }

                Std_a.ID_ASIGNATURA_ENCUESTA= ASIGNATURA_ENCUESTA.get(Std_a.ID_ASIGNATURA_ENCUESTA)
                # Diccionario para JORNADA_ACAD
                JORNADA_ACAD = {
                    1: 'Diurno',
                    2: 'Nocturno'
                }
                Std_a.ID_JORNADA_ACAD= JORNADA_ACAD.get(Std_a.ID_JORNADA_ACAD)
                # Diccionario para RENDIMIENTO_ACTUAL
                RENDIMIENTO_ACTUAL = {
                    1: 'Bajo',
                    2: 'Medio',
                    3: 'Alto',
                    4: 'Excelente'
                }
                Std_a.ID_RENDIMIENTO_ACTUAL= RENDIMIENTO_ACTUAL.get(Std_a.ID_RENDIMIENTO_ACTUAL)
                # Diccionario para NIVEL_SATISFACION_ASIG
                NIVEL_SATISFACION_ASIG = {
                    1: 'Bajo',
                    2: 'Medio',
                    3: 'Alto',
                    4: 'Excelente'
                }
                Std_a.ID_NIVEL_SATISFACION_ASIG= NIVEL_SATISFACION_ASIG.get(Std_a.ID_NIVEL_SATISFACION_ASIG)

                data = {  
                    'Std_C' : Std_c,
                    'Std_A' : Std_a,
                    'Std_S' : Std_s
                            
                    }
                print(data)
                return render(request, "consulta.html", data)
        except Estudiante.DoesNotExist:
                data = {
                    'error': "Usuario no encontrado"
                }
                return JsonResponse(data)

        
    
def eliminar_std(request,id):
    std = Estudiante.objects.get(ID_DOCUMENTO=id)
    std.delete()

    return redirect('/api/consultas_p')

def edicion_std(request, id):
    Std_c = Estudiante.objects.get(ID_DOCUMENTO=id)
    Std_s = SocioEconomica.objects.get(ID_ESTUDIANTE=id)
    Std_a = InfoAcademica.objects.get(ID_ESTUDIANTE=id)
    data = {  
            'Std_C' : Std_c,
            'Std_A' : Std_a,
            'Std_S' : Std_s                    
        }
    return render(request, "edicion.html", data)

def change_std(request):
    ID_c_DOCUMENTO = request.POST['ID_DOCUMENTO']
    ID_TIPO_DOCUMENTO = request.POST['ID_TIPO_DOCUMENTO']
    ID_NOMBRE = request.POST['ID_NOMBRE']
    ID_EDAD = request.POST['ID_EDAD_ss']
    ID_NUM_CONTACTO = request.POST['ID_NUM_CONTACTO']
    ID_GENERO = request.POST['ID_GENERO']
    ID_VIC_CONFLICTO = request.POST['ID_VIC_CONFLICTO']
    ID_ESTADO_CIVIL = request.POST['ID_ESTADO_CIVIL']
    ID_DPTO_NAC = request.POST['ID_DPTO_NAC']
    ID_MUN_NAC = request.POST['ID_MUN_NAC']
    ID_TIPO_DISC = request.POST['ID_TIPO_DISC']
    ID_ETNIA = request.POST['ID_ETNIA']
    ID_EMAIL = request.POST['ID_EMAIL']
    ID_MAD_CAB_HOGAR = request.POST['ID_MAD_CAB_HOGAR']
    ID_EDAD_MAYOR = request.POST['ID_EDAD_MAYOR']
    ID_EDAD_MENOR = request.POST['ID_EDAD_MENOR']
    ID_CANT_HIJOS = request.POST['ID_CANT_HIJOS']
    ID_OCUP_MADRE = request.POST['ID_OCUP_MADRE']
    ID_OCUP_PADRE = request.POST['ID_OCUP_PADRE']
    ID_CANT_HERMANOS = request.POST['ID_CANT_HERMANOS']
    ID_POS_HERMANO = request.POST['ID_POS_HERMANO']
    ID_INTEGRANTES = request.POST['ID_INTEGRANTES']
    ID_TALENTO = request.POST['ID_TALENTO']
    ID_EPS = request.POST['ID_EPS']
    ID_SISBEN = request.POST['ID_SISBEN']
    ID_LENTES = request.POST['ID_LENTES']
    #Tabla socio economica
    ID_OCUPACION = request.POST['ID_OCUPACION']
    ID_ESTRATO = request.POST['ID_ESTRATO']
    ID_TIPO_VIVIENDA = request.POST['ID_TIPO_VIVIENDA']
    ID_RECIBE_INGRESOS = request.POST['ID_RECIBE_INGRESOS']
    ID_ACUDIENTE = request.POST['ID_ACUDIENTE']
    ID_NIVEL_ACADEMICO = request.POST['ID_NIVEL_ACADEMICO']
    ID_INGRESO_FAMILIAR = request.POST['ID_INGRESO_FAMILIAR']
    ID_TIENE_PC = request.POST['ID_TIENE_PC']
    ID_TIENE_INTERNET = request.POST['ID_TIENE_INTERNET']
    ID_CEL_SMART = request.POST['ID_CEL_SMART']
    ID_PLAN_DATOS = request.POST['ID_PLAN_DATOS']
    ID_INGRESO_TRABAJA = request.POST['ID_INGRESO_TRABAJA']
    #Tabla Academica
    ID_PROGR_ACTUAL = request.POST['ID_PROGR_ACTUAL']
    ID_HERMANOS_IES = request.POST['ID_HERMANOS_IES']
    ID_INGRESO_UPC = request.POST['ID_INGRESO_UPC']
    ID_INGRESO_OFERTA = request.POST['ID_INGRESO_OFERTA']
    ID_MOTIVACION = request.POST['ID_MOTIVACION']
    ID_VALIDO_BACH = request.POST['ID_VALIDO_BACH']
    ID_TIPO_COLEGIO = request.POST['ID_TIPO_COLEGIO']
    ID_SEMESTRE_INICIO = request.POST['ID_SEMESTRE_INICIO']
    ID_REPITIO_ICFES = request.POST['ID_REPITIO_ICFES']
    ID_PUNTAJE_ICFES = request.POST['ID_PUNTAJE_ICFES']
    ID_PUESTO_ICFES = request.POST['ID_PUESTO_ICFES']
    ID_LECTURA_CRITICA = request.POST['ID_LECTURA_CRITICA']
    ID_MATEMATICA = request.POST['ID_MATEMATICA']
    ID_CIUDADANOS = request.POST['ID_CIUDADANOS']
    ID_CIENCIAS = request.POST['ID_CIENCIAS']
    ID_INGLES = request.POST['ID_INGLES']
    ID_SEMESTRES_CURSADOS = request.POST['ID_SEMESTRES_CURSADOS']
    ID_UBICACION_SEMESTRE = request.POST['ID_UBICACION_SEMESTRE']
    ID_CREDITOS_APROBADOS = request.POST['ID_CREDITOS_APROBADOS']
    ID_PROMEDIO_ACUMULADO = request.POST['ID_PROMEDIO_ACUMULADO']
    ID_PROMEDIO_SEMESTRE_ANT = request.POST['ID_PROMEDIO_SEMESTRE_ANT']
    ID_CREDITOS_NO_APROBADOS = request.POST['ID_CREDITOS_NO_APROBADOS']
    ID_CREDITOS_MATRIC = request.POST['ID_CREDITOS_MATRIC']
    ID_MATERIAS_CANCELADAS = request.POST['ID_MATERIAS_CANCELADAS']
    ID_ASIGNATURA_ENCUESTA = request.POST['ID_ASIGNATURA_ENCUESTA']
    ID_JORNADA_ACAD = request.POST['ID_JORNADA_ACAD']
    ID_NOTA_ACTUAL = request.POST['ID_NOTA_ACTUAL']
    ID_RENDIMIENTO_ACTUAL = request.POST['ID_RENDIMIENTO_ACTUAL']
    ID_NIVEL_SATISFACION_ASIG = request.POST['ID_NIVEL_SATISFACION_ASIG']
    
    
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
 
    return redirect('/api/consultas_p/')

def dashboard(request):
    Total=Estudiante.objects.count()
    context = {'total_estudiantes': Total}
    print(context)
    return render(request, "fp.html",context)

         
def get_chart(_request):  
    chart = {
       'title': {
            'text': 'Cantidad de estudiantes \n segun su genero',
            'left': 'center'
         },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}: {c} ({d}%)'
        },
        'legend': {
            'right': '0%',
            'top': '30%',
            'orient': 'vertical'
        },
        'series': [
        {
            'type': 'pie',
            'radius': ['40%', '70%'],
            'avoidLabelOverlap': 'false',
            'left': '-30%',
            'top': '40',
            'label': {
                'show': 'false',
                'formatter': '({d}%)'
            },
        'emphasis': {
                'label': {
                'show': 'false',
                'fontSize': 10,
                'fontWeight': 'bold',
                
                }
            },
            'labelLine': {
                'show': 'false'
            },
            'data': [
                { 'itemStyle': {'color': "rgb(101, 197, 189)"},'value': len(Estudiante.objects.filter(ID_GENERO=2)),'name': 'Mujeres' },
                { 'itemStyle': {'color': "rgb(147,112,219)"},'value': len(Estudiante.objects.filter(ID_GENERO=1)), 'name': 'Hombres' },
                { 'itemStyle': {'color': "rgba(255, 251, 13, 1)"},'value': len(Estudiante.objects.filter(ID_GENERO=0)),'name': 'Otro Genero' }
                
            ]
            }
        ]
    }
    
    return JsonResponse(chart)

def get_chart_2(_request): 
    sixy = Estudiante.objects.filter(ID_GENERO=2)
    A = InfoAcademica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy])
    A = A.filter(ID_SEMESTRE_INICIO__lte=12)      
    sixy_m = Estudiante.objects.filter(ID_GENERO=1)
    B = InfoAcademica.objects.filter(ID_ESTUDIANTE__in=[estudiante.ID_DOCUMENTO for estudiante in sixy_m])
    B = B.filter(ID_SEMESTRE_INICIO__lte=12) 
    chart_2 = {
        'title': {
            'text': 'Estudiantes con mas de 6 años',
            'right': '25%',
            'top' : '5%'
         },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}: {c}'
        },
        'legend': {
            'data': ['Mujeres', 'Hombres']
        },
       'xAxis': {
            'type': 'category',
            'data': ['Mujeres', 'Hombres']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
            'data': [{'itemStyle': {'color': "rgb(101, 197, 189)"},'value':len(A)},
                     {'itemStyle': {'color': "rgb(147,112,219)"},'value':len(B)},],
            'type': 'bar',
            'top' : '0%',
            'showBackground': 'true',
            'backgroundStyle': {
                'color': 'rgba(180, 180, 180, 0.2)'
            }
            }
  ]
}
    return JsonResponse(chart_2)

def get_chart_3(_request): 
    sixy = Estudiante.objects.filter(ID_GENERO=2,ID_CANT_HIJOS__gt=0)  
    sixy_m = Estudiante.objects.filter(ID_GENERO=1,ID_CANT_HIJOS__gt=0)
    chart_3 = {
       'title': {
            'text': 'Estudiantes con hijos',
            'left': 'center',
            'top': '0%'
         },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}: {c} ({d}%)'
        },
        'legend': {
            'right': '0%',
            'top': '30%',
            'orient': 'vertical'
        },
        'series': [
        {
            'type': 'pie',
            'radius': ['40%', '70%'],
            'avoidLabelOverlap': 'false',
            'left': '-30%',
            'top': '25',
            'label': {
                'show': 'false',
                'formatter': '({d}%)'
            },
        'emphasis': {
                'label': {
                'show': 'false',
                'fontSize': 10,
                'fontWeight': 'bold',
                
                }
            },
            'labelLine': {
                'show': 'false'
            },
            'data': [
                { 'itemStyle': {'color': "rgb(101, 197, 189)"},'value': len(sixy),'name': 'Mujeres' },
                { 'itemStyle': {'color': "rgb(147,112,219)"},'value': len(sixy_m), 'name': 'Hombres' },

                
            ]
            }
        ]
    }
    return JsonResponse(chart_3)

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
       'title': {
            'text': 'Estudiantes que trabajan',
            'left': 'center',
            'top': '0%'
         },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{b}: {c} ({d}%)'
        },
        'legend': {
            'right': '0%',
            'top': '30%',
            'orient': 'vertical'
        },
        'series': [
        {
            'type': 'pie',
            'radius': ['40%', '70%'],
            'avoidLabelOverlap': 'false',
            'left': '-30%',
            'top': '25',
            'label': {
                'show': 'false',
                'formatter': '({d}%)'
            },
        'emphasis': {
                'label': {
                'show': 'false',
                'fontSize': 10,
                'fontWeight': 'bold',
                
                }
            },
            'labelLine': {
                'show': 'false'
            },
            'data': [
                { 'itemStyle': {'color': "rgb(101, 197, 189)"},'value': len(A),'name': 'Mujeres' },
                { 'itemStyle': {'color': "rgb(147,112,219)"},'value': len(B), 'name': 'Hombres' },
                { 'itemStyle': {'color': "rgb(255, 251, 13, 1)"},'value': len(C), 'name': 'Otros' },

                
            ]
            }
        ]
    }
    return JsonResponse(chart_4)

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
    'color': ["rgb(147,112,219)","rgb(101, 197, 189)","rgb(255, 251, 13, 1)"],
    'title': {
    'text': 'Grado de motivaciion de los estudiantes',
    'right': '10%',
    'top' : '5%'

    },
    'legend': {
            'right': '0%',
            'top': '30%',
            'orient': 'vertical'
    },

    'tooltip': {
      'trigger': 'axis',
      'axisPointer': {
        'type': 'shadow'
      }
    },
    
    'yAxis': {
      'splitLine': '{' 'show'':' 'false' '}',
      'axisLabel': '{' 'show'':' 'false' '}',
      'axisTick': '{' 'show'':' 'false' '}',
      'axisLine': '{' 'show'':' 'false' '}'
      

      },
      'xAxis': {
      'data': ['Bajo', 'Medio', 'Alto', 'Exc'],
    }, 
      'series': [
          {
            'name': 'Hombres',
            'type': 'bar',
            'barWidth': '20%',
            'bargap': '30%', 
            'label':{
                'show': 'true',
                'position': 'top',
                'fontSize': '16'
                },
            'data': [
                {   
                    'value': len(A1),  
                },
                {
                    'value': len(B1), 
                } ,
                    {
                    'value': len(C1),
                },
                    {
                    'value': len(D1), 
                }             
                ]
          },
          {
            'name': 'Mujeres',
            'type': 'bar',
            'barWidth': '20%',
            'bargap': '30%', 
            'label':{
                'show': 'true',
                'position': 'top',
                'fontSize': '16'
                },
            'data': [
                {
                    'value': len(A2), 
                },
                {
                    'value': len(B2),
                } ,
                    {
                    'value': len(C2),
                },
                    {   
                    'value': len(D2),
                }             
                ]
          },
          
          {
            'name': 'Otros',
            'type': 'bar',
            'barWidth': '20%',
            'bargap': '30%', 
            'label':{
                'show': 'true',
                'position': 'top',
                'fontSize': '16'
                },
            'data': [
                {},
                {},
                {
                    'value': len(C3), 
                },
                {}             
                ]
          }    
      ]           
    }
    
    
    return JsonResponse(chart_5)