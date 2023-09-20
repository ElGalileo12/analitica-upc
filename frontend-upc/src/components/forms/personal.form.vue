<script setup>
import { ref, reactive } from "vue";

const dataInscri = reactive({
  "Tipo de documento": {
    options: ["Cédula", "Tarjeta de identidad"],
  },
  Documento: "",
  Nombre: "",
  Edad: "",
  Telefono: "",
  Email: "",
  Genero: {
    options: ["Masculino", "Femenino"],
  },
  "Estado Cívil": {
    options: ["Casado", "Separado", "Soltero", "Unión libre", "Viudo"],
  },
  Departamento: "",
  Municipio: "",
  "¿Tiene alguna discapacidad?": {
    options: ["Movilidad reducida", "Ninguna", "Auditiva", "Visual"],
  },
  Etnia: {
    options: [
      "Indigena",
      "Palenquero",
      "Sin distincion racial",
      "Negro, mulato, afrodescendiente, afrocolombiano",
      "Raizal",
    ],
  },
  "¿Es victima del conflicto?": {
    options: ["Si", "No"],
  },
  "Edad de su hijo mayor": "",
  "Edad de su hijo menor": "",
  "Cuantos hijos tiene?": "",
  "¿Cuantos hermanos tiene?": "",
  "¿Posicion de hijo?": "",
  "Número de miembros en la familia": "",
  "Ocupacion de la madre": {
    options: {
      0: "Ninguna",
      1: "Ama de  casa",
      2: "Estudiante",
      3: "Fallecida",
      4: "Independiente",
      5: "Labora",
      6: "Madre cabeza hogar",
      7: "Pensionada",
    },
  },
  "Ocupacion del padre": {
    options: {
      0: "Ninguna",
      1: "Padre cabeza hogar",
      2: "Pensionado",
      3: "Fallecido",
      4: "Independiente",
      5: "Labora",
    },
  },
  "Nivel del sisben": "",
  "Talento": {
    options: {
      0: "Ninguna",
      1: "Actor",
      2: "Atletismo",
      3: "Bailarin",
      4: "Baloncesto",
      5: "Fútbol",
      6: "Fútbol sala",
      7: "Músico",
      8: "Natación",
      9: "Softbol",
      10: "Taewondo",
      11: "Tenis de mesa",
      12: "Voleibol",
    },
  },
  "¿Tiene EPS?": {
    options: {
      0: "Ninguna",
      1: "Sí",
      2: "No",
    },
  },
  "¿Usa lentes?": {
    options: {
      1: "Sí",
      2: "No",
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
</script>

<template>
  <section>
    <div class="mt-10 sm:mt-0">
      <div class="flex flex-col justify-between items-center">
        <div class="">
          <div class="px-4 sm:px-0 mt-10 flex justify-center items-center flex-col">
            <h3 class="text-2xl font-bold leading-6 text-gray-900">
              Información personal
            </h3>
            <p class="mt-1 text-base text-gray-600">Complete todos los datos.</p>
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
                      v-if="Object.keys(group).length < 1"
                      type="text"
                      v-model="dataTo[groupKey]"
                      name="Nombres"
                      autocomplete="given-name"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm"
                    />
                    <div class="flex" v-if="Object.keys(group).length > 0">
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
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>


