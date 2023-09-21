<script setup>
import { ref, reactive } from "vue";

const dataInscri = reactive({
  "¿Tiene usted alguna ocupación?": {
    options: {
                    1: 'Únicamente estudiante',
                    2: 'Empleado',
                    3: 'Independiente',
                    4: 'Trabaja medio tiempo',
                    5: 'Trabaja tiempo completo'
                },
  },
  "¿Estrato socioeconómico?":{
   options:  {
                    1: '1',
                    2: '2',
                    3: '3',
                    4: '4',
                    5: '5'
                },
  },
  "¿Tipo de vivienda?":{
   options:  {
                    1: 'Familiar',
                    2: 'Propia',
                    3: 'Arrendada',
                    4: 'Otra'
                }
  },
  "¿Recibe usted ingresos mensualmente?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "¿Alguien lo representa legalmente?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "Nivel académico":{
   options:  {
                    1: 'Bachiller',
                    2: 'Tecnico',
                    3: 'Tecnico Bachiller',
                    4: 'Tecnologo',
                    5: 'Universitario'
                }
  },
  "¿Cuánto es el ingreso familiar?": "",
  "¿Posee usted computador?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "¿Tiene acceso a Internet?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "¿Posee usted un celular inteligente?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "¿Posee usted un plan de datos?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
                }
  },
  "¿Al momento de entrar a la universidad usted trabajaba?":{
   options:  {
                    1: 'Sí',
                    2: 'No'
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


