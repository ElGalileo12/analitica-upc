<script setup>
import { ref, toRaw } from "vue";
import { useConsulta } from "@/composable/useConsulta";
import AcademicForm from "../../components/forms/academic.form.vue";
import PersonalForm from "../../components/forms/personal.form.vue";
import EconomicForm from "../../components/forms/socioeco.form.vue";
import { changeDatas } from "./validation/funtions";

const { inscriptionaByApi } = useConsulta();

var concatObject = ref({});
var datasPerson = ref({});
var datasSoci = ref({});
var datasAcad = ref({});

var showEconomicForm = ref(false);
var showAcademicForm = ref(false);

async function formPersonal(datas) {
  datasPerson.value = datas.value;
  showEconomicForm.value = true;
}

async function formSocio(datas) {
  datasSoci.value = datas.value;
  showAcademicForm.value = true;
}

async function formAcademic(datas) {
  datasAcad.value = datas.value;
  const resultado = ref({});
  concatObject.value = {
    datosEstudiante: toRaw(datasPerson.value),
    socioeconomica: toRaw(datasSoci.value),
    infoacademica: toRaw(datasAcad.value),
  };
  resultado.value = changeDatas(toRaw(concatObject.value), datasPerson.value.Documento);

  await inscriptionaByApi(toRaw(resultado.value));
}
</script>

<template>
  <section>
    <div class="m-8">
      <transition name="fade" mode="out-in">
        <div :key="showEconomicForm
          ? 'economic'
          : showAcademicForm
            ? 'academic'
            : 'personal'
          ">
          <PersonalForm v-if="!showEconomicForm && !showAcademicForm" @formPersonal="formPersonal"></PersonalForm>
          <EconomicForm v-if="showEconomicForm && !showAcademicForm" @formSocio="formSocio" />
          <AcademicForm v-if="showAcademicForm" @formAcademic="formAcademic" />
        </div>
      </transition>
    </div>
  </section>
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
