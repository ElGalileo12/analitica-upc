function datasLabo(datasLab) {
  const trabajaMapping = {
    1: "Si",
    2: "No",
  };

  const trabaja_situacion_Mapping = {
    1: "Empleado",
    2: "Independiente",
  };

  const trabaja_perfil_Mapping = {
    1: "Sí",
    2: "No",
  };

  const trabaja_sector_Mapping = {
    1: "Agropecuario",
    2: "Industrial",
    3: "Transporte",
    4: "Comercial",
    5: "Comunicaciones",
    6: "Minero y energético",
    7: "Salud",
    8: "Educación",
  };

  const trabaja_tiempo_Mapping = {
    1: "Menos de seis meses",
    2: "Entre seis meses y un año",
    3: "Más de un año",
    4: "Más de dos años",
  };

  const trabaja_nivel_Mapping = {
    1: "Técnico",
    2: "Supervisor",
    3: "Jefe de área",
    4: "Funcionario",
    5: "Directivo",
    6: "Empresario",
  };

  const trabaja_tiempo_primer_Mapping = {
    1: "Antes de graduarse",
    2: "Menos de seis meses",
    3: "Entre seis meses y un año",
    4: "Más de un año",
  };

  const trabaja_medio_Mapping = {
    1: "Bolsa de trabajo de la Universidad",
    2: "Contactos personales",
    3: "Residencia profesional",
    4: "Medios masivos de comunicación",
    5: "Concurso de merito",
  };

  const trabaja_sector_dos = {
    1: "Pública",
    2: "Privada",
  };

  const trabaja_sector_tres = {
    1: "Investigación",
    2: "Industria",
    3: "Administrativo",
    4: "Comercial",
    5: "Educación",
    6: "Desarrollo de Software",
    7: "Minero",
    8: "Salud",
    9: "Comunicaciones",
    10: "OTRA",
  };

  const trabaja_requisitos = {
    1: "Competencias laborales",
    2: "Título profesional",
    3: "Examen de Selección",
    4: "Idioma extranjero",
    5: "Todas las anteriores",
    6: "Ninguno",
  };

  const trabaja_rango = {
    1: "Entre 1 un SMMLV y 3 un SMMLV",
    2: "Entre 3 un SMMLV y 5 un SMMLV",
    3: "Mas de 5 SMMLV",
  };

  const trabaja_reconocimiento = {
    1: "Sí",
    2: "No",
  };

  const trabaja_Empresa = {
    1: "Sí",
    2: "No",
  };

  const trabaja_Empresa_antes = {
    1: "Sí",
    2: "No",
  };

  const experiencia = {
    1:	"de 0 a 3 años",
    2:	"de 3 a 5 años",
    3:	"más de 5 años"
  };

  const resultado = {
  "¿Trabaja actualmente?": trabajaMapping[datasLab.ID_TRABAJA] || "Valor no definido",
  "Nombre de la empresa": datasLab.ID_TRABAJA_NOMBRE_EMPRESA|| "Valor no definido",
  "Experiencia en la empresa": experiencia[datasLab.ID_EXP_ACOMU] || "Valor no definido",
  "Pais donde trabaja": datasLab.ID_TRABAJA_PAIS || "Valor no definido",
  "Ciudad donde trabaja": datasLab.ID_TRABAJA_CIUDAD || "Valor no definido",
  "Situación laboral actual": trabaja_situacion_Mapping[datasLab.ID_TRABAJA_SITUACION] || "Valor no definido",
  "Es su trabajo acorde a su perfil profesional": trabaja_perfil_Mapping[datasLab.ID_TRABAJA_PERFIL] || "Valor no definido",
  "Sector donde trabaja": trabaja_sector_Mapping[datasLab.ID_TRABAJA_SECTOR] || "Valor no definido",
  "Tiempo transcurrido para la contratación en su empleo actual": trabaja_tiempo_Mapping[datasLab.ID_TRABAJA_TIEMPO] || "Valor no definido",
  "Nivel jerárquico en el trabajo": trabaja_nivel_Mapping[datasLab.ID_TRABAJA_NIVEL] || "Valor no definido",
  "Primer empleo": trabaja_tiempo_primer_Mapping[datasLab.ID_TRABAJA_TIEMPO_PRIMER] || "Valor no definido",
  "Medio usado para obtener el empleo": trabaja_medio_Mapping[datasLab.ID_TRABAJA_MEDIO] || "Valor no definido",
  "Sector en los se ha desempeñado": trabaja_sector_dos[datasLab.ID_TRABAJA_SECTOR_DOS] || "Valor no definido",
  "Sector productivo en el que ha laborado": trabaja_sector_tres[datasLab.ID_TRABAJA_SECTOR_TRES] || "Valor no definido",
  "Requisitos que para su contratación": trabaja_requisitos[datasLab.ID_TRABAJA_REQUISITOS] || "Valor no definido",
  "Rango salarial actualmente": trabaja_rango[datasLab.ID_TRABAJA_RANGO] || "Valor no definido",
  "Ha tenido reconocimiento en el trabajo": trabaja_reconocimiento[datasLab.ID_TRABAJA_RECONOCIMIENTO] || "Valor no definido",
  "Tiene empresa?": trabaja_Empresa[datasLab.ID_EMPRESA] || "Valor no definido",
  "Nombre de su empresa": datasLab.ID_NOMBRE_EMPRESA || "Valor no definido",
  "Ubicacion de la empresa": datasLab.ID_UBICACION_EMPRESA || "Valor no definido",
  "Creo su empresa antes de graduarse?": trabaja_Empresa_antes[datasLab.ID_EMPRESA_ANTES] || "Valor no definido",
  "Sector de la empresa": datasLab.ID_EMPRESA_SECTOR || "Valor no definido",
  };

  return resultado;
}

function datasMoti(datasMot) {
  const mot_pregrado_Mapping = {
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Excelente",
  };
  
  const mot_volumen_Mapping = {
    1: "Muy bajo",
    2: "Poco",
    3: "Regular",
    4: "Exigente",
    5: "Muy exigente",
  };
  
  const mot_nivels_Mapping = {
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Muy alto",
  };
  
  const mot_ambiente_Mapping = {
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Muy alto",
  };
  
  const mot_fortalecer_Mapping = {
    1: "Si",
    2: "No",
  };
  
  const mot_apoyo_Mapping = {
    1: "Si",
    2: "No",
  };
  
  const mot_recursos_Mapping = {
    1: "Muy poco adecuados",
    2: "Adecuados",
    3: "Muy adecuados",
  };
  
  const mot_modalidad_Mapping = {
    1: "Prácticas",
    2: "Trabajo final de carrera",
  };
  
  const mot_modalidad_p_Mapping = {
    1: "Muy poco",
    2: "Poco",
    3: "Moderado",
    4: "Alto",
    5: "Muy alto",
  };
  
  const mot_modalidad_t_Mapping = {
    1: "Muy poco",
    2: "Poco",
    3: "Moderado",
    4: "Alto",
    5: "Muy alto",
  };
  
  const mot_profundizacion_Mapping = {
    1: "Optoelectrónica",
    2: "Telecomunicaciones",
    3: "Instrumentación Electrónica",
    4: "Procesamiento de Señales",
    5: "Automatización y Control",
    6: "Bioingeniería",
  };
  
  const mot_ingresar_Mapping = {
    1: "Mala",
    2: "Buena",
    3: "Excelente",
  };
  
  const mot_conocimientos_Mapping = {
    1: "Muy poco",
    2: "Poco",
    3: "Regularmente",
    4: "La mayoría de las veces",
    5: "Siempre",
  };
  
  const mot_contribucion_Mapping = {
    1: "Muy poco",
    2: "Poco",
    3: "Moderado",
    4: "Alto",
    5: "Muy alto",
  };
  
  const mot_calidad_Mapping = {
    1: "Totalmente en desacuerdo",
    2: "En desacuerdo",
    3: "Ni de acuerdo ni en desacuerdo",
    4: "De acuerdo",
    5: "Totalmente de acuerdo",
  };
  
  const mot_favorecido_Mapping = {
    1: "Totalmente en desacuerdo",
    2: "En desacuerdo",
    3: "Ni de acuerdo ni en desacuerdo",
    4: "De acuerdo",
    5: "Totalmente de acuerdo",
  };
  
  const mot_post_cont_Mapping = {
    1: "Si",
    2: "No",
  };
  
  const mot_servicio_Mapping = {
    1:	"Carnetización",
    2:	"Biblioteca",
    3:	"Espacio Deportivo",
    4:	"Otros",
    5:	"Ninguno",
  }

  const mot_carnet_Mapping = {
    1:	"Si",
    2:	"No",
  }



const resultado = {

"Motivacion del pregrado": mot_pregrado_Mapping[datasMot.ID_MOT_PREGRADO] || "Valor no definido",
"Volumen de trabajo exigido": mot_volumen_Mapping[datasMot.ID_MOT_VOLUMEN] || "Valor no definido",
"Nivel de satisfacción entre las horas teóricas y prácticas": mot_nivels_Mapping[datasMot.ID_MOT_NIVELS] || "Valor no definido",
"Ambiente de aprendizaje": mot_ambiente_Mapping[datasMot.ID_MOT_AMBIENTE] || "Valor no definido",
"Se deben fortaler algunas materias?": mot_fortalecer_Mapping[datasMot.ID_MOT_FORTALECER] || "Valor no definido",
"Materias a fortalecer": datasMot.ID_MOT_MATERIAS || "Valor no definido",
"La institución le brindó servicios de apoyo": mot_apoyo_Mapping[datasMot.ID_MOT_APOYO] || "Valor no definido",
"¿Ha utilizado como egresado algún servicio de la universidad?":  mot_servicio_Mapping[datasMot.ID_MOT_SERVICIO] || "Valor no definido",
"¿Qué servicio le gustaría que ofreciera la institución como egresado?": datasMot.ID_MOT_SERVICIO_DESEADO  || "Valor no definido",
"¿Cuenta con carnet de egresado?": mot_carnet_Mapping[datasMot.ID_MOT_CARNET] || "Valor no definido",
"Los recursos de la institucion fueron adecuados": mot_recursos_Mapping[datasMot.ID_MOT_RECURSOS] || "Valor no definido",
"¿Cuál fue su modalidad de grado?": mot_modalidad_Mapping[datasMot.ID_MOT_MODALIDAD] || "Valor no definido",
"Las Prácticas te han permitido aplicar los conocimientos": mot_modalidad_p_Mapping[datasMot.ID_MOT_MODALIDAD_P] || "Valor no definido",
"El trabajo final le ha sido de utilidad para aplicar conocimientos?": mot_modalidad_t_Mapping[datasMot.ID_MOT_MODALIDAD_T] || "Valor no definido",
"Linea de profundización del trabajo final": mot_profundizacion_Mapping[datasMot.ID_MOT_PROFUNDIZACION] || "Valor no definido",
"¿Cómo evalúa las expectativas de formación profesional que tenía al ingresar?": mot_ingresar_Mapping[datasMot.ID_MOT_INGRESAR] || "Valor no definido",
"¿En que medida ha aplicado los conocimientos adquiridos de su carrera en su ocupación profesional?": mot_conocimientos_Mapping[datasMot.ID_MOT_CONOCIMIENTOS] || "Valor no definido",
"En que medida cree que ha contribuido con su trabajo al desarrollo de su comunidad, ciudad, región y/o empresa?": mot_contribucion_Mapping[datasMot.ID_MOT_CONTRIBUCION] || "Valor no definido",
"¿Usted considera que la formación recibida en el programa fue de Calidad?": mot_calidad_Mapping[datasMot.ID_MOT_CALIDAD] || "Valor no definido",
"¿El programa del cual egreso ha favorecido en su proyecto de vida?": mot_favorecido_Mapping[datasMot.ID_MOT_FAVORECIDO] || "Valor no definido",
"Daria continuidad a estudio de posgrado en la institución": mot_post_cont_Mapping[datasMot.ID_MOT_POST_CONT] || "Valor no definido",
  };
  return resultado;
}

export const changedos = (data) => {
  const resultado = {};

  for (const key in data) {
    const value = data[key];
    if (key == "datasLab") {
      resultado[key] = datasLabo(value);
    }
  }

  return resultado;
};
