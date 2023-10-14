<script setup>
import { ref, reactive, onMounted } from "vue";
import { useRoute } from "vue-router";
import Swal from "sweetalert2";
const route = useRoute();

const requiredFields = [
  "Materias a fortalecer",
  "¿Qué servicio le gustaría que ofreciera la institución como egresado?"
];

const fieldsWithOptions = [
    "Motivacion del pregrado",
    "Volumen de trabajo exigido",
    "Nivel de satisfacción entre las horas teóricas y prácticas",
    "Ambiente de aprendizaje",
    "Se deben fortalecer algunas materias?",
    "La institución le brindó servicios de apoyo",
    "¿Ha utilizado como egresado algún servicio de la universidad?",
    "¿Cuenta con carnet de egresado?",
    "Los recursos de la institución fueron adecuados",
    "¿Cuál fue su modalidad de grado?",
    "Las Prácticas te han permitido aplicar los conocimientos",
    "El trabajo final le ha sido de utilidad para aplicar conocimientos?",
    "Linea de profundización del trabajo final",
    "¿Cómo evalúa las expectativas de formación profesional que tenía al ingresar?",
    "¿En qué medida ha aplicado los conocimientos adquiridos de su carrera en su ocupación profesional?",
    "En qué medida cree que ha contribuido con su trabajo al desarrollo de su comunidad, ciudad, región y/o empresa?",
    "¿Usted considera que la formación recibida en el programa fue de Calidad?",
    "¿El programa del cual egresó ha favorecido en su proyecto de vida?",
    "Daría continuidad a estudio de posgrado en la institución"
];

const dataInscri = reactive({
  "Motivacion del pregrado": {
    options:{
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Excelente",
    }
  },
  "Volumen de trabajo exigido": {
    options:{
      1: "Muy bajo",
      2: "Poco",
      3: "Regular",
      4: "Exigente",
      5: "Muy exigente",
    }
  },
  "Nivel de satisfacción entre las horas teóricas y prácticas": {
    options:{
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Muy alto",
    }
  },
  "Ambiente de aprendizaje": {
    options:{
    1: "Muy bajo",
    2: "Bajo",
    3: "Bueno",
    4: "Alto",
    5: "Muy alto",
    }
  },
  "Se deben fortalecer algunas materias?": {
    options:{
      1: "Si",
      2: "No",
    }
  },

  "Materias a fortalecer": {
    value: 0,
    type: "text",
  },
  "La institución le brindó servicios de apoyo": {
    options:{
      1: "Si",
      2: "No",
    }
  },
  "¿Ha utilizado como egresado algún servicio de la universidad?": {
    options:{
      1:	"Carnetización",
      2:	"Biblioteca",
      3:	"Espacio Deportivo",
      4:	"Otros",
      5:	"Ninguno",
    }
  },
  "¿Qué servicio le gustaría que ofreciera la institución como egresado?": {
    value: 0,
    type: "text",
  },
  "¿Cuenta con carnet de egresado?": {
    options:{
      1: "Si",
      2: "No",
    }
  },
  "Los recursos de la institución fueron adecuados": {
    options:{
      1: "Muy poco adecuados",
      2: "Adecuados",
      3: "Muy adecuados",
    }
  },
  "¿Cuál fue su modalidad de grado?": {
    options:{
      1: "Prácticas",
      2: "Trabajo final de carrera",
    }
  },
  "Las Prácticas te han permitido aplicar los conocimientos": {
    options:{
      1: "Muy poco",
      2: "Poco",
      3: "Moderado",
      4: "Alto",
      5: "Muy alto",
    }
  },
  "El trabajo final le ha sido de utilidad para aplicar conocimientos?": {
    options:{
      1: "Muy poco",
      2: "Poco",
      3: "Moderado",
      4: "Alto",
      5: "Muy alto",
    }
  },
  "Linea de profundización del trabajo final": {
    options:{
      1: "Optoelectrónica",
      2: "Telecomunicaciones",
      3: "Instrumentación Electrónica",
      4: "Procesamiento de Señales",
      5: "Automatización y Control",
      6: "Bioingeniería",
    }
  },
  "¿Cómo evalúa las expectativas de formación profesional que tenía al ingresar?": {
    options:{
      1: "Mala",
      2: "Buena",
      3: "Excelente",
    }
  },
  "¿En qué medida ha aplicado los conocimientos adquiridos de su carrera en su ocupación profesional?": {
    options:{
      1: "Muy poco",
      2: "Poco",
      3: "Regularmente",
      4: "La mayoría de las veces",
      5: "Siempre",
    }
  },
  "En qué medida cree que ha contribuido con su trabajo al desarrollo de su comunidad, ciudad, región y/o empresa?": {
    options:{
      1: "Muy poco",
      2: "Poco",
      3: "Moderado",
      4: "Alto",
      5: "Muy alto",
    }
  },
  "¿Usted considera que la formación recibida en el programa fue de Calidad?": {
    options:{
      1: "Totalmente en desacuerdo",
      2: "En desacuerdo",
      3: "Ni de acuerdo ni en desacuerdo",
      4: "De acuerdo",
      5: "Totalmente de acuerdo",
    }
  },
  "¿El programa del cual egresó ha favorecido en su proyecto de vida?": {
    options:{
      1: "Totalmente en desacuerdo",
      2: "En desacuerdo",
      3: "Ni de acuerdo ni en desacuerdo",
      4: "De acuerdo",
      5: "Totalmente de acuerdo",
    }
  },
  "Daría continuidad a estudio de posgrado en la institución": {
    options:{
      1: "Si",
      2: "No",
    }
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
const emisorOfWeek = defineEmits(["formMot", "formEditMot"]);

const sendInfoMot = () => {
  if (validateForm()) {
    emisorOfWeek("formMot", dataTo);
    Swal.fire({
      icon: 'success',
      title: 'El registro ha sido Exitoso',
      showConfirmButton: false,
      timer: 1500
    })

     setTimeout(function() { location.reload();}, 1500);
  }
  
};
//Emitir evento edit
const sendEditMot = () => {
  if (validateForm()) {
    emisorOfWeek("formEditMot", dataTo);
    Swal.fire({
      icon: 'success',
      title: 'Se han modificado los datos correctamente',
      showConfirmButton: false,
      timer: 1500
    })
    setTimeout(function() { window.location.href = '/consulta_egresados'; }, 1500);
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
  contendMot: {
    type: Object,
  },
});

const onContendMotChange = () => {
  dataTo.value = props.contendMot.datasMot;
};

onMounted(() => {
  if (route.query.id) {
    onContendMotChange();
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
              Información Motivacional
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
                <div class="grid gap-6 mb-4 grid-cols-3">
                  <div v-for="(group, groupKey) in dataInscri" :key="groupKey">
                    <label
                      for="Nombres"
                      class="block mb-2 text-base font-bold text-gray-900 dark:text-white px-2"
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
                        class="w-full border border-gray-300 bg-white shadow-sm text-whit focus:outline-none focus:ring-blue-300 font-medium rounded-md mt-0 text-sm px-5 py-2 justify-between inline-flex items-center"
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
                <button
                  @click.prevent="sendInfoMot()"
                  type="button"
                  class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5"
                >
                  Enviar
                </button>
              </div>
              <div
                v-if="route.query.id"
                class="w-full flex justify-end bg-gray-50"
              >
                <button
                  @click.prevent="sendEditMot()"
                  type="button"
                  class="text-gray-200 mb-10 mr-20 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-300 font-bold rounded-lg text-base px-5 py-2.5"
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
