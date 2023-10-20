<script setup>
import { ref, onMounted, toRaw } from "vue";
import { useStudent } from "@/composable/useStudent";
import { changeId } from "../Consulta/validation/funtions.js";
import { changeAcad } from "../Edition/validation/funtions";
import { useRoute } from "vue-router";
import PersonalForm from "../../components/forms/personal.form.vue";
import EconomicForm from "../../components/forms/socioeco.form.vue";
import AcademicForm from "../../components/forms/academic.form.vue";
import { changeDatas } from "../Inscripcion/validation/funtions";

const route = useRoute();

const { editionByApi, consultaByApi, rqConsult } = useStudent();

var concatObject = ref({});
var consultValidation = ref({});
var consultValidationAcad = ref({});
var datasPerson = ref({});
var datasSoci = ref({});
var datasAcad = ref({});

var showEconomicForm = ref(false);
var showAcademicForm = ref(false);

async function formEditPersonal(datas) {
  datasPerson.value = datas.value;
  showEconomicForm.value = true;
}

async function formEditSoci(datas) {
  datasSoci.value = datas.value;
  showAcademicForm.value = true;
}

async function formEditAcad(datas) {
  datasAcad.value = datas.value;
  const resultado = ref({});
  concatObject.value = {
    datosEstudiante: toRaw(datasPerson.value),
    socioeconomica: toRaw(datasSoci.value),
    infoacademica: toRaw(datasAcad.value),
  };

  resultado.value = changeDatas(
    toRaw(concatObject.value),
    datasPerson.value.Documento
  );

  await editionByApi(toRaw(resultado.value));
}

onMounted(async () => {
  if (route.query.id != undefined) {
    await consultaByApi(route.query.id);
    consultValidation.value = changeId(toRaw(rqConsult.value));
    consultValidationAcad.value = changeAcad(toRaw(rqConsult.value));
  }
});
</script>

<template>
  <div class="m-8">
    <transition name="fade" mode="out-in">
      <div
        :key="
          showEconomicForm
            ? 'economic'
            : showAcademicForm
            ? 'academic'
            : 'personal'
        "
      >
        <PersonalForm
          v-if="!showEconomicForm && !showAcademicForm"
          :contendPersonarl="consultValidation"
          @formEditPersonal="formEditPersonal"
        />
        <EconomicForm
          v-if="showEconomicForm && !showAcademicForm"
          :contendEconomic="consultValidation"
          @formEditSoci="formEditSoci"
        />
        <AcademicForm
          v-if="showAcademicForm"
          :contendAcademic="consultValidationAcad"
          @formEditAcad="formEditAcad"
        />
      </div>
    </transition>
  </div>
</template>


<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
