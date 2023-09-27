<script setup>
import { ref, reactive } from "vue";

const requiredFields = [
  "¿Tiene hermanos estudiando actualmente en alguna IES?",
  /*   "PUNTAJE de las pruebas saber 11° ICFES",
  "PERCENTIL de las pruebas saber 11° ICFES",
  "Puntaje de lectura critica",
  "Puntaje de matematicas",
  "Puntaje de sociales y ciudadanas",
  "Puntaje de ciencias naturales",
  "Puntaje de ingles",
  "¿Cuántos semestres ha cursado usted actualmente?",
  "Su ubicación semestral según el vortal",
  "Créditos aprobados hasta el 2023-1",
  "¿Cual es su promedio acumulado actual?",
  "¿Cual es su promedio del semestre anterior?",
  "Cuantos créditos no aprobados?",
  "Créditos matriculados este semestre 2023-1",
  "¿Ha cancelado alguna asignatura este semestre 2023-1?",
  "Su nota obtenida actualmente en la asignatura donde esta siendo encuestado", */
];

const fieldsWithOptions = [
  "Seleccione la carrera universitaria que está estudiando actualmente",
  /*   "Usted ingresó a la Universidad Popular del Cesar por medio de según su oferta acamédica",
  "Ingresó a la universidad por (Mejor bachiller, preuniversitario o deportista)",
  "Qué tan motivado te sentías al momento de ingresar a estudiar su carrera profesional",
  "Validó el bachillerato",
  "Tipo de colegio en el que estudio",
  "En qué semestre iniciaste tu carrera profesional en la Universidad Popular del Cesar",
  "Repitió usted las pruebas saber 11° ICFES",
  "Desde que asignatura esta haciendo la encuesta",
  "Jornada académica",
  "Actual rendimiento académico en la asignatura",
  "Nivel de satisfacción con la asignatura", */
];

const dataInscri = reactive({
  "Seleccione la carrera universitaria que está estudiando actualmente": {
    options: {
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
    },
  },
  "¿Tiene hermanos estudiando actualmente en alguna IES?": {
    value: 0,
    type: "number",
  },

  "Usted ingresó a la Universidad Popular del Cesar por medio de según su oferta acamédica":
    {
      options: {
        1: "Preuniversitario",
        2: "Aspirante regular",
        3: "Perteneciente a cabildo indigena",
        4: "Reintegro",
        5: "ReservaCupo",
        6: "TransExterna",
        7: "TransInterna",
        8: "Otro",
        9: "Deportista destacado",
      },
    },
  "Ingresó a la universidad por (Mejor bachiller, preuniversitario o deportista)":
    {
      options: {
        1: "Sí",
        2: "No",
      },
    },
  "Qué tan motivado te sentías al momento de ingresar a estudiar su carrera profesional":
    {
      options: {
        1: "Bajo",
        2: "Medio",
        3: "Alto",
        4: "Excelente",
      },
    },
  "Validó el bachillerato": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "Tipo de colegio en el que estudio": {
    options: {
      1: "Privado",
      2: "Público",
    },
  },
  "En qué semestre iniciaste tu carrera profesional en la Universidad Popular del Cesar":
    {
      options: {
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
      },
    },
  "Repitió usted las pruebas saber 11° ICFES": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "PUNTAJE de las pruebas saber 11° ICFES": {
    value: 0,
    type: "number",
  },
  "PERCENTIL de las pruebas saber 11° ICFES": {
    value: 0,
    type: "number",
  },
  "Puntaje de lectura critica": {
    value: 0,
    type: "number",
  },
  "Puntaje de matematicas": {
    value: 0,
    type: "number",
  },
  "Puntaje de sociales y ciudadanas": {
    value: 0,
    type: "number",
  },
  "Puntaje de ciencias naturales": {
    value: 0,
    type: "number",
  },
  "Puntaje de ingles": {
    value: 0,
    type: "number",
  },
  "¿Cuántos semestres ha cursado usted actualmente?": {
    value: 0,
    type: "number",
  },
  "Su ubicación semestral según el vortal": {
    value: 0,
    type: "number",
  },
  "Créditos aprobados hasta el 2023-1": {
    value: 0,
    type: "number",
  },
  "¿Cual es su promedio acumulado actual?": {
    value: 0,
    type: "number",
  },
  "¿Cual es su promedio del semestre anterior?": {
    value: 0,
    type: "number",
  },
  "Cuantos créditos no aprobados?": {
    value: 0,
    type: "number",
  },
  "Créditos matriculados este semestre 2023-1": {
    value: 0,
    type: "number",
  },
  "¿Ha cancelado alguna asignatura este semestre 2023-1?": {
    value: 0,
    type: "number",
  },
  "Desde que asignatura esta haciendo la encuesta": {
    options: {
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
    },
  },
  "Jornada académica": {
    options: {
      1: "Diurno",
      2: "Nocturno",
    },
  },
  "Su nota obtenida actualmente en la asignatura donde esta siendo encuestado":
    {
      value: 0,
      type: "number",
    },
  "Actual rendimiento académico en la asignatura": {
    options: {
      1: "Bajo",
      2: "Medio",
      3: "Alto",
      4: "Excelente",
    },
  },
  "Nivel de satisfacción con la asignatura": {
    options: {
      1: "Bajo",
      2: "Medio",
      3: "Alto",
      4: "Excelente",
    },
  },
});

const selectedOption = reactive({});

const toggleDropdown = (groupKey) => {
  dataInscri[groupKey].isOpen = !dataInscri[groupKey].isOpen;
};

const selectOption = (groupKey, option) => {
  selectedOption[groupKey] = option;
  dataInscri[groupKey].isOpen = false;
  setDataTo(groupKey, option);
};

const setDataTo = (key, value) => {
  dataTo.value[key] = value;
};

const dataTo = ref({});
//Prosps
const emisorOfWeek = defineEmits(["formAcademic"]);

const sendInfoAcademic = () => {
  if (validateForm()) {
    emisorOfWeek("formAcademic", dataTo);
  }
};

//Validation
const validateForm = () => {
  const areAllRequiredFieldsFilled = requiredFields.every((fieldName) => {
    const value = dataTo.value[fieldName];
    return value !== null && value !== undefined && value !== "";
  });

  if (!areAllRequiredFieldsFilled) {
    alert(
      "Por favor, completa todos los campos obligatorios antes de continuar."
    );
    return false;
  }

  const areAllOptionsSelected = fieldsWithOptions.every((fieldName) => {
    const selectedOption = dataTo.value[fieldName];
    if (selectedOption === undefined) {
      alert(`Por favor, selecciona una opción válida para "${fieldName}".`);
      return false;
    }
    return true;
  });

  if (!areAllOptionsSelected) {
    return false;
  }

  return true;
};
</script>

<template>
  <section>
    <div class="mt-10 sm:mt-0">
      <div class="flex flex-col justify-between items-center">
        <div class="">
          <div
            class="px-4 sm:px-0 mt-10 flex justify-center items-center flex-col"
          >
            <h3 class="text-2xl font-bold leading-6 text-gray-900">
              Información Academica
            </h3>
            <p class="mt-1 text-base text-gray-600">
              Complete todos los datos.
            </p>
          </div>
        </div>
        <div class="mt-5 w-full">
          <form>
            <div class="overflow-hidden shadow sm:rounded-md">
              <div class="bg-gray-50 px-4 py-5 sm:p-6">
                <div class="grid gap-4 mb-4 grid-cols-4">
                  <div v-for="(group, groupKey) in dataInscri" :key="groupKey">
                    <label
                      for="Nombres"
                      class="block mb-2 text-base font-bold text-gray-900 dark:text-white"
                    >
                      {{ groupKey }}
                    </label>
                    <input
                      v-if="group.value === 0"
                      :type="group.type"
                      required
                      v-model="dataTo[groupKey]"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm"
                    />
                    <div class="flex" v-if="group.value != 0">
                      <button
                        id="dropdownDefaultButton"
                        @click="toggleDropdown(groupKey)"
                        class="w-full border border-gray-300 bg-white shadow-sm text-whit focus:outline-none focus:ring-blue-300 font-medium rounded-md mt-1 text-sm px-5 py-2 justify-between inline-flex items-center"
                        type="button"
                      >
                        {{ selectedOption[groupKey] || "Seleccionar" }}
                        <svg
                          class="w-2.5 h-2.5 ml-2.5"
                          aria-hidden="true"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 10 6"
                        >
                          <path
                            stroke="currentColor"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="m1 1 4 4 4-4"
                          />
                        </svg>
                      </button>
                      <!-- Dropdown menu -->
                      <div
                        id="dropdown"
                        :class="{ hidden: !group.isOpen }"
                        class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-52 absolute mt-11"
                      >
                        <ul
                          class="py-2 text-sm text-gray-700 dark:text-gray-200"
                          aria-labelledby="dropdownDefaultButton"
                        >
                          <li v-for="(data, id) in group.options" :key="id">
                            <h3
                              class="block px-4 py-2 hover:bg-gray-100 text-center"
                              @click="selectOption(groupKey, data)"
                            >
                              {{ data }}
                            </h3>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full flex justify-end bg-gray-50">
                <button
                  @click.prevent="sendInfoAcademic()"
                  type="button"
                  class="text-white mb-10 mr-20 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5"
                >
                  Enviar
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
