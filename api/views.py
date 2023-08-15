from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Estudiante , SocioEconomica, InfoAcademica
from django.views.generic import ListView
from random import randrange
# Create your views here.


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

        
    
#def eliminar_curso(request,id):
 #   curso = Curso.objects.get(id=id)
  #  curso.delete()

   # return redirect('/api/home')

#def edicion_curso(request, id):
 #   curso = Curso.objects.get(id=id)
  #  data = {
  #      'curso': curso
   # }
    #return render(request, "edicion.html", data)

#def change_curso(request):
 #  id= int(request.POST['id'])
  # nombre = request.POST['txtNombre']
  #creditos = request.POST['numCreditos']
   #curso = Curso.objects.get(id=id)
   #curso.nombre = nombre
   #curso.creditos = creditos
   #curso.save()
 
   #return redirect('/api/home')

def get_chart(_request):
   # cursos_listados = Curso.objects.all()
    nombres = []
    creditos = []

# Itera a través de las instancias y agrega los valores a los arrays
    
    #for item in cursos_listados:
    #   nombres.append(item.nombre)
     #   creditos.append(item.creditos)
        
    colors = ['blue', 'orange', 'red', 'black', 'yellow', 'green', 'magenta', 'lightblue', 'purple', 'brown']
    random_color = colors[randrange(0, (len(colors)-1))]

    chart = {
        'backgroundColor': '#000000',
        'tooltip' : {
        'trigger': 'axis',
        'axisPointer': {
          'type': 'cross'
            },
        },
        'xAxis': {
            'type': 'category',
            'data': nombres,
            'axisLabel': {
                'interval': 0  
            },
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
            'data': creditos,
            'type': 'bar',
            'itemStyle': {
                    'color': random_color
            },
            'showBackground': 'true',
            'backgroundStyle': {
                'color': 'rgba(180, 180, 180, 0.2)'
            }
            }
        ]    
    }

    return JsonResponse(chart)