<script setup>
import { ref, reactive, onMounted } from "vue";
import { useRoute } from "vue-router";
import Swal from "sweetalert2";
const route = useRoute();

const requiredFields = [
  "Nombre de la empresa",
  "Ciudad donde trabaja",
  "Nombre de su empresa",
  "Ubicación de la empresa",
  "Sector de la empresa",
];

const fieldsWithOptions = [
    "¿Trabaja actualmente?",
    "Experiencia en la empresa",
    "Situación laboral actual",
    "Es su trabajo acorde a su perfil profesional",
    "Sector donde trabaja",
    "Tiempo transcurrido para la contratación en su empleo actual",
    "Nivel jerárquico en el trabajo",
    "Primer empleo",
    "Medio usado para obtener el empleo",
    "Sector en los que se ha desempeñado",
    "Sector productivo en el que ha laborado",
    "Requisitos que para su contratación",
    "Rango salarial actualmente",
    "Ha tenido reconocimiento en el trabajo",
    "¿Tiene empresa?",
    "Creó su empresa antes de graduarse?",
];

const dataInscri = reactive({
  "¿Trabaja actualmente?": {
    options: {
      1: "Si",
      2: "No",
    },
  },
  "Nombre de la empresa":{
    value: 0,
    type: "text",
  },
  "Experiencia en la empresa": {
    options: {
      1:	"de 0 a 3 años",
      2:	"de 3 a 5 años",
      3:	"más de 5 años"
    },
  },
  "Ciudad donde trabaja":{
    value: 0,
    type: "text",
  },
  "Pais donde trabaja":{
    value: 0,
    type: "text",
  },
  "Situación laboral actual": {
    options: {
      1: "Empleado",
      2: "Independiente",
    },
  },
  "Es su trabajo acorde a su perfil profesional": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "Sector donde trabaja": {
    options: {
    1: "Agropecuario",
    2: "Industrial",
    3: "Transporte",
    4: "Comercial",
    5: "Comunicaciones",
    6: "Minero y energético",
    7: "Salud",
    8: "Educación",
    },
  },
  "Tiempo transcurrido para la contratación en su empleo actual": {
    options: {
    1: "Menos de seis meses",
    2: "Entre seis meses y un año",
    3: "Más de un año",
    4: "Más de dos años",
    },
  },
  "Nivel jerárquico en el trabajo": {
    options: {
    1: "Técnico",
    2: "Supervisor",
    3: "Jefe de área",
    4: "Funcionario",
    5: "Directivo",
    6: "Empresario",
    },
  },
  "Primer empleo": {
    options:{
    1: "Antes de graduarse",
    2: "Menos de seis meses",
    3: "Entre seis meses y un año",
    4: "Más de un año",
    }
  },
  "Medio usado para obtener el empleo": {
    options: {
    1: "Bolsa de trabajo de la Universidad",
    2: "Contactos personales",
    3: "Residencia profesional",
    4: "Medios masivos de comunicación",
    5: "Concurso de merito",
    },
  },
  "Sector en los que se ha desempeñado": {
    options: {
      1: "Pública",
      2: "Privada",
    },
  },
  "Sector productivo en el que ha laborado": {
    options: {
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
    },
  },
  "Requisitos que para su contratación": {
    options: {
      1: "Competencias laborales",
      2: "Título profesional",
      3: "Examen de Selección",
      4: "Idioma extranjero",
      5: "Todas las anteriores",
      6: "Ninguno",
    },
  },
  "Rango salarial actualmente": {
    options: {
      1: "Entre 1 un SMMLV y 3 un SMMLV",
      2: "Entre 3 un SMMLV y 5 un SMMLV",
      3: "Mas de 5 SMMLV",
    },
  },
  "Ha tenido reconocimiento en el trabajo": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "¿Tiene empresa?": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "Nombre de su empresa": {
    value: 0,
    type: "text",
  },
  "Ubicación de la empresa": {
    value: 0,
    type: "text",
  },
  "Creó su empresa antes de graduarse?": {
    options: {
      1: "Sí",
      2: "No",
    },
  },
  "Sector de la empresa": {
      value: 0,
      type: "text",
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
const emisorOfWeek = defineEmits(["formLab", "formEditLab"]);

const sendInfoLab = () => {
  if (validateForm()) {
    emisorOfWeek("formLab", dataTo);
  }
};

//Emitir evento edit
const sendEditInfoLab = () => {
  if (validateForm()) {
    emisorOfWeek("formEditLab", dataTo);
  }
};
//Validation
const validateForm = () => {
  const areAllRequiredFieldsFilled = requiredFields.every((fieldName) => {
    const value = dataTo.value[fieldName];
    if (value === undefined) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: `Por favor, selecciona una opción válida para "${fieldName}".`,
      })
      return false;
    }
    return true;
  });

  if (!areAllRequiredFieldsFilled) {
    return false;
  }

  const areAllOptionsSelected = fieldsWithOptions.every((fieldName) => {
    const selectedOption = dataTo.value[fieldName];
    if (selectedOption === undefined) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: `Por favor, selecciona una opción válida para "${fieldName}".`,
      })
      return false;
    }
    return true;
  });

  if (!areAllOptionsSelected) {
    return false;
  }

  return true;
};

//Props
const props = defineProps({
  contendLab: {
    type: Object,
  },
});

const onContendPersonarlChange = () => {
  dataTo.value = props.contendLab.datasLab;
};

onMounted(() => {
  if (route.query.id) {
    onContendPersonarlChange();
  }
});
</script>

<template>
  <section>
    <div class="mt-10 sm:mt-0">
      <div class="flex flex-col justify-between items-center">
        <div class="">
          <div class="px-4 sm:px-6 flex justify-center items-center flex-col">
            <h3 class="text-3xl font-bold leading-6 text-gray-900">
              Información Laboral
            </h3>
            <p class="mt-2 text-base text-gray-600">
              Complete todos los datos.
            </p>
          </div>
        </div>
        <div class="mt-4 w-full">
          <form>
            <div class="overflow-hidden shadow sm:rounded-md">
              <div class="bg-gray-50 px-4 py-5 sm:p-6">
                <div class="grid gap-4 mb-4 grid-cols-3">
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
                        {{
                          selectedOption[groupKey] ||
                          dataTo[groupKey] ||
                          "Seleccionar"
                        }}
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
              <div
                v-if="!route.query.id"
                class="w-full flex justify-end bg-gray-50"
              >
                <!--                 <button
                  type="button"
                  class="text-white w-44 text-center mb-10 ml-20 bg-gray-800 hover:bg-gray-900 focus:outline-none focus:ring-4 focus:ring-gray-300 font-medium rounded-lg text-base py-2.5"
                >
                  Atrás
                </button> -->
                <button
                  @click.prevent="sendInfoLab()"
                  type="button"
                  class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5"
                >
                  Siguiente
                </button>
              </div>

              <div
                v-if="route.query.id"
                class="w-full flex justify-end bg-gray-50"
              >
                <button
                  @click.prevent="sendEditInfoLab()"
                  type="button"
                  class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5"
                >
                  Siguiente
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
