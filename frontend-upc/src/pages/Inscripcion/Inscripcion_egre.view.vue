<script setup>
import { ref, toRaw } from "vue";
import { useStudent } from "@/composable/useStudent";
import AcademicForm_egre from "../../components/forms_egre/academic_egre.form.vue";
import PersonalForm_egre from "../../components/forms_egre/personal_egre.form.vue";
import EconomicForm from "../../components/forms/socioeco.form.vue";
import { changeDatas } from "./validation/funtions";

const { inscriptionaByApi } = useStudent();

var concatObject = ref({});
var datasPerson = ref({});
var datasSoci = ref({});
var datasAcad = ref({});

var showEconomicForm = ref(false);
var showAcademicForm = ref(false);

async function formPersonal(datas) {
  datasPerson.value = datas.value;
  showAcademicForm.value = true;
}

async function formAcademic(datas) {
  datasAcad.value = datas.value;
  showEconomicForm.value = true;
}

async function formSocio(datas) {
  datasSoci.value = datas.value;
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
  await inscriptionaByApi(toRaw(resultado.value));
}
</script>

<template>
  <section>
    <div class="m-8">
      <transition name="fade" mode="out-in">
        <div
          :key="
            showAcademicForm
              ? 'academic'
              : showEconomicForm
              ? 'economic'
              : 'personal'
          "
        >
          <PersonalForm_egre
            v-if="!showEconomicForm && !showAcademicForm"
            @formPersonal="formPersonal"
          />
          <AcademicForm_egre
            v-if="!showEconomicForm && showAcademicForm"
            @formAcademic="formAcademic"
          />
          <EconomicForm v-if="showEconomicForm"  @formSocio="formSocio" />
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
