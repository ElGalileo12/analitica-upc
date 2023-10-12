function datasAcad(datasAcad) {
  const programaMapping = {
    22: "Lic. en Arte",
    21: "Lic. Ciencias naturales",
    20: "Lic. Educacion Fisica",
    19: "Musica",
    18: "Lic. en Castellano",
    17: "Lic. Español e ingles",
    16: "Administracion de empresas",
    15: "Ing. de Sistemas",
    14: "Ing. Ambiental",
    13: "Ing. Agroindustrial",
    12: "Comercio Internacional",
    11: "Instrumentacion",
    10: "Enfermeria",
    9: "Sociologia",
    8: "Administracion Turistica",
    7: "Derecho",
    6: "Economia",
    5: "Contaduria publica",
    4: "No registra",
    3: "Psicologia",
    2: "Microbiologia",
    1: "Ing. Electronica",
  };

  const ingresoMapping = {
    1: "Preuniversitario",
    2: "Aspirante regular",
    3: "Perteneciente a cabildo indigena",
    4: "Reintegro",
    5: "ReservaCupo",
    6: "TransExterna",
    7: "TransInterna",
    8: "Otro",
    9: "Deportista destacado",
  };

  const yesOrNo = {
    1: "Sí",
    2: "No",
  };

  const motivacionMapping = {
    1: "Bajo",
    2: "Medio",
    3: "Alto",
    4: "Excelente",
  };

  const tipoColegioMapping = {
    1: "Privado",
    2: "Público",
  };

  const inicioSemestreMapping = {
    1: "2012-1",
    2: "2013-1",
    3: "2013-2",
    4: "2014-1",
    5: "2014-2",
    6: "2015-1",
    7: "2015-2",
    8: "2016-1",
    9: "2016-2",
    10: "2017-1",
    11: "2017-2",
    12: "2018-1",
    13: "2018-2",
    14: "2019-1",
    15: "2019-2",
    16: "2020-1",
    17: "2020-2",
    18: "2021-1",
    19: "2021-2",
    20: "2022-1",
    21: "2022-2",
    22: "2023-1",
    23: "2012-2",
    24: "2010-1",
    25: "2010-2",
    26: "2011-1",
    27: "2011-2",
  };

  const asignatuaEncuestaMapping = {
    0: "nRegistra",
    1: "Algebra lineal, código MT301B",
    2: "Algoritmos y fundamentos de programación, Código SS407",
    3: "Analisis de señales, código EL431",
    4: "Calculo integral, código MT303B",
    5: "Circuitos en corriente directa, código EL300",
    6: "Circuitos I, código EL401",
    7: "Circuitos II, código EL408",
    8: "Circuitos III, código EL411",
    9: "Comunicaciones I, código EL420",
    10: "Comunicaciones II, código EL425",
    11: "Control I, código EL417",
    12: "Control II, código EL422",
    13: "Digitales I, código EL409",
    14: "Electiva I Procesamiento de señales",
    15: "Electiva II Procesamiento de señales",
    16: "Electiva III Procesamiento de señales",
    17: "Electrónica de potencia, código EL419",
    18: "Electrónica I, código EL402",
    19: "Electrónica II, código EL412",
    20: "Gestion empresarial y emprendimiento, código MB322",
    21: "Herramientas de software, código EL436",
    22: "Instrumentacion, código EL424",
    23: "Introducción a la ingenieria electrónica, código EL435",
    24: "Lógica digital, código EL502",
    25: "Medios de transmisión, código EL445",
    26: "Modelamiento y simulación, código EL432",
    27: "Ondas electrómagneticas, código FS315E",
    28: "Profundización, código EL444",
    29: "Psicometría, código PS505",
    30: "Semillero de investigación, código EL437",
    31: "Semillero de procesamiento de señales TRIAC",
    32: "Seminario de investigación, código EL439",
    33: "Tratamiento de señales, código EL433",
    34: "CATEDRA UPECISTA COD: UPC01",
    35: "HUMANIDADES I COD: HM301",
    36: "CALCULO DIFERENCIAL COD: MT302B",
    37: "TECNICAS DE AUTOAPRENDIZAJE COD: PG312",
    38: "HUMANIDADES II COD: HM302",
    39: "LENGUA EXTRANJERA-GRAMATICA COD: UPC04",
    40: "MECANICA COD: FS314",
    41: "PROGRAMACION DE COMPUTADORES I COD: SS401",
    42: "CALCULO MULTIVARIABLE COD: MT304B",
    43: "ELECTROMAGNETISMO COD: FS311",
    44: "ESTADISTICA DESCRIPTIVA E INFERENCIAL COD: MT307B",
    45: "LENGUA EXTRANJERA-LECTURA COD: UPC05",
    46: "METODOLOGIA DE LA INVESTIGACION COD: EL438",
    47: "ANALISIS NUMERICO COD: MT309B",
    48: "ECUACIONES DIFERENCIALES ORDINARIAS COD: MT305B",
    49: "LENGUA EXTRANJERA-ESCRITURA COD: UPC06",
    50: "ACTIVIDAD DEPORTIVA COD: UPC08",
    51: "FISICA MODERNA Y OPTICA COD: FS328",
    52: "FUNCIONES ESPECIALES Y ECUACIONES DIFERENCIALES COD: MT306B",
    53: "SEMINARIO DE INVESTIGACION COD: EL439",
    54: "ACTIVIDAD CULTURAL COD: UPC09",
    55: "DIGITALES II COD: EL410",
    56: "ELECTRONICA III COD: EL416",
    57: "INGENIERIA ECONOMICA COD: AI420",
    58: "LENGUA EXTRANJERA CONVERSACION COD: UPC07",
    59: "MAQUINAS ELECTRICAS COD: EL440",
    60: "DIGITALES III COD: EL403",
    61: "GERENCIA COD: AE118",
    62: "LABORATORIO DE DISEÑO INTEGRAL COD: EL441",
    63: "FORMULACION Y EVALU DE PROYEC EN INGENIERIA COD: FC407",
    64: "OPTATIVA VIRTUAL COD: EL801",
    65: "TELEMATICA I COD: EL443",
    66: "DISEÑO EXPERIMENTAL COD: FC403",
    67: "PROYECTO I COD: EL447",
    68: "TELEMATICA II COD: EL446",
    69: "COMPETENCIAS PEDAGOGICAS COD: PG013",
    70: "LEGISLACION COD: DR556",
    71: "PROYECTO II COD: EL448",
  };

  const jornadaAcademMapping = {
    1: "Diurno",
    2: "Nocturno",
  };

  const rendimientoMapping = {
    1: "Bajo",
    2: "Medio",
    3: "Alto",
    4: "Excelente",
  };

  const resultado = {
    "Seleccione la carrera universitaria que está estudiando actualmente":
      programaMapping[datasAcad.ID_PROGR_ACTUAL] || "Valor no definido",
    "Su nota obtenida actualmente en la asignatura donde esta siendo encuestado":
      datasAcad.ID_NOTA_ACTUAL,
    "Usted ingresó a la Universidad Popular del Cesar por medio de según su oferta acamédica":
      ingresoMapping[datasAcad.ID_INGRESO_OFERTA] || "Valor no definido",
    "Ingresó a la universidad por (Mejor bachiller, preuniversitario o deportista)":
      yesOrNo[datasAcad.ID_INGRESO_UPC] || "Valor no definido",
    "Qué tan motivado te sentías al momento de ingresar a estudiar su carrera profesional":
      motivacionMapping[datasAcad.ID_MOTIVACION] || "Valor no definido",
    "En qué semestre iniciaste tu carrera profesional en la Universidad Popular del Cesar":
      inicioSemestreMapping[datasAcad.ID_SEMESTRE_INICIO] ||
      "Valor no definido",
    "Tipo de colegio en el que estudio":
      tipoColegioMapping[datasAcad.ID_TIPO_COLEGIO] || "Valor no definido",
    "Validó el bachillerato":
      yesOrNo[datasAcad.ID_VALIDO_BACH] || "Valor no definido",
    "Repitió usted las pruebas saber 11° ICFES":
      yesOrNo[datasAcad.ID_REPITIO_ICFES] || "Valor no definido",
    "PUNTAJE de las pruebas saber 11° ICFES":
      datasAcad.ID_PUNTAJE_ICFES || "Valor no definido",
    "PERCENTIL de las pruebas saber 11° ICFES":
      datasAcad.ID_PUESTO_ICFES || "Valor no definido",
    "Puntaje de lectura critica":
      datasAcad.ID_LECTURA_CRITICA || "Valor no definido",
    "Puntaje de matematicas": datasAcad.ID_MATEMATICA || "Valor no definido",
    "Puntaje de sociales y ciudadanas":
      datasAcad.ID_CIUDADANOS || "Valor no definido",
    "Puntaje de ciencias naturales":
      datasAcad.ID_CIENCIAS || "Valor no definido",
    "Puntaje de ingles": datasAcad.ID_INGLES || "Valor no definido",
    "¿Cuántos semestres ha cursado usted actualmente?":
      datasAcad.ID_SEMESTRES_CURSADOS || "Valor no definido",
    "Su ubicación semestral según el vortal":
      datasAcad.ID_UBICACION_SEMESTRE || "Valor no definido",
    "Créditos aprobados hasta el 2023-1":
      datasAcad.ID_CREDITOS_APROBADOS || "Valor no definido",
    "¿Cual es su promedio acumulado actual?":
      datasAcad.ID_PROMEDIO_ACUMULADO || "Valor no definido",
    "¿Cual es su promedio del semestre anterior?":
      datasAcad.ID_PROMEDIO_SEMESTRE_ANT || "Valor no definido",
    "Cuantos créditos no aprobados?": datasAcad.ID_CREDITOS_NO_APROBADOS,
    "Créditos matriculados este semestre 2023-1":
      datasAcad.ID_CREDITOS_MATRIC || "Valor no definido",
    "Desde que asignatura esta haciendo la encuesta":
      asignatuaEncuestaMapping[datasAcad.ID_ASIGNATURA_ENCUESTA] ||
      "Valor no definido",
    "Jornada académica":
      jornadaAcademMapping[datasAcad.ID_JORNADA_ACAD] || "Valor no definido",
    "Actual rendimiento académico en la asignatura":
      rendimientoMapping[datasAcad.ID_RENDIMIENTO_ACTUAL] ||
      "Valor no definido",
    "Nivel de satisfacción con la asignatura":
      rendimientoMapping[datasAcad.ID_NIVEL_SATISFACION_ASIG] ||
      "Valor no definido",
    "¿Tiene hermanos estudiando actualmente en alguna IES?":
      datasAcad.ID_HERMANOS_IES,
    "¿Ha cancelado alguna asignatura este semestre 2023-1?":
      datasAcad.ID_MATERIAS_CANCELADAS,
  };

  return resultado;
}

export const changeAcad = (data) => {
  const resultado = {};

  for (const key in data) {
    const value = data[key];
    if (key == "datasAcad") {
      resultado[key] = datasAcad(value);
    }
  }

  return resultado;
};
