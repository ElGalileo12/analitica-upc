from django.db import models

# Create your models here.
#class Curso(models.Model):
  #  nombre = models.CharField(max_length=30)
   # creditos = models.PositiveSmallIntegerField()
    
   # def __str__(self):
    #   texto = "{0} ({1})"
     #  return texto.format(self.nombre, self.creditos)
    


class Estudiante(models.Model):
    ID_DOCUMENTO = models.IntegerField(primary_key=True)
    ID_TIPO_DOCUMENTO = models.CharField(max_length=35)
    ID_NOMBRE = models.CharField(max_length=50)
    ID_EDAD= models.IntegerField()
    ID_NUM_CONTACTO = models.CharField(max_length=20)
    ID_GENERO = models.IntegerField(null=True)
    ID_VIC_CONFLICTO = models.IntegerField()
    ID_ESTADO_CIVIL = models.IntegerField()
    ID_DPTO_NAC = models.CharField(max_length=30)
    ID_MUN_NAC = models.CharField(max_length=30)
    ID_TIPO_DISC = models.IntegerField()
    ID_ETNIA = models.IntegerField()
    ID_EMAIL = models.CharField(max_length=50)
    ID_MAD_CAB_HOGAR = models.IntegerField()
    ID_EDAD_MAYOR = models.IntegerField()
    ID_EDAD_MENOR = models.IntegerField()
    ID_CANT_HIJOS = models.IntegerField()
    ID_OCUP_MADRE = models.IntegerField()
    ID_OCUP_PADRE = models.IntegerField()
    ID_CANT_HERMANOS = models.IntegerField()
    ID_POS_HERMANO = models.IntegerField()
    ID_INTEGRANTES = models.IntegerField()
    ID_TALENTO = models.IntegerField()
    ID_EPS = models.IntegerField()
    ID_SISBEN = models.CharField(max_length=20)
    ID_LENTES = models.IntegerField()
    
    def __str__(self):
       texto = "{0} ({1})"
       return texto.format(self.ID_DOCUMENTO, self.ID_NOMBRE)

class SocioEconomica(models.Model):
    ID_ESTUDIANTE = models.OneToOneField(Estudiante, on_delete=models.CASCADE, primary_key=True)
    ID_OCUPACION = models.IntegerField()
    ID_ESTRATO = models.IntegerField()
    ID_TIPO_VIVIENDA = models.IntegerField(null=True)
    ID_RECIBE_INGRESOS = models.IntegerField()
    ID_ACUDIENTE = models.IntegerField()
    ID_NIVEL_ACADEMICO = models.IntegerField()
    ID_INGRESO_FAMILIAR = models.IntegerField()
    ID_TIENE_PC = models.IntegerField()
    ID_TIENE_INTERNET = models.IntegerField()
    ID_CEL_SMART = models.IntegerField()
    ID_PLAN_DATOS = models.IntegerField()
    ID_INGRESO_TRABAJA = models.IntegerField()
    def __str__(self):
       texto = "{0}"
       return texto.format(self.ID_ESTUDIANTE)

class InfoAcademica(models.Model):
    ID_ESTUDIANTE = models.OneToOneField(Estudiante, on_delete=models.CASCADE, primary_key=True)
    ID_PROGR_ACTUAL = models.IntegerField()
    ID_HERMANOS_IES = models.IntegerField()
    ID_INGRESO_UPC = models.IntegerField()
    ID_INGRESO_OFERTA = models.IntegerField()
    ID_MOTIVACION = models.IntegerField()
    ID_VALIDO_BACH = models.IntegerField()
    ID_TIPO_COLEGIO = models.IntegerField()
    ID_SEMESTRE_INICIO = models.IntegerField()
    ID_REPITIO_ICFES = models.IntegerField()
    ID_PUNTAJE_ICFES = models.IntegerField()
    ID_PUESTO_ICFES = models.IntegerField()
    ID_LECTURA_CRITICA = models.IntegerField()
    ID_MATEMATICA = models.IntegerField()
    ID_CIUDADANOS = models.IntegerField()
    ID_CIENCIAS = models.IntegerField()
    ID_INGLES = models.IntegerField()
    ID_SEMESTRES_CURSADOS = models.IntegerField()
    ID_UBICACION_SEMESTRE = models.IntegerField()
    ID_CREDITOS_APROBADOS = models.IntegerField()
    ID_PROMEDIO_ACUMULADO = models.FloatField()
    ID_PROMEDIO_SEMESTRE_ANT = models.FloatField()
    ID_CREDITOS_NO_APROBADOS = models.IntegerField()
    ID_CREDITOS_MATRIC = models.IntegerField()
    ID_MATERIAS_CANCELADAS = models.IntegerField()
    ID_ASIGNATURA_ENCUESTA = models.IntegerField()
    ID_JORNADA_ACAD = models.IntegerField()
    ID_NOTA_ACTUAL = models.FloatField()
    ID_RENDIMIENTO_ACTUAL = models.IntegerField()
    ID_NIVEL_SATISFACION_ASIG = models.IntegerField()
    def __str__(self):
       texto = "{0}"
       return texto.format(self.ID_ESTUDIANTE)
   
   #MODELO DE EGRESADOS
class Egresados(models.Model):
    ID_DOCUMENTO = models.IntegerField(primary_key=True)
    ID_TIPO_DOCUMENTO = models.CharField(max_length=35)
    ID_NOMBRE = models.CharField(max_length=50)
    ID_NUM_CONTACTO = models.CharField(max_length=20)
    ID_GENERO = models.IntegerField(null=True)
    ID_EDAD= models.IntegerField()
    ID_ESTADO_CIVIL = models.IntegerField()
    ID_ETNIA = models.IntegerField()
    ID_EMAIL = models.CharField(max_length=40)
    ID_ESTRATO = models.IntegerField()
    
    def __str__(self):
       texto = "{0} ({1})"
       return texto.format(self.ID_DOCUMENTO, self.ID_NOMBRE)



class EgreAcademica(models.Model):
    ID_EGRESADO = models.OneToOneField(Egresados, on_delete=models.CASCADE, primary_key=True, related_name='info_academica')
    ID_TITULO = models.IntegerField()
    ID_SEMESTRE_INICIO = models.IntegerField()
    ID_SEMESTRES_CURSADOS = models.IntegerField()
    ID_PROMEDIO_ACUMULADO = models.FloatField()
    ID_SEMESTRE_FIN = models.IntegerField()
    ID_FECHA_GRADO = models.IntegerField()
    ID_PRACTICAS = models.IntegerField()
    ID_POSTGRADO = models.IntegerField()
    ID_POSTGRADO_NIVEL = models.IntegerField()
    ID_POSTGRADO_LUGAR = models.IntegerField()


class EgreLaboral(models.Model):
    ID_EGRESADO = models.OneToOneField(Egresados, on_delete=models.CASCADE, primary_key=True, related_name='info_laboral')
    ID_TRABAJA = models.IntegerField()
    ID_TRABAJA_PAIS = models.CharField(max_length=35)
    ID_TRABAJA_CIUDAD = models.CharField(max_length=30)
    ID_TRABAJA_SITUACION = models.IntegerField()
    ID_TRABAJA_PERFIL = models.IntegerField()
    ID_TRABAJA_SECTOR = models.IntegerField()
    ID_TRABAJA_TIEMPO = models.IntegerField()
    ID_TRABAJA_NIVEL = models.IntegerField()
    ID_TRABAJA_TIEMPO_PRIMER = models.IntegerField()
    ID_TRABAJA_MEDIO = models.IntegerField()
    ID_TRABAJA_SECTOR_DOS = models.IntegerField()
    ID_TRABAJA_SECTOR_TRES = models.IntegerField()
    ID_TRABAJA_REQUISITOS = models.IntegerField()
    ID_TRABAJA_RANGO = models.IntegerField()
    ID_TRABAJA_RECONOCIMIENTO = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    ID_EMPRESA_ANTES = models.IntegerField()
    ID_EMPRESA_SECTOR = models.CharField(max_length=35)
    def __str__(self):
       texto = "{0}"
       return texto.format(self.ID_EGRESADO)
   
class EgreMotivacion(models.Model):
    ID_EGRESADO = models.OneToOneField(Egresados, on_delete=models.CASCADE, primary_key=True, related_name='info_motivacion')
    ID_MOT_PREGRADO = models.IntegerField()
    ID_MOT_VOLUMEN = models.IntegerField()
    ID_MOT_NIVELS = models.IntegerField()
    ID_MOT_AMBIENTE = models.IntegerField()
    ID_MOT_FORTALECER = models.IntegerField()
    ID_MOT_MATERIAS = models.CharField(max_length=60)
    ID_MOT_APOYO = models.IntegerField()
    ID_MOT_RECURSOS = models.IntegerField()
    ID_MOT_MODALIDAD = models.IntegerField()
    ID_MOT_MODALIDAD_P = models.IntegerField()
    ID_MOT_MODALIDAD_T = models.IntegerField()
    ID_MOT_PROFUNDIZACION = models.IntegerField()
    ID_MOT_INGRESAR = models.IntegerField()
    ID_MOT_CONOCIMIENTOS = models.IntegerField()
    ID_MOT_CONTRIBUCION = models.IntegerField()
    ID_MOT_CALIDAD = models.IntegerField()
    ID_MOT_FAVORECIDO = models.IntegerField()
    ID_MOT_POST_CONT = models.IntegerField()
    def __str__(self):
       texto = "{0}"
       return texto.format(self.ID_EGRESADO)
