<script setup>
import { ref, reactive, watch } from "vue";
import { useRoute } from "vue-router";
import Swal from "sweetalert2";
const route = useRoute();

const requiredFields = [
  "Documento",
  "Nombre",
  "Edad",
  "Telefono",
  "Email",
  "Estrato"
  
];

const fieldsWithOptions = [
    "Tipo de documento",
    "Genero",
    "Estado Civil",
    "¿Tiene alguna discapacidad?",
    "Etnia",
];

const dataInscri = reactive({
  "Tipo de documento": {
    options: ["Cédula", "Pasaporte","Tarjeta de identidad"],
  },
  Documento: {
    value: 0,
    type: "number",
  },
  Nombre: {
    value: 0,
    type: "text",
  },
  Telefono: {
    value: 0,
    type: "number",
  },
  Genero: {
    options: { 0: "Otro", 1: "Masculino", 2: "Femenino" },
  },
  Edad: {
    value: 0,
    type: "number",
  },
  "Estado Civil": {
    options: {
      1: "Casado",
      2: "Separado",
      3: "Soltero",
      4: "Unión libre",
      5: "Viudo",
    },
  },
  Etnia: {
    options: {
      1: "Indigena",
      2: "Palenquero",
      3: "Sin distincion racial",
      4: "Negro, mulato, afrodescendiente, afrocolombiano",
      5: "Raizal",
    },
  },
  "¿Tiene alguna discapacidad?": {
    options: {
      1: "Movilidad reducida",
      2: "Ninguna",
      3: "Auditiva",
      4: "Visual",
    },
  },
  Email: {
    value: 0,
    type: "text",
  },
  Estrato: {
    options: {
      1: "1",
      2: "2",
      3: "3",
      4: "4",
      5: "5",
      6: "6",
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

var dataTo = ref({});

//Emitir evento
const emisorOfWeek = defineEmits(["formPersonal", "formEditPersonal"]);

const sendInfoPersonal = () => {
  if (validateForm()) {
    emisorOfWeek("formPersonal", dataTo);
  }
};

//Emitir evento edit
const sendEditInfoPersonal = () => {
  if (validateForm()) {
    emisorOfWeek("formEditPersonal", dataTo);
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
  contendPersonarl: {
    type: Object,
  },
});

const onContendAcademicChange = () => {
  const Documento = route.query.id;
  dataTo.value = props.contendPersonarl.datasPers;
  dataTo.value.Documento = Documento;
};

watch(() => props.contendPersonarl, onContendAcademicChange);
</script>

<template>
  <section>
    <div class="mt-10 sm:mt-0">
      <div class="flex flex-col justify-between items-center">
        <div class="">
          <div class="px-4 sm:px-6 flex justify-center items-center flex-col">
            <h3 class="text-3xl font-bold leading-6 text-gray-900">
              Información personal
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
                <div class="grid gap-4 mb-4 grid-cols-4">
                  <div v-for="(group, groupKey) in dataInscri" :key="groupKey">
                    <label
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
                <button
                  @click.prevent="sendInfoPersonal()"
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
                  @click.prevent="sendEditInfoPersonal()"
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
