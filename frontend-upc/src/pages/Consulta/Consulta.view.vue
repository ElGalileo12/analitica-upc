<script setup>
import { ref, toRaw } from "vue";
import { useConsulta } from "@/composable/useConsulta";
import { changeId } from "./validation/funtions";

const { consultaByApi, rqConsult } = useConsulta();

var identifications = ref("");
var consultValidation = ref({});

const activeButton = ref("");

async function searchConsult(idDoc) {
  await consultaByApi(idDoc);
  consultValidation.value = changeId(toRaw(rqConsult.value));
  activateButton("datasPerson");
}

const activateButton = (buttonName) => {
  if (buttonName == "datasPerson") {
    activeButton.value = "datasPerson";
  } else if (buttonName == "datasSoci") {
    activeButton.value = "datasSoci";
  } else {
    activeButton.value = "datasAcad";
  }
};
</script>

<template>
  <section class="bg-gray-50">
    <div class="h-full flex flex-col items-center justify-center">
      <h1 class="mt-10 font-bold text-xl">Consulta de estudiantes</h1>
      <form
        class="block h-48 mt-6 w-1/3 p-6 bg-white border border-gray-200 rounded-lg shadow"
      >
        <div class="relative z-0 w-full mb-6 group mt-4">
          <input
            type="number"
            name="document"
            id="document"
            class="block py-1 px-1 w-full text-lg text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=""
            v-model="identifications"
            required
          />
          <label
            for="document"
            class="peer-focus:font-medium font-bold absolute text-sm text-gray-500 duration-300 transform -translate-y-8 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
            >Documento</label
          >
        </div>
        <div class="flex justify-between mt-11">
          <button
            @click.prevent="searchConsult(identifications)"
            type="submit"
            class="w-28 text-lg text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg  py-1.5 text-center"
          >
            Buscar
          </button>
          <button
            @click.prevent="changeId"
            type="submit"
            class="text-white w-28 text-lg bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg  py-1.5 text-center"
          >
            Editar
          </button>
          <button
            type="submit"
            class="text-white text-lg w-28 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg  text-center"
          >
            Eliminar
          </button>
        </div>
      </form>
    </div>

    <div v-if="activeButton" class="flex ml-36">
      <div class="w-1/2 flex mt-6">
        <button
          @click="activateButton('datasPerson')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasPerson',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tl-lg text-sm px-5 py-2.5"
        >
          Datos personales
        </button>
        <button
          @click="activateButton('datasSoci')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasSoci',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none text-sm px-5 py-2.5"
        >
          Datos socioeconomicos
        </button>
        <button
          @click="activateButton('datasAcad')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasAcad',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tr-lg text-sm px-5 py-2.5"
        >
          Datos academicos
        </button>
      </div>
    </div>

    <div class="" v-for="(datas, key) in consultValidation" :key="key">
      <!--  Datos personales -->
      <div class="flex w-full justify-center" v-if="key === 'datasPers'">
        <div
          v-if="activeButton === 'datasPerson'"
          class="grid gap-4 mb-4 grid-cols-4 w-4/5 p-6 bg-white border border-gray-200 rounded-lg shadow"
        >
          <div v-for="(value, innerKey) in datas" :key="innerKey">
            <div>
              <label
                :for="innerKey"
                class="block mb-2 text-base font-bold text-gray-900 dark:text-white"
              >
                {{ innerKey }}</label
              >
              <input
                type="text"
                :id="value"
                :v-model="value"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                required
                :placeholder="value"
                readonly
              />
            </div>
          </div>
        </div>
      </div>
      <!--  Datos socioeconomicos -->
      <div class="flex w-full justify-center" v-else-if="key === 'datasSoci'">
        <div
          v-if="activeButton === 'datasSoci'"
          class="grid gap-4 mb-4 grid-cols-4 w-4/5 p-6 bg-white border border-gray-200 rounded-lg shadow"
        >
          <div v-for="(value, innerKey) in datas" :key="innerKey">
            <div>
              <label
                :for="innerKey"
                class="block mb-2 text-base font-bold text-gray-900 dark:text-white"
              >
                {{ innerKey }}</label
              >
              <input
                type="text"
                :id="value"
                :v-model="value"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                required
                :placeholder="value"
                readonly
              />
            </div>
          </div>
        </div>
      </div>
      <!--  Datos academicos -->
      <div class="flex w-full justify-center" v-else-if="key === 'datasAcad'">
        <div
          v-if="activeButton === 'datasAcad'"
          class="grid gap-4 mb-4 grid-cols-4 w-4/5 p-6 bg-white border border-gray-200 rounded-lg shadow"
        >
          <div v-for="(value, innerKey) in datas" :key="innerKey">
            <div>
              <label
                :for="innerKey"
                class="block mb-2 text-base font-bold text-gray-900 dark:text-white"
              >
                {{ innerKey }}</label
              >
              <input
                type="text"
                :id="value"
                :v-model="value"
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                required
                :placeholder="value"
                readonly
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>