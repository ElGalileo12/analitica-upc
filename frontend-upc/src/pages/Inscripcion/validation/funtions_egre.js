function dataPersonal(dataPers) {
  const tipoDocMapping = {
    Cédula: "cedulaCiudadania",
    "Tarjeta de identidad": "tarjetaIdentidad",
    Pasaporte: "Pasaporte"
  };

  const generoMapping = {
    Otro: 0,
    Masculino: 1,
    Femenino: 2,
  };

  const estadoCivilMapping = {
    Casado: 1,
    Separado: 2,
    Soltero: 3,
    "Unión libre": 4,
    "Viudo(a)": 5,
    
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
    "Sin distincion racial": 3,
    "Negro, mulato, afrodescendiente, afrocolombiano": 4,
    Raizal: 5,
    "Rrom o Gitano": 6,
  };

  const resultado = {
    ID_DOCUMENTO: dataPers.Documento,
    ID_TIPO_DOCUMENTO: tipoDocMapping[dataPers["Tipo de documento"]],
    ID_NOMBRE: dataPers["Nombre"],
    ID_NUM_CONTACTO: dataPers["Telefono"],
    ID_GENERO: generoMapping[dataPers["Genero"]],
    ID_EDAD: dataPers["Edad"],
    ID_ESTADO_CIVIL: estadoCivilMapping[dataPers["Estado Civil"]],
    ID_ETNIA: etniaMapping[dataPers["Etnia"]],
    ID_DISCAPACIDAD:tipoDiscapacidadMapping[dataPers["¿Tiene alguna discapacidad?"]],
    ID_EMAIL: dataPers["Email"],
    ID_ESTRATO: dataPers["Estrato"]
  };
  return resultado;
}

function datasAcade(datasAcad, id) {
  const tituloMapping = {
    "Ing. Electronica": 1,
    "Ing. Electronica": 2,
    "Ing. Electronica": 3,
  };
  
  const practicasMapping = {
    "Si": 1,
    "No": 2,
  };
  
  const postMapping = {
    "Si": 1,
    "No": 2,
  };
  
  const postnivelMapping = {
    "Especialización": 1,
    "Maestría": 2,
    "Doctorado": 3,
    "Pos-Doctorado": 4,
    "Ninguno": 5,
  };
  
  const postlugarMapping = {
    "Nacional": 1,
    "Extranjera": 2,
    "Ninguno": 3,
  };
  
  const segundalenguaMapping = {
    "Si": 1,
    "No": 2,
  };
  
  const nivellenguaMapping = {
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4,
    "C1": 5,
    "C2": 6,
  };
  
  const yesOrNo = {
    Sí: 1,
    No: 2,
  };

  const resultado = {
    ID_EGRESADO: id,
      ID_TITULO: tituloMapping[datasAcad["Titulo"]],
      ID_SEMESTRE_INICIO: datasAcad["Semestre de inicio"],
      ID_SEMESTRES_CURSADOS: datasAcad["Semestre Cursados"],
      ID_PROMEDIO_ACUMULADO: datasAcad["Promedio Acumulado"],
      ID_SEMESTRE_FIN: datasAcad["Año de finalizacion pregrado"],
      ID_FECHA_GRADO: datasAcad["Año de grado"],
      ID_SEGNDALENGUA: segundalenguaMapping[datasAcad["¿Domina una segunda lengua?"]],
      ID_NIVEL: nivellenguaMapping[datasAcad["¿Cuál nivel?"]],
      ID_PRACTICAS: practicasMapping[datasAcad["¿Hizo practicas?"]],
      ID_POSTGRADO: postMapping[datasAcad["¿Tiene estudios de postgrados?"]],
      ID_POSTGRADO_NIVEL: postnivelMapping[datasAcad["Último estudio de posgrado"]],
      ID_POSTGRADO_LUGAR: postlugarMapping[datasAcad["Nivel del posgrado"]]
  };

  return resultado;
}

function dastasLaboral(dastasLabo, id) {
  const trabajaMapping = {
    "Si": 1,
    "No": 2,
  };
  
  const trabaja_situacion_Mapping = {
    "Empleado": 1,
    "Independiente": 2,
  };
  
  const trabaja_perfil_Mapping = {
    "Sí": 1,
    "No": 2,
  };
  
  const trabaja_sector_Mapping = {
    "Agropecuario": 1,
    "Industrial": 2,
    "Transporte": 3,
    "Comercial": 4,
    "Comunicaciones": 5,
    "Minero y energético": 6,
    "Salud": 7,
    "Educación": 8,
  };
  
  const trabaja_tiempo_Mapping = {
    "Menos de seis meses": 1,
    "Entre seis meses y un año": 2,
    "Más de un año": 3,
    "Más de dos años": 4,
  };
  
  const trabaja_nivel_Mapping = {
    "Técnico": 1,
    "Supervisor": 2,
    "Jefe de área": 3,
    "Funcionario": 4,
    "Directivo": 5,
    "Empresario": 6,
  };
  
  const trabaja_tiempo_primer_Mapping = {
    "Antes de graduarse": 1,
    "Menos de seis meses": 2,
    "Entre seis meses y un año": 3,
    "Más de un año": 4,
  };
  
  const trabaja_medio_Mapping = {
    "Bolsa de trabajo de la Universidad": 1,
    "Contactos personales": 2,
    "Residencia profesional": 3,
    "Medios masivos de comunicación": 4,
    "Concurso de mérito": 5,
  };
  
  const trabaja_sector_dos = {
    "Pública": 1,
    "Privada": 2,
  };
  
  const trabaja_sector_tres = {
    "Investigación": 1,
    "Industria": 2,
    "Administrativo": 3,
    "Comercial": 4,
    "Educación": 5,
    "Desarrollo de Software": 6,
    "Minero": 7,
    "Salud": 8,
    "Comunicaciones": 9,
    "OTRA": 10,
  };
  
  const trabaja_requisitos = {
    "Competencias laborales": 1,
    "Título profesional": 2,
    "Examen de Selección": 3,
    "Idioma extranjero": 4,
    "Todas las anteriores": 5,
    "Ninguno": 6,
  };
  
  const trabaja_rango = {
    "Entre 1 un SMMLV y 3 un SMMLV": 1,
    "Entre 3 un SMMLV y 5 un SMMLV": 2,
    "Mas de 5 SMMLV": 3,
  };
  
  const trabaja_reconocimiento = {
    "Sí": 1,
    "No": 2,
  };
  
  const trabaja_Empresa = {
    "Sí": 1,
    "No": 2,
  };
  
  const trabaja_Empresa_antes = {
    "Sí": 1,
    "No": 2,
  };
  
  const experiencia = {
    "de 0 a 3 años": 1,
    "de 3 a 5 años": 2,
    "más de 5 años": 3,
  };
  
  const resultado = {
    ID_EGRESADO: id,
    ID_TRABAJA: trabajaMapping[dastasLabo["¿Trabaja actualmente?"]],
    ID_TRABAJA_NOMBRE_EMPRESA: dastasLabo["Nombre de la empresa"],
    ID_EXP_ACOMU: experiencia[dastasLabo["Experiencia en la empresa"]],
    ID_TRABAJA_PAIS: dastasLabo["Pais donde trabaja"],
    ID_TRABAJA_CIUDAD: dastasLabo["Ciudad donde trabaja"],
    ID_TRABAJA_SITUACION: trabaja_situacion_Mapping[dastasLabo["Situación laboral actual"]],
    ID_TRABAJA_PERFIL: trabaja_perfil_Mapping[dastasLabo["Es su trabajo acorde a su perfil profesional"]],
    ID_TRABAJA_SECTOR: trabaja_sector_Mapping[dastasLabo["Sector donde trabaja"]],
    ID_TRABAJA_TIEMPO: trabaja_tiempo_Mapping[dastasLabo["Tiempo transcurrido para la contratación en su empleo actual"]],
    ID_TRABAJA_NIVEL: trabaja_nivel_Mapping[dastasLabo["Nivel jerárquico en el trabajo"]],
    ID_TRABAJA_TIEMPO_PRIMER: trabaja_tiempo_primer_Mapping[dastasLabo["Primer empleo"]],
    ID_TRABAJA_MEDIO: trabaja_medio_Mapping[dastasLabo["Medio usado para obtener el empleo"]],
    ID_TRABAJA_SECTOR_DOS: trabaja_sector_dos[dastasLabo["Sector en los que se ha desempeñado"]],
    ID_TRABAJA_SECTOR_TRES: trabaja_sector_tres[dastasLabo["Sector productivo en el que ha laborado"]],
    ID_TRABAJA_REQUISITOS: trabaja_requisitos[dastasLabo["Requisitos que para su contratación"]],
    ID_TRABAJA_RANGO: trabaja_rango[dastasLabo["Rango salarial actualmente"]],
    ID_TRABAJA_RECONOCIMIENTO: trabaja_reconocimiento[dastasLabo["Ha tenido reconocimiento en el trabajo"]],
    ID_EMPRESA: trabaja_Empresa[dastasLabo["¿Tiene empresa?"]],
    ID_NOMBRE_EMPRESA: dastasLabo["Nombre de su empresa"],
    ID_UBICACION_EMPRESA: dastasLabo["Ubicación de la empresa"],
    ID_EMPRESA_ANTES: trabaja_Empresa_antes[dastasLabo["Creó su empresa antes de graduarse?"]],
    ID_EMPRESA_SECTOR: dastasLabo["Sector de la empresa"],
  };

  return resultado;
}

function datasMoti(datasMot, id) {
  const mot_pregrado_Mapping = {
    "Muy bajo": 1,
    "Bajo": 2,
    "Bueno": 3,
    "Alto": 4,
    "Excelente": 5,
  };
  
  const mot_volumen_Mapping = {
    "Muy bajo": 1,
    "Poco": 2,
    "Regular": 3,
    "Exigente": 4,
    "Muy exigente": 5,
  };
  
  const mot_nivels_Mapping = {
    "Muy bajo": 1,
    "Bajo": 2,
    "Bueno": 3,
    "Alto": 4,
    "Muy alto": 5,
  };
  
  const mot_ambiente_Mapping = {
    "Muy bajo": 1,
    "Bajo": 2,
    "Bueno": 3,
    "Alto": 4,
    "Muy alto": 5,
  };
  
  const mot_fortalecer_Mapping = {
    "Si": 1,
    "No": 2,
  };
  
  const mot_apoyo_Mapping = {
    "Si": 1,
    "No": 2,
  };
  
  const mot_recursos_Mapping = {
    "Muy poco adecuados": 1,
    "Adecuados": 2,
    "Muy adecuados": 3,
  };
  
  const mot_modalidad_Mapping = {
    "Prácticas": 1,
    "Trabajo final de carrera": 2,
  };
  
  const mot_modalidad_p_Mapping = {
    "Muy poco": 1,
    "Poco": 2,
    "Moderado": 3,
    "Alto": 4,
    "Muy alto": 5,
  };
  
  const mot_modalidad_t_Mapping = {
    "Muy poco": 1,
    "Poco": 2,
    "Moderado": 3,
    "Alto": 4,
    "Muy alto": 5,
  };
  
  const mot_profundizacion_Mapping = {
    "Optoelectrónica": 1,
    "Telecomunicaciones": 2,
    "Instrumentación Electrónica": 3,
    "Procesamiento de Señales": 4,
    "Automatización y Control": 5,
    "Bioingeniería": 6,
  };
  
  const mot_ingresar_Mapping = {
    "Mala": 1,
    "Buena": 2,
    "Excelente": 3,
  };
  
  const mot_conocimientos_Mapping = {
    "Muy poco": 1,
    "Poco": 2,
    "Regularmente": 3,
    "La mayoría de las veces": 4,
    "Siempre": 5,
  };
  
  const mot_contribucion_Mapping = {
    "Muy poco": 1,
    "Poco": 2,
    "Moderado": 3,
    "Alto": 4,
    "Muy alto": 5,
  };
  
  const mot_calidad_Mapping = {
    "Totalmente en desacuerdo": 1,
    "En desacuerdo": 2,
    "Ni de acuerdo ni en desacuerdo": 3,
    "De acuerdo": 4,
    "Totalmente de acuerdo": 5,
  };
  
  const mot_favorecido_Mapping = {
    "Totalmente en desacuerdo": 1,
    "En desacuerdo": 2,
    "Ni de acuerdo ni en desacuerdo": 3,
    "De acuerdo": 4,
    "Totalmente de acuerdo": 5,
  };
  
  const mot_post_cont_Mapping = {
    "Si": 1,
    "No": 2,
  };
  
  const mot_servicio_Mapping = {
    "Carnetización": 1,
    "Biblioteca": 2,
    "Espacio Deportivo": 3,
    "Otros": 4,
    "Ninguno": 5,
  };
  
  const mot_carnet_Mapping = {
    "Si": 1,
    "No": 2,
  };
  
  
  const resultado = {
    ID_EGRESADO: id,
    ID_MOT_PREGRADO: mot_pregrado_Mapping[datasMot["Motivacion del pregrado"]],
    ID_MOT_VOLUMEN: mot_volumen_Mapping[datasMot["Volumen de trabajo exigido"]],
    ID_MOT_NIVELS: mot_nivels_Mapping[datasMot["Nivel de satisfacción entre las horas teóricas y prácticas"]],
    ID_MOT_AMBIENTE: mot_ambiente_Mapping[datasMot["Ambiente de aprendizaje"]],
    ID_MOT_FORTALECER: mot_fortalecer_Mapping[datasMot["Se deben fortalecer algunas materias?"]],
    ID_MOT_MATERIAS: datasMot["Materias a fortalecer"],
    ID_MOT_APOYO: mot_apoyo_Mapping[datasMot["La institución le brindó servicios de apoyo"]],
    ID_MOT_SERVICIO: mot_servicio_Mapping[datasMot["¿Ha utilizado como egresado algún servicio de la universidad?"]],
    ID_MOT_SERVICIO_DESEADO: datasMot["¿Qué servicio le gustaría que ofreciera la institución como egresado?"],
    ID_MOT_CARNET: mot_carnet_Mapping[datasMot["¿Cuenta con carnet de egresado?"]],
    ID_MOT_RECURSOS: mot_recursos_Mapping[datasMot["Los recursos de la institución fueron adecuados"]],
    ID_MOT_MODALIDAD: mot_modalidad_Mapping[datasMot["¿Cuál fue su modalidad de grado?"]],
    ID_MOT_MODALIDAD_P: mot_modalidad_p_Mapping[datasMot["Las Prácticas te han permitido aplicar los conocimientos"]],
    ID_MOT_MODALIDAD_T: mot_modalidad_t_Mapping[datasMot["El trabajo final le ha sido de utilidad para aplicar conocimientos?"]],
    ID_MOT_PROFUNDIZACION: mot_profundizacion_Mapping[datasMot["Linea de profundización del trabajo final"]],
    ID_MOT_INGRESAR: mot_ingresar_Mapping[datasMot["¿Cómo evalúa las expectativas de formación profesional que tenía al ingresar?"]],
    ID_MOT_CONOCIMIENTOS: mot_conocimientos_Mapping[datasMot["¿En qué medida ha aplicado los conocimientos adquiridos de su carrera en su ocupación profesional?"]],
    ID_MOT_CONTRIBUCION: mot_contribucion_Mapping[datasMot["En qué medida cree que ha contribuido con su trabajo al desarrollo de su comunidad, ciudad, región y/o empresa?"]],
    ID_MOT_CALIDAD: mot_calidad_Mapping[datasMot["¿Usted considera que la formación recibida en el programa fue de Calidad?"]],
    ID_MOT_FAVORECIDO: mot_favorecido_Mapping[datasMot["¿El programa del cual egresó ha favorecido en su proyecto de vida?"]],
    ID_MOT_POST_CONT: mot_post_cont_Mapping[datasMot["Daría continuidad a estudio de posgrado en la institución"]]
    
  };

  return resultado;
}

export const changeDatas = (data, isDoc) => {
  const resultado = {};
  for (const key in data) {
    const value = data[key];
    if (key == "datosEgresado") {
      resultado[key] = dataPersonal(value);
    } else if (key == "infoacademica") {
      resultado[key] = datasAcade(value);
    } else if (key == "infolaboral") {
      resultado[key] = dastasLaboral(value);
    } else {
      resultado[key] = datasMoti(value);
    }
  }
  return resultado;
};
