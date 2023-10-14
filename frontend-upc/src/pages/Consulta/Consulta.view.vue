<script setup>
import { ref, toRaw } from "vue";
import { useStudent } from "@/composable/useStudent";
import { changeId } from "./validation/funtions";
import Swal from "sweetalert2";
import separadorThings from "../../components/things/separador.things.vue";

const { deleteByApi, consultaByApi, rqConsult } = useStudent();

var identifications = ref("");
var consultValidation = ref({});

const activeButton = ref("");

async function deleteConsult(idDoc) {
  await deleteByApi(idDoc);
}

async function searchConsult(idDoc) {
  try {
    await consultaByApi(idDoc);
    consultValidation.value = changeId(toRaw(rqConsult.value));
    activateButton("datasPerson");
  } catch (error) {
    if (error.response && error.response.status === 404) {
      // Aquí puedes mostrar un mensaje de error al usuario, por ejemplo:
      Swal.fire({
        icon: 'error',
        title: 'No se encontró la consulta.',
        text: 'Por favor, verifique el ID del documento.',})
    } else {
      // Otros tipos de errores, manéjalos según corresponda.
      console.error("Ocurrió un error inesperado:", error);
    }
  }
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

async function confirmacion(idDoc) {
  var document = idDoc;
  Swal.fire({
    title: `¿Estás seguro de que quieres eliminar al estudiante con documento ${document}?`,
    text: "¡No podrás revertir este cambio!",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sí, eliminarlo",
  }).then(async (result) => {
    if (result.isConfirmed) {
      try {
        // Intenta eliminar al estudiante
        await deleteConsult(idDoc);
        Swal.fire({
          title: "Eliminado",
          text: "La eliminación ha sido exitosa",
          icon: "success",
          confirmButtonColor: "#3085d6",
        });
      } catch (error) {
        if (error.response && error.response.status === 404) {
          // Muestra un mensaje de error específico para el error 404
          Swal.fire({
            icon: 'error',
            title: 'Estudiante no encontrado',
            text: 'Verifique el ID del documento.',
          });
        } else {
          // Otros tipos de errores, manéjalos según corresponda.
          console.error("Ocurrió un error inesperado:", error);
        }
      }
    }
  });
}

async function mostrarAlerta(id){
   const resultado = await Swal.fire({
        title: '¿Estás seguro de que quieres editar?',
        text: 'No podrás revertir este cambio.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, editar',
        cancelButtonText: 'Cancelar',
    });
    if (resultado.isConfirmed) {
      try {
        await consultaByApi(id);
        window.location.href = `/edition?id=${id}` 
      } catch (error) {
        if (error.response && error.response.status === 404) {
          // Muestra un mensaje de error específico para el error 404
          Swal.fire({
            icon: 'error',
            title: 'Estudiante no encontrado',
            text: 'Verifique el ID del documento.',
          });
        } else {
          // Otros tipos de errores, manéjalos según corresponda.
          console.error("Ocurrió un error inesperado:", error);
        }
      }
        // El usuario ha confirmado, redirige a la página de edición con el id         
      }

}
</script>

<template>
  <section>
    <div class="h-full flex flex-col items-center justify-center">
      <h1 class="mt-10 font-bold text-2xl">Consulta de estudiantes</h1>
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
            class="w-28 text-gray-200 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-900 font-bold rounded-lg text-lg py-1.5"
          >
            Buscar
          </button>
          <button
            @click.prevent="mostrarAlerta(identifications)"
            type="submit"
            class="w-28 text-gray-200 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-900 rounded-lg text-lg font-medium py-1.5 text-center"
            
            >
            Editar
          </button>
          <button
            @click.prevent="confirmacion(identifications)"
            type="submit"
            class="w-28 text-gray-200 bg-gray-900 hover:bg-gray-700 focus:ring-4 focus:ring-blue-900 rounded-lg text-lg font-medium py-1.5 text-center"
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
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tl-lg text-base px-5 py-2.5"
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
          class="text-white w-2/5 bg-gray-600 hover:bg-gray-900 focus:outline-none text-base px-5 py-2.5"
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
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tr-lg text-base px-5 py-2.5"
        >
          Datos académicos
        </button>
      </div>
    </div>

    <div class="" v-for="(datas, key) in consultValidation" :key="key">
      <!--  Datos personales -->
      <div class="flex w-full justify-center" v-if="key === 'datasPers'">
        <div
          v-if="activeButton === 'datasPerson'"
          class="grid gap-4 mb-4 grid-cols-4 w-5/6 p-6 bg-white border border-gray-200 rounded-lg shadow"
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
          class="grid gap-4 mb-4 grid-cols-4 w-5/6 p-6 bg-white border border-gray-200 rounded-lg shadow"
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
          class="grid gap-4 mb-4 grid-cols-4 w-5/6 p-6 bg-white border border-gray-200 rounded-lg shadow"
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
    <separadorThings></separadorThings>
  </section>
</template>
