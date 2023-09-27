<script setup>
import { ref, toRaw } from "vue";
import {EgreuseConsulta} from "@/composable/useConsulta";
import { useConsulta } from "@/composable/useConsulta";
import { changeId } from "./validation/funtions egre";
import Swal from 'sweetalert2'
import Separador from "../../components/things/separador.things.vue";
const { EgreconsultaByApi,EgredeleteByApi, rqConsult } = EgreuseConsulta();
const {  inscriptionaByApi } = useConsulta();


var identifications = ref("");
var consultValidation = ref({});
var estudiante = {
  datosEstudiante:{
      "ID_CANT_HERMANOS": 4,
      "ID_CANT_HIJOS": 0,
      "ID_DOCUMENTO": 1234567,
      "ID_DPTO_NAC": "Kevin",
      "ID_EDAD": 0,
      "ID_EDAD_MAYOR": 0,
      "ID_EDAD_MENOR": 0,
      "ID_EMAIL": "Kevin",
      "ID_EPS": 0,
      "ID_ESTADO_CIVIL": 1,
      "ID_ETNIA": 1,
      "ID_GENERO": 1,
      "ID_INTEGRANTES": 4,
      "ID_LENTES": 1,
      "ID_MAD_CAB_HOGAR": 1,
      "ID_MUN_NAC": "Kevin",
      "ID_NOMBRE": "Kevin",
      "ID_NUM_CONTACTO": "33333",
      "ID_OCUP_MADRE": 0,
      "ID_OCUP_PADRE": 0,
      "ID_POS_HERMANO": 4,
      "ID_SISBEN": "A12",
      "ID_TALENTO": 0,
      "ID_TIPO_DISC": 2,
      "ID_TIPO_DOCUMENTO": "cedulaCiudadania",
      "ID_VIC_CONFLICTO": 1},
      socioeconomica:
        {
          "ID_ESTUDIANTE": 1234567,
          "ID_OCUPACION": 2,
          "ID_ESTRATO": 1,
          "ID_TIPO_VIVIENDA": 2,
          "ID_RECIBE_INGRESOS": 2,
          "ID_ACUDIENTE": 1,
          "ID_NIVEL_ACADEMICO": 1,
          "ID_INGRESO_FAMILIAR": 200,
          "ID_TIENE_PC": 2,
          "ID_TIENE_INTERNET": 1,
          "ID_CEL_SMART": 1,
          "ID_PLAN_DATOS": 1,
          "ID_INGRESO_TRABAJA": 1
          },
          infoacademica:{
            "ID_ESTUDIANTE": 1234567,
            "ID_PROGR_ACTUAL": 1,
            "ID_HERMANOS_IES": 1,
            "ID_INGRESO_UPC": 2,
            "ID_INGRESO_OFERTA": 2,
            "ID_VALIDO_BACH": 2,
            "ID_MOTIVACION": 1,
            "ID_TIPO_COLEGIO": 1,
            "ID_SEMESTRE_INICIO": 2,
            "ID_REPITIO_ICFES": 1,
            "ID_PUNTAJE_ICFES": 1,
            "ID_PUESTO_ICFES": 1,
            "ID_LECTURA_CRITICA": 1,
            "ID_MATEMATICA": 1,
            "ID_CIUDADANOS": 1,
            "ID_CIENCIAS": 1,
            "ID_INGLES": 1,
            "ID_SEMESTRES_CURSADOS": 1,
            "ID_UBICACION_SEMESTRE": 1,
            "ID_CREDITOS_APROBADOS": 1,
            "ID_PROMEDIO_ACUMULADO": 1,
            "ID_PROMEDIO_SEMESTRE_ANT": 1,
            "ID_CREDITOS_NO_APROBADOS": 1,
            "ID_CREDITOS_MATRIC": 1,
            "ID_MATERIAS_CANCELADAS": 1,
            "ID_ASIGNATURA_ENCUESTA": 1,
            "ID_JORNADA_ACAD": 2,
            "ID_NOTA_ACTUAL": 1,
            "ID_RENDIMIENTO_ACTUAL": 2,
            "ID_NIVEL_SATISFACION_ASIG": 2
}

      


}

async function prueba(datas){
  console.log(datas);
  await inscriptionaByApi(datas);

}

const activeButton = ref("");

async function deleteConsult(idDoc){
  await EgredeleteByApi(idDoc);
}

async function searchConsult(idDoc) {
  await EgreconsultaByApi(idDoc);
  consultValidation.value = changeId(toRaw(rqConsult.value));
  activateButton("datasPerson");
}

const activateButton = (buttonName) => {
  if (buttonName == "datasPerson") {
    activeButton.value = "datasPerson";
  } else if (buttonName == "datasAcad") {
    activeButton.value = "datasAcad";
  } else if (buttonName == "datasLab") {
    activeButton.value = "datasLab";
  } else {
    activeButton.value = "datasMot";
  }
};

function confirmacion(idDoc){
  var document = idDoc;
  Swal.fire({
  title: `Estas seguro que quieres eliminar a la persona con documento ${document}`,
  text: "No podras revertir este cambio!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Si, eliminarlo!'
}).then((result) => {
  if (result.isConfirmed) {
    deleteConsult(idDoc);
    Swal.fire({
      title: 'Eliminado!',
      text: 'Tu eliminacion ha sido exitosa.',
      icon: 'success',
      confirmButtonColor: '#3085d6'
    }
    )
  }
})
}
</script>

<template>
  <section class="bg-gray-50">
    <div class="h-full flex flex-col items-center justify-center">
      <h1 class="mt-10 font-bold text-xl">Consulta de Egresados</h1>
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
            @click.prevent="prueba(estudiante)"
            type="submit"
            class="text-white w-28 text-lg bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg  py-1.5 text-center"
          >
            Editar
          </button>
          <button
            @click.prevent="confirmacion(identifications)"            
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
          @click="activateButton('datasAcad')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasAcad',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none text-sm px-5 py-2.5"
        >
          Datos academicos
        </button>
        <button
          @click="activateButton('datasLab')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasLab',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tr-lg text-sm px-5 py-2.5"
        >
          Datos Laborales
        </button>
        <button
          @click="activateButton('datasMot')"
          :class="{
            'bg-gray-900 hover:bg-gray-900 font-bold text-white':
              activeButton === 'datasMot',
          }"
          type="button"
          class="text-white w-1/3 bg-gray-600 hover:bg-gray-900 focus:outline-none rounded-tr-lg text-sm px-5 py-2.5"
        >
          Datos de motivacion
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
      <!--  Datos Laboral -->
      <div class="flex w-full justify-center" v-else-if="key === 'datasLab'">
        <div
          v-if="activeButton === 'datasLab'"
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
      <!--  Datos Motivacionales -->
      <div class="flex w-full justify-center" v-else-if="key === 'datasMot'">
        <div
          v-if="activeButton === 'datasMot'"
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
    
    <Separador></Separador>
  </section>
</template>