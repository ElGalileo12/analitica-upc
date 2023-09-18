import pandas as pd
from sqlalchemy import create_engine

# Cargar datos desde Excel
archivo_excel = 'E:/Universidad/Analitica/analitica-upc/datos.xlsx'
datos_excel = pd.read_excel(archivo_excel)

# Establecer conexión a la base de datos PostgreSQL
engine = create_engine('postgresql://postgres:Kevin12@127.0.0.1/ADI')

# Insertar datos en la tabla de Estudiantescl
datos_estudiantes = datos_excel[['ID_DOCUMENTO', 'ID_TIPO_DOCUMENTO', 'ID_NOMBRE', 'ID_EDAD', 'ID_NUM_CONTACTO', 'ID_GENERO', 'ID_VIC_CONFLICTO', 'ID_ESTADO_CIVIL', 'ID_DPTO_NAC', 'ID_MUN_NAC', 'ID_TIPO_DISC', 'ID_ETNIA',
                                 'ID_EMAIL', 'ID_MAD_CAB_HOGAR', 'ID_EDAD_MAYOR', 'ID_EDAD_MENOR', 'ID_CANT_HIJOS', 'ID_OCUP_MADRE', 'ID_OCUP_PADRE', 'ID_CANT_HERMANOS', 'ID_POS_HERMANO', 'ID_INTEGRANTES', 'ID_TALENTO', 'ID_EPS', 'ID_SISBEN', 'ID_LENTES']]
datos_estudiantes_sin_nulos = datos_estudiantes.dropna()
datos_estudiantes_sin_nulos.to_sql(
    'api_estudiante', engine, if_exists='append', index=False)

# Insertar datos en la tabla de Socio-economica
datos_socio = datos_excel[['ID_DOCUMENTO', 'ID_OCUPACION', 'ID_ESTRATO', 'ID_TIPO_VIVIENDA', 'ID_RECIBE_INGRESOS', 'ID_ACUDIENTE',
                           'ID_NIVEL_ACADEMICO', 'ID_INGRESO_FAMILIAR', 'ID_TIENE_PC', 'ID_TIENE_INTERNET', 'ID_CEL_SMART', 'ID_PLAN_DATOS', 'ID_INGRESO_TRABAJA']]
datos_socio.rename(columns={'ID_DOCUMENTO': 'ID_ESTUDIANTE_id'}, inplace=True)
datos_socio_sin_nulos = datos_socio.dropna()
datos_socio_sin_nulos.to_sql(
    'api_socioeconomica', engine, if_exists='append', index=False)

# Insertar datos en la tabla de Informacion Academica
datos_infoaca = datos_excel[['ID_DOCUMENTO', 'ID_PROGR_ACTUAL', 'ID_HERMANOS_IES', 'ID_INGRESO_UPC', 'ID_INGRESO_OFERTA', 'ID_MOTIVACION', 'ID_VALIDO_BACH', 'ID_TIPO_COLEGIO', 'ID_SEMESTRE_INICIO', 'ID_REPITIO_ICFES', 'ID_PUNTAJE_ICFES', 'ID_PUESTO_ICFES', 'ID_LECTURA_CRITICA', 'ID_MATEMATICA', 'ID_CIUDADANOS', 'ID_CIENCIAS',
                             'ID_INGLES', 'ID_SEMESTRES_CURSADOS', 'ID_UBICACION_SEMESTRE', 'ID_CREDITOS_APROBADOS', 'ID_PROMEDIO_ACUMULADO', 'ID_PROMEDIO_SEMESTRE_ANT', 'ID_CREDITOS_NO_APROBADOS', 'ID_CREDITOS_MATRIC', 'ID_MATERIAS_CANCELADAS', 'ID_ASIGNATURA_ENCUESTA', 'ID_JORNADA_ACAD', 'ID_NOTA_ACTUAL', 'ID_RENDIMIENTO_ACTUAL', 'ID_NIVEL_SATISFACION_ASIG']]
datos_infoaca.rename(
    columns={'ID_DOCUMENTO': 'ID_ESTUDIANTE_id'}, inplace=True)
datos_infoaca_sin_nulos = datos_infoaca.dropna()
datos_infoaca_sin_nulos.to_sql(
    'api_infoacademica', engine, if_exists='append', index=False)
# Cerrar la conexión
engine.dispose()
