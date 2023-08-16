-- Crear tabla ESTUDIANTES
CREATE TABLE ESTUDIANTES (
    ID_DOCUMENTO int NOT NULL,
    ID_TIPO_DOCUMENTO char(1) NOT NULL,
    ID_NOMBRE char(35) NOT NULL,
    ID_EDAD INT NOT NULL,
    ID_NUM_CONTACTO CHAR(10) NOT NULL,
    ID_GENERO int NULL,
    ID_VIC_CONFLICTO int NOT NULL,
    ID_ESTADO_CIVIL INT NOT NULL,
    ID_DPTO_NAC CHAR(30) NOT NULL,
    ID_MUN_NAC CHAR(30) NOT NULL,
    ID_TIPO_DISC INT NOT NULL,
    ID_ETNIA INT NOT NULL,
    ID_EMAIL CHAR(50) NOT NULL,
    ID_MAD_CAB_HOGAR INT NOT NULL,
    ID_EDAD_MAYOR INT NOT NULL,
    ID_EDAD_MENOR INT NOT NULL,
    ID_CANT_HIJOS INT NOT NULL,
    ID_OCUP_MADRE INT NOT NULL,
    ID_OCUP_PADRE INT NOT NULL,
    ID_CANT_HERMANOS INT NOT NULL,
    ID_POS_HERMANO INT NOT NULL,
    ID_INTEGRANTES INT NOT NULL,
    ID_TALENTO INT NOT NULL,
    ID_EPS INT NOT NULL,
    ID_SISBEN CHAR(3) NOT NULL,
    ID_LENTES INT NOT NULL,
    CONSTRAINT PK_ESTUDIANTES PRIMARY KEY (ID_DOCUMENTO)
);

-- Crear tabla SOCIO_ECONOMICA
CREATE TABLE SOCIO_ECONOMICA (
    ID_ESTUDIANTE int NOT NULL,
    ID_OCUPACION int NOT NULL,
    ID_ESTRATO INT NOT NULL,
    ID_TIPO_VIVIENDA int NULL,
    ID_RECIBE_INGRESOS INT NOT NULL,
    ID_ACUDIENTE INT NOT NULL,
    ID_NIVEL_ACADEMICO INT NOT NULL,
    ID_INGRESO_FAMILIAR NUMERIC NOT NULL,
    ID_TIENE_PC INT NOT NULL,
    ID_TIENE_INTERNET INT NOT NULL,
    ID_CEL_SMART INT NOT NULL,
    ID_PLAN_DATOS INT NOT NULL,
    ID_INGRESO_TRABAJA INT NOT NULL,
    CONSTRAINT PK_SOCIO_ECONOMICA PRIMARY KEY (ID_ESTUDIANTE),
    CONSTRAINT FK_SOCIO_ESTUDIANTE
    FOREIGN KEY (ID_ESTUDIANTE)
    REFERENCES ESTUDIANTES (ID_DOCUMENTO)
);

-- Crear tabla INFO_ACADEMICA
CREATE TABLE INFO_ACADEMICA (
    ID_ESTUDIANTE int NOT NULL,
    ID_PROGR_ACTUAL int NOT NULL,
    ID_HERMANOS_IES int NOT NULL,
    ID_INGRESO_UPC int NOT NULL,
    ID_INGRESO_OFERTA INT NOT NULL,
    ID_MOTIVACION INT NOT NULL,
    ID_VALIDO_BACH INT NOT NULL,
    ID_TIPO_COLEGIO INT NOT NULL,
    ID_SEMESTRE_INICIO CHAR(6) NOT NULL,
    ID_REPITIO_ICFES INT NOT NULL,
    ID_PUNTAJE_ICFES INT NOT NULL,
    ID_PUESTO_ICFES INT NOT NULL,
    ID_LECTURA_CRITICA INT NOT NULL,
    ID_MATEMATICA INT NOT NULL,
    ID_CIUDADANOS INT NOT NULL,
    ID_CIENCIAS INT NOT NULL,
    ID_INGLES INT NOT NULL,
    ID_SEMESTRES_CURSADOS INT NOT NULL,
    ID_UBICACION_SEMESTRE INT NOT NULL,
    ID_CREDITOS_APROBADOS INT NOT NULL,
    ID_PROMEDIO_ACUMULADO INT NOT NULL,
    ID_PROMEDIO_SEMESTRE_ANT INT NOT NULL,
    ID_CREDITOS_NO_APROBADOS INT NOT NULL,
    ID_CREDITOS_MATRIC INT NOT NULL,
    ID_MATERIAS_CANCELADAS INT NOT NULL,
    ID_ASIGNATURA_ENCUESTA CHAR(6) NOT NULL,
    ID_JORNADA_ACAD INT NOT NULL,
    ID_NOTA_ACTUAL INT NOT NULL,
    ID_RENDIMIENTO_ACTUAL INT NOT NULL,
    ID_NIVEL_SATISFACION_ASIG INT NOT NULL,
    CONSTRAINT PK_INFO_ACADEMICA PRIMARY KEY (ID_ESTUDIANTE),
    CONSTRAINT FK_ACADEMICA_ESTUDIANTE
    FOREIGN KEY (ID_ESTUDIANTE)
    REFERENCES ESTUDIANTES (ID_DOCUMENTO)
);