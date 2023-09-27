function dataPersonal(dataPers) {
  const tipoDocMapping = {
    Cédula: "cedulaCiudadania",
    "Tarjeta de identidad": "tarjetaIdentidad",
  };

  const generoMapping = {
    Otro: 0,
    Masculino: 1,
    Femenino: 2,
  };

  const victimaConMapping = {
    Sí: 1,
    No: 2,
  };

  const estadoCivilMapping = {
    Casado: 1,
    Separado: 2,
    Soltero: 3,
    "Unión libre": 4,
    Viudo: 5,
  };

  const tipoDiscapacidadMapping = {
    "Movilidad reducida": 1,
    Ninguna: 2,
    Auditiva: 3,
    Visual: 4,
  };

  const etniaMapping = {
    Indigena: 1,
    Palenquero: 2,
    "Sin distinción racial": 3,
    "Negro, mulato, afrodescendiente, afrocolombiano": 4,
    Raizal: 5,
  };

  const madCabHogarMapping = {
    "No Registra": 0,
    Sí: 1,
    No: 2,
  };

  const ocupMadreMapping = {
    Ninguna: 0,
    "Ama de casa": 1,
    Estudiante: 2,
    Fallecida: 3,
    Independiente: 4,
    Labora: 5,
    "Madre cabeza de hogar": 6,
    Pensionada: 7,
  };

  const ocupPadreMapping = {
    Ninguna: 0,
    "Padre cabeza de hogar": 1,
    Pensionado: 2,
    Fallecido: 3,
    Independiente: 4,
    Labora: 5,
  };

  const talentoMapping = {
    Ninguna: 0,
    Actor: 1,
    Atletismo: 2,
    Bailarín: 3,
    Baloncesto: 4,
    Fútbol: 5,
    "Fútbol sala": 6,
    Músico: 7,
    Natación: 8,
    Softbol: 9,
    Taekwondo: 10,
    "Tenis de mesa": 11,
    Voleibol: 12,
  };

  const EPSMapping = {
    Ninguna: 0,
    Sí: 1,
    No: 2,
  };

  const LentesMapping = {
    "No Registra": 0,
    Sí: 1,
    No: 2,
  };

  const resultado = {
    ID_DOCUMENTO: dataPers.Documento,
    ID_TIPO_DOCUMENTO: tipoDocMapping[dataPers["Tipo de documento"]],
    ID_NOMBRE: dataPers["Nombre"],
    ID_EDAD: dataPers["Edad"],
    ID_NUM_CONTACTO: dataPers["Telefono"],
    ID_GENERO: generoMapping[dataPers["Genero"]],
    ID_VIC_CONFLICTO: victimaConMapping[dataPers["¿Es victima del conflicto?"]],
    ID_ESTADO_CIVIL: estadoCivilMapping[dataPers["Estado Cívil"]],
    ID_DPTO_NAC: dataPers["Departamento"],
    ID_MUN_NAC: dataPers["Municipio"],
    ID_TIPO_DISC:
      tipoDiscapacidadMapping[dataPers["¿Tiene alguna discapacidad?"]],
    ID_ETNIA: etniaMapping[dataPers["Etnia"]],
    ID_EMAIL: dataPers["Email"],
    ID_MAD_CAB_HOGAR:
      madCabHogarMapping[dataPers["¿Es Madre o Padre Cabeza de hogar?"]],
    ID_EDAD_MAYOR: dataPers["Edad de su hijo mayor"],
    ID_EDAD_MENOR: dataPers["Edad de su hijo menor"],
    ID_CANT_HIJOS: dataPers["¿Cuántos hijos tiene?"],
    ID_OCUP_MADRE: ocupMadreMapping[dataPers["Ocupacion de la madre"]],
    ID_OCUP_PADRE: ocupPadreMapping[dataPers["Ocupacion del padre"]],
    ID_CANT_HERMANOS: dataPers["¿Cuántos hermanos tiene?"],
    ID_POS_HERMANO: dataPers["¿Posicion de hijo?"],
    ID_INTEGRANTES: dataPers["Número de miembros en la familia"],
    ID_TALENTO: talentoMapping[dataPers["Talento"]],
    ID_EPS: EPSMapping[dataPers["¿Tiene EPS?"]],
    ID_SISBEN: dataPers["Nivel del sisben"],
    ID_LENTES: LentesMapping[dataPers["¿Usa lentes?"]],
  };
  return resultado;
}

function datasSoci(datasSoci, id) {
  const ocupacionMapping = {
    "Únicamente estudiante": 1,
    Empleado: 2,
    Independiente: 3,
    "Trabaja medio tiempo": 4,
    "Trabaja tiempo completo": 5,
  };

  const viviendaMapping = {
    Familiar: 1,
    Propia: 2,
    Arrendada: 3,
    Otra: 4,
  };

  const yesOrNo = {
    Sí: 1,
    No: 2,
  };

  const nivelAcademicoMapping = {
    Bachiller: 1,
    Tecnico: 2,
    "Tecnico Bachiller": 3,
    Tecnologo: 4,
    Universitario: 5,
  };

  const resultado = {
    ID_ESTUDIANTE: id,
    ID_OCUPACION: ocupacionMapping[datasSoci["¿Tiene usted alguna ocupación?"]],
    ID_ESTRATO: datasSoci["¿Estrato socioeconómico?"],
    ID_TIPO_VIVIENDA: viviendaMapping[datasSoci["¿Tipo de vivienda?"]],
    ID_RECIBE_INGRESOS:
      yesOrNo[datasSoci["¿Recibe usted ingresos mensualmente?"]],
    ID_ACUDIENTE: yesOrNo[datasSoci["¿Alguien lo representa legalmente?"]],
    ID_NIVEL_ACADEMICO:
      yesOrNo[datasSoci["¿Alguien lo representa legalmente?"]],
    ID_NIVEL_ACADEMICO: nivelAcademicoMapping[datasSoci["Nivel académico"]],
    ID_INGRESO_FAMILIAR: datasSoci["¿Cuánto es el ingreso familiar?"],
    ID_TIENE_PC: yesOrNo[datasSoci["¿Posee usted computador?"]],
    ID_TIENE_INTERNET: yesOrNo[datasSoci["¿Tiene acceso a Internet?"]],
    ID_CEL_SMART: yesOrNo[datasSoci["¿Posee usted un celular inteligente?"]],
    ID_PLAN_DATOS: yesOrNo[datasSoci["¿Posee usted un plan de datos?"]],
    ID_INGRESO_TRABAJA:
      yesOrNo[
        datasSoci["¿Al momento de entrar a la universidad usted trabajaba?"]
      ],
  };

  return resultado;
}

function datasAcad(datasAcad, id) {
  const yesOrNo = {
    Sí: 1,
    No: 2,
  };

  const programaMapping = {
    "Lic. en Arte": 22,
    "Lic. Ciencias naturales": 21,
    "Lic. Educacion Fisica": 20,
    Musica: 19,
    "Lic. en Castellano": 18,
    "Lic. Español e ingles": 17,
    "Administracion de empresas": 16,
    "Ing. de Sistemas": 15,
    "Ing. Ambiental": 14,
    "Ing. Agroindustrial": 13,
    "Comercio Internacional": 12,
    Instrumentacion: 11,
    Enfermeria: 10,
    Sociologia: 9,
    "Administracion Turistica": 8,
    Derecho: 7,
    Economia: 6,
    "Contaduria publica": 5,
    "No registra": 4,
    Psicologia: 3,
    Microbiologia: 2,
    "Ing. Electronica": 1,
  };

  const ingresoMapping = {
    Preuniversitario: 1,
    "Aspirante regular": 2,
    "Perteneciente a cabildo indigena": 3,
    Reintegro: 4,
    ReservaCupo: 5,
    TransExterna: 6,
    TransInterna: 7,
    Otro: 8,
    "Deportista destacado": 9,
  };

  const motivacionMapping = {
    Bajo: 1,
    Medio: 2,
    Alto: 3,
    Excelente: 4,
  };

  const tipoColegioMapping = {
    Privado: 1,
    Público: 2,
  };

  const inicioSemestreMapping = {
    "2012-1": 1,
    "2013-1": 2,
    "2013-2": 3,
    "2014-1": 4,
    "2014-2": 5,
    "2015-1": 6,
    "2015-2": 7,
    "2016-1": 8,
    "2016-2": 9,
    "2017-1": 10,
    "2017-2": 11,
    "2018-1": 12,
    "2018-2": 13,
    "2019-1": 14,
    "2019-2": 15,
    "2020-1": 16,
    "2020-2": 17,
    "2021-1": 18,
    "2021-2": 19,
    "2022-1": 20,
    "2022-2": 21,
    "2023-1": 22,
    "2012-2": 23,
    "2010-1": 24,
    "2010-2": 25,
    "2011-1": 26,
    "2011-2": 27,
  };

  const asignatuaEncuestaMapping = {
    nRegistra: 0,
    "Algebra lineal, código MT301B": 1,
    "Algoritmos y fundamentos de programación, Código SS407": 2,
    "Analisis de señales, código EL431": 3,
    "Calculo integral, código MT303B": 4,
    "Circuitos en corriente directa, código EL300": 5,
    "Circuitos I, código EL401": 6,
    "Circuitos II, código EL408": 7,
    "Circuitos III, código EL411": 8,
    "Comunicaciones I, código EL420": 9,
    "Comunicaciones II, código EL425": 10,
    "Control I, código EL417": 11,
    "Control II, código EL422": 12,
    "Digitales I, código EL409": 13,
    "Electiva I Procesamiento de señales": 14,
    "Electiva II Procesamiento de señales": 15,
    "Electiva III Procesamiento de señales": 16,
    "Electrónica de potencia, código EL419": 17,
    "Electrónica I, código EL402": 18,
    "Electrónica II, código EL412": 19,
    "Gestion empresarial y emprendimiento, código MB322": 20,
    "Herramientas de software, código EL436": 21,
    "Instrumentacion, código EL424": 22,
    "Introducción a la ingenieria electrónica, código EL435": 23,
    "Lógica digital, código EL502": 24,
    "Medios de transmisión, código EL445": 25,
    "Modelamiento y simulación, código EL432": 26,
    "Ondas electrómagneticas, código FS315E": 27,
    "Profundización, código EL444": 28,
    "Psicometría, código PS505": 29,
    "Semillero de investigación, código EL437": 30,
    "Semillero de procesamiento de señales TRIAC": 31,
    "Seminario de investigación, código EL439": 32,
    "Tratamiento de señales, código EL433": 33,
    "CATEDRA UPECISTA COD: UPC01": 34,
    "HUMANIDADES I COD: HM301": 35,
    "CALCULO DIFERENCIAL COD: MT302B": 36,
    "TECNICAS DE AUTOAPRENDIZAJE COD: PG312": 37,
    "HUMANIDADES II COD: HM302": 38,
    "LENGUA EXTRANJERA-GRAMATICA COD: UPC04": 39,
    "MECANICA COD: FS314": 40,
    "PROGRAMACION DE COMPUTADORES I COD: SS401": 41,
    "CALCULO MULTIVARIABLE COD: MT304B": 42,
    "ELECTROMAGNETISMO COD: FS311": 43,
    "ESTADISTICA DESCRIPTIVA E INFERENCIAL COD: MT307B": 44,
    "LENGUA EXTRANJERA-LECTURA COD: UPC05": 45,
    "METODOLOGIA DE LA INVESTIGACION COD: EL438": 46,
    "ANALISIS NUMERICO COD: MT309B": 47,
    "ECUACIONES DIFERENCIALES ORDINARIAS COD: MT305B": 48,
    "LENGUA EXTRANJERA-ESCRITURA COD: UPC06": 49,
    "ACTIVIDAD DEPORTIVA COD: UPC08": 50,
    "FISICA MODERNA Y OPTICA COD: FS328": 51,
    "FUNCIONES ESPECIALES Y ECUACIONES DIFERENCIALES COD: MT306B": 52,
    "SEMINARIO DE INVESTIGACION COD: EL439": 53,
    "ACTIVIDAD CULTURAL COD: UPC09": 54,
    "DIGITALES II COD: EL410": 55,
    "ELECTRONICA III COD: EL416": 56,
    "INGENIERIA ECONOMICA COD: AI420": 57,
    "LENGUA EXTRANJERA CONVERSACION COD: UPC07": 58,
    "MAQUINAS ELECTRICAS COD: EL440": 59,
    "DIGITALES III COD: EL403": 60,
    "GERENCIA COD: AE118": 61,
    "LABORATORIO DE DISEÑO INTEGRAL COD: EL441": 62,
    "FORMULACION Y EVALU DE PROYEC EN INGENIERIA COD: FC407": 63,
    "OPTATIVA VIRTUAL COD: EL801": 64,
    "TELEMATICA I COD: EL443": 65,
    "DISEÑO EXPERIMENTAL COD: FC403": 66,
    "PROYECTO I COD: EL447": 67,
    "TELEMATICA II COD: EL446": 68,
    "COMPETENCIAS PEDAGOGICAS COD: PG013": 69,
    "LEGISLACION COD: DR556": 70,
    "PROYECTO II COD: EL448": 71,
  };

  const jornadaAcademMapping = {
    Diurno: 1,
    Nocturno: 2,
  };

  const rendimientoMapping = {
    Bajo: 1,
    Medio: 2,
    Alto: 3,
    Excelente: 4,
  };

  const resultado = {
    ID_ESTUDIANTE: id,
    ID_PROGR_ACTUAL:
      programaMapping[
        datasAcad[
          "Seleccione la carrera universitaria que está estudiando actualmente"
        ]
      ],
    ID_HERMANOS_IES:
      datasAcad["¿Tiene hermanos estudiando actualmente en alguna IES?"],
    ID_INGRESO_UPC:
      ingresoMapping[
        datasAcad[
          "Usted ingresó a la Universidad Popular del Cesar por medio de según su oferta acamédica"
        ]
      ],
    ID_INGRESO_OFERTA:
      yesOrNo[
        datasAcad[
          "Ingresó a la universidad por (Mejor bachiller, preuniversitario o deportista)"
        ]
      ],
    ID_VALIDO_BACH:
      yesOrNo[
        datasAcad[
          "Ingresó a la universidad por (Mejor bachiller, preuniversitario o deportista)"
        ]
      ],
    ID_MOTIVACION:
      motivacionMapping[
        datasAcad[
          "Qué tan motivado te sentías al momento de ingresar a estudiar su carrera profesional"
        ]
      ],
    ID_TIPO_COLEGIO:
      tipoColegioMapping[datasAcad["Tipo de colegio en el que estudio"]],
    ID_SEMESTRE_INICIO:
      inicioSemestreMapping[
        datasAcad[
          "En qué semestre iniciaste tu carrera profesional en la Universidad Popular del Cesar"
        ]
      ],
    ID_REPITIO_ICFES:
      yesOrNo[datasAcad["Repitió usted las pruebas saber 11° ICFES"]],
    ID_PUNTAJE_ICFES: datasAcad["PUNTAJE de las pruebas saber 11° ICFES"],
    ID_PUESTO_ICFES: datasAcad["PERCENTIL de las pruebas saber 11° ICFES"],
    ID_LECTURA_CRITICA: datasAcad["Puntaje de lectura critica"],
    ID_MATEMATICA: datasAcad["Puntaje de matematicas"],
    ID_CIUDADANOS: datasAcad["Puntaje de sociales y ciudadanas"],
    ID_CIENCIAS: datasAcad["Puntaje de ciencias naturales"],
    ID_INGLES: datasAcad["Puntaje de ingles"],
    ID_SEMESTRES_CURSADOS:
      datasAcad["¿Cuántos semestres ha cursado usted actualmente?"],
    ID_UBICACION_SEMESTRE: datasAcad["Su ubicación semestral según el vortal"],
    ID_CREDITOS_APROBADOS: datasAcad["Créditos aprobados hasta el 2023-1"],
    ID_PROMEDIO_ACUMULADO: datasAcad["¿Cual es su promedio acumulado actual?"],
    ID_PROMEDIO_SEMESTRE_ANT:
      datasAcad["¿Cual es su promedio del semestre anterior?"],
    ID_CREDITOS_NO_APROBADOS: datasAcad["Cuantos créditos no aprobados?"],
    ID_CREDITOS_MATRIC: datasAcad["Créditos matriculados este semestre 2023-1"],
    ID_MATERIAS_CANCELADAS:
      datasAcad["¿Ha cancelado alguna asignatura este semestre 2023-1?"],
    ID_ASIGNATURA_ENCUESTA:
      asignatuaEncuestaMapping[
        datasAcad["Desde que asignatura esta haciendo la encuesta"]
      ],
    ID_JORNADA_ACAD: jornadaAcademMapping[datasAcad["Jornada académica"]],
    ID_NOTA_ACTUAL:
      datasAcad[
        "Su nota obtenida actualmente en la asignatura donde esta siendo encuestado"
      ],
    ID_RENDIMIENTO_ACTUAL:
      rendimientoMapping[
        datasAcad["Actual rendimiento académico en la asignatura"]
      ],
    ID_NIVEL_SATISFACION_ASIG:
      rendimientoMapping[datasAcad["Nivel de satisfacción con la asignatura"]],
  };

  return resultado;
}

export const changeDatas = (data, isDoc) => {
  const resultado = {};
  for (const key in data) {
    const value = data[key];
    if (key == "datosEstudiante") {
      resultado[key] = dataPersonal(value);
    } else if (key == "socioeconomica") {
      resultado[key] = datasSoci(value, isDoc);
    } else {
      resultado[key] = datasAcad(value, isDoc);
    }
  }
  return resultado;
};
