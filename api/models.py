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
    ID_TIPO_DOCUMENTO = models.CharField(max_length=1)
    ID_NOMBRE = models.CharField(max_length=35)
    ID_EDAD= models.IntegerField()
    ID_NUM_CONTACTO = models.CharField(max_length=10)
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
    ID_SISBEN = models.CharField(max_length=3)
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
    ID_INGRESO_FAMILIAR = models.DecimalField(max_digits=10, decimal_places=2)
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
    ID_SEMESTRE_INICIO = models.CharField(max_length=6)
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
    ID_PROMEDIO_ACUMULADO = models.IntegerField()
    ID_PROMEDIO_SEMESTRE_ANT = models.IntegerField()
    ID_CREDITOS_NO_APROBADOS = models.IntegerField()
    ID_CREDITOS_MATRIC = models.IntegerField()
    ID_MATERIAS_CANCELADAS = models.IntegerField()
    ID_ASIGNATURA_ENCUESTA = models.CharField(max_length=6)
    ID_JORNADA_ACAD = models.IntegerField()
    ID_NOTA_ACTUAL = models.IntegerField()
    ID_RENDIMIENTO_ACTUAL = models.IntegerField()
    ID_NIVEL_SATISFACION_ASIG = models.IntegerField()
    def __str__(self):
       texto = "{0}"
       return texto.format(self.ID_ESTUDIANTE)
   