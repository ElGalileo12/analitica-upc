function dataPersonal(dataPers) {
  const generoMapping = {
    0: "Otro",
    1: "Masculino",
    2: "Femenino",
  };

  const victimaConMapping = {
    1: "Sí",
    2: "No",
  };

  const estadoCivilMapping = {
    1: "Casado",
    2: "Separado",
    3: "Soltero",
    4: "Unión libre",
    5: "Viudo",
  };

  const tipoDiscapacidadMapping = {
    1: "Movilidad reducida",
    2: "Ninguna",
    3: "Auditiva",
    4: "Visual",
  };

  const etniaMapping = {
    1: "Indigena",
    2: "Palenquero",
    3: "Sin distincion racial",
    4: "Negro, mulato, afrodescendiente, afrocolombiano",
    5: "Raizal",
  };

  const madCabHogarMapping = {
    0: "No Registra",
    1: "Sí",
    2: "No",
  };

  const ocupMadreMapping = {
    0: "No Registra",
    1: "Ama de Casa",
    2: "Estudiante",
    3: "Fallecida",
    4: "Independiente",
    5: "Labora",
    6: "Madre Cabeza de Hogar",
    7: "Pensionada",
  };

  const ocupPadreMapping = {
    0: "No Registra",
    1: "Padre Cabeza de Hogar",
    2: "Pensionado",
    3: "Fallecido",
    4: "Independiente",
    5: "Labora",
  };

  const talentoMapping = {
    0: "No Registra",
    1: "Actor",
    2: "Atletismo",
    3: "Bailarín",
    4: "Baloncesto",
    5: "Fútbol",
    6: "Fútbol sala",
    7: "Músico",
    8: "Natación",
    9: "Softbol",
    10: "Taekwondo",
    11: "Tenis de mesa",
    12: "Voleibol",
  };

  const EPSMapping = {
    0: "No Registra",
    1: "Sí",
    2: "No",
  };

  const LentesMapping = {
    0: "No Registra",
    1: "Sí",
    2: "No",
  };

  const resultado = {
    Nombre: dataPers.ID_NOMBRE || "Valor no definido",
    Edad: dataPers.ID_EDAD || "Valor no definido",
    Telefono: dataPers.ID_NUM_CONTACTO || "Valor no definido",
    Genero: generoMapping[dataPers.ID_GENERO] || "Valor no definido",
    "Victima del conflicto":
      victimaConMapping[dataPers.ID_VIC_CONFLICTO] || "Valor no definido",
    "Estado Civil":
      estadoCivilMapping[dataPers.ID_ESTADO_CIVIL] || "Valor no definido",
    Departamento: dataPers.ID_DPTO_NAC || "Valor no definido",
    Municipio: dataPers.ID_MUN_NAC || "Valor no definido",
    "Tipo de Discapacidad":
      tipoDiscapacidadMapping[dataPers.ID_TIPO_DISC] || "Valor no definido",
    Etnia: etniaMapping[dataPers.ID_ETNIA] || "Valor no definido",
    Email: dataPers.ID_EMAIL || "Valor no definido",
    "Madre Cabeza de Hogar":
      madCabHogarMapping[dataPers.ID_MAD_CAB_HOGAR] || "Valor no definido",
    "Cantidad de hijos": dataPers.ID_CANT_HIJOS || "Valor no definido",
    "Edad hijo Mayor": dataPers.ID_EDAD_MAYOR || "Valor no definido",
    "Edad hijo Menor": dataPers.ID_EDAD_MENOR || "Valor no definido",
    "Ocupación Madre":
      ocupMadreMapping[dataPers.ID_OCUP_MADRE] || "Valor no definido",
    "Ocupación Padre":
      ocupPadreMapping[dataPers.ID_OCUP_PADRE] || "Valor no definido",
    "Cantidad de hermanos": dataPers.ID_CANT_HERMANOS || "Valor no definido",
    "Posición hermanos": dataPers.ID_POS_HERMANO || "Valor no definido",
    Integrantes: dataPers.ID_INTEGRANTES || "Valor no definido",
    Talento: talentoMapping[dataPers.ID_TALENTO] || "Valor no definido",
    EPS: EPSMapping[dataPers.ID_EPS] || "Valor no definido",
    Sisben: dataPers.ID_SISBEN || "Valor no definido",
    Lentes: LentesMapping[dataPers.ID_LENTES] || "Valor no definido",
  };

  return resultado;
}

function datasSoci(datasSoci) {
  const ocupacionMapping = {
    1: "Únicamente estudiante",
    2: "Empleado",
    3: "Independiente",
    4: "Trabaja medio tiempo",
    5: "Trabaja tiempo completo",
  };

  const viviendaMapping = {
    1: "Familiar",
    2: "Propia",
    3: "Arrendada",
    4: "Otra",
  };

  const yesOrNo = {
    1: "Sí",
    2: "No",
  };

  const nivelAcademicoMapping = {
    1: "Bachiller",
    2: "Técnico",
    3: "Técnico Bachiller",
    4: "Tecnólogo",
    5: "Universitario",
  };

  const tienePcMapping = {
    0: "No Registra",
    1: "Sí",
    2: "No",
  };

  const resultado = {
    Ocupacion: ocupacionMapping[datasSoci.ID_OCUPACION] || "Valor no definido",
    Estrato: datasSoci.ID_ESTRATO || "Valor no definido",
    "Tipo de vivienda":
      viviendaMapping[datasSoci.ID_TIPO_VIVIENDA] || "Valor no definido",
    "Recibe ingresos":
      yesOrNo[datasSoci.ID_RECIBE_INGRESOS] || "Valor no definido",
    Acudiente: yesOrNo[datasSoci.ID_ACUDIENTE] || "Valor no definido",
    "Nivel academico":
      nivelAcademicoMapping[datasSoci.ID_NIVEL_ACADEMICO] ||
      "Valor no definido",
    "Ingreso familiar": datasSoci.ID_INGRESO_FAMILIAR || "Valor no definido",
    "Tiene PC": tienePcMapping[datasSoci.ID_TIENE_PC] || "Valor no definido",
    "Tiene internet":
      yesOrNo[datasSoci.ID_TIENE_INTERNET] || "Valor no definido",
    "Tiene celular smart":
      yesOrNo[datasSoci.ID_CEL_SMART] || "Valor no definido",
    "Tiene plan de datos":
      yesOrNo[datasSoci.ID_PLAN_DATOS] || "Valor no definido",
    "Ingresos por trabajar":
      yesOrNo[datasSoci.ID_INGRESO_TRABAJA] || "Valor no definido",
  };

  return resultado;
}

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
    "Programa actual":
      programaMapping[datasAcad.ID_PROGR_ACTUAL] || "Valor no definido",
    "Ingreso a la upc":
      ingresoMapping[datasAcad.ID_INGRESO_UPC] || "Valor no definido",
    "Hermanos IES": datasAcad.ID_HERMANOS_IES || "Valor no definido",
    "Ingreso oferta":
      yesOrNo[datasAcad.ID_INGRESO_OFERTA] || "Valor no definido",
    Motivación:
      motivacionMapping[datasAcad.ID_MOTIVACION] || "Valor no definido",
    "Validó bachiderato":
      yesOrNo[datasAcad.ID_VALIDO_BACH] || "Valor no definido",
    "Tipo de colegio":
      tipoColegioMapping[datasAcad.ID_TIPO_COLEGIO] || "Valor no definido",
    "Inicio semestre":
      inicioSemestreMapping[datasAcad.ID_SEMESTRE_INICIO] ||
      "Valor no definido",
    "Repitió icfes": yesOrNo[datasAcad.ID_REPITIO_ICFES] || "Valor no definido",
    "Puntaje icfes": datasAcad.ID_PUNTAJE_ICFES || "Valor no definido",
    "Puesto icfes": datasAcad.ID_PUESTO_ICFES || "Valor no definido",
    "Lectura crítica": datasAcad.ID_LECTURA_CRITICA || "Valor no definido",
    Matemática: datasAcad.ID_MATEMATICA || "Valor no definido",
    Ciudadanos: datasAcad.ID_CIUDADANOS || "Valor no definido",
    Ciencias: datasAcad.ID_CIENCIAS || "Valor no definido",
    Inglés: datasAcad.ID_INGLES || "Valor no definido",
    "Ubicación semestre":
      datasAcad.ID_UBICACION_SEMESTRE || "Valor no definido",
    "Créditos aprobados":
      datasAcad.ID_CREDITOS_APROBADOS || "Valor no definido",
    "Promedio acumulado":
      datasAcad.ID_PROMEDIO_ACUMULADO || "Valor no definido",
    "Promedio semestre anterior":
      datasAcad.ID_PROMEDIO_SEMESTRE_ANT || "Valor no definido",
    "Crérditos no aprobados":
      datasAcad.ID_CREDITOS_NO_APROBADOS || "Valor no definido",
    "Créditos matriculados":
      datasAcad.ID_CREDITOS_MATRIC || "Valor no definido",
    "Materias canceladas":
      datasAcad.ID_MATERIAS_CANCELADAS || "Valor no definido",
    "Asignatura Encuesta":
      asignatuaEncuestaMapping[datasAcad.ID_ASIGNATURA_ENCUESTA] ||
      "Valor no definido",
    "Jornada académica":
      jornadaAcademMapping[datasAcad.ID_JORNADA_ACAD] || "Valor no definido",
    "Nota actual": datasAcad.ID_NOTA_ACTUAL || "Valor no definido",
    "Rendimiento actual":
      rendimientoMapping[datasAcad.ID_RENDIMIENTO_ACTUAL] ||
      "Valor no definido",
    "Nivel satisfacción asignatura":
      rendimientoMapping[datasAcad.ID_NIVEL_SATISFACION_ASIG] ||
      "Valor no definido",
  };

  return resultado;
}

export const changeId = (data) => {
  const resultado = {};

  for (const key in data) {
    const value = data[key];
    if (key == "datasPers") {
      resultado[key] = dataPersonal(value);
    } else if (key == "datasSoci") {
      resultado[key] = datasSoci(value);
    } else {
      resultado[key] = datasAcad(value);
    }
  }

  // resultado es el nuevo objeto con las traducciones
  console.log("Nuevo objeto:", resultado);

  return resultado;
};
