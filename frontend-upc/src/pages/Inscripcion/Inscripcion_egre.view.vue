<script setup>
import { ref, toRaw } from "vue";
import { useEgresadoConsulta } from "@/composable/useEgresados";
import AcademicForm_egre from "../../components/forms_egre/academic_egre.form.vue";
import PersonalForm_egre from "../../components/forms_egre/personal_egre.form.vue";
import Laboral_egre from "../../components/forms_egre/Laboral_egre.form.vue";
import Moti_egre from "../../components/forms_egre/Moti_egre.form.vue";
import { changeDatas } from "./validation/funtions_egre.js";
const { EgreinscriptionaByApi } = useEgresadoConsulta();

var concatObject = ref({});
var datasPerson = ref({});
var dastasLabo = ref({});
var datasAcad = ref({});
var datasMot = ref({});

var showLaboralForm = ref(false);
var showAcademicForm = ref(false);
var showMotForm = ref(false);

async function formPersonal(datas) {
  datasPerson.value = datas.value;
  showAcademicForm.value = true;
}

async function formAcademic(datas) {
  datasAcad.value = datas.value;
  showLaboralForm.value = true;
}

async function formLab(datas) {
  dastasLabo.value = datas.value;
  showMotForm.value = true;
}

async function formMot(datas) {
  datasMot.value = datas.value;
  const resultado = ref({});
  concatObject.value = {
    datosEgresado: toRaw(datasPerson.value),
    infoacademica: toRaw(datasAcad.value),
    infolaboral: toRaw(dastasLabo.value),
    infomotivacion: toRaw(datasMot.value),
  };
  resultado.value = changeDatas(
    toRaw(concatObject.value),
    datasPerson.value.Documento
  );
  await EgreinscriptionaByApi(toRaw(resultado.value));
}
</script>

<template>
  <section>
    <div class="m-8">
      <transition name="fade" mode="out-in">
        <div
          :key="
             showLaboralForm
              ? 'economic'
              : showMotForm
              ? 'motivation'
              : showAcademicForm
              ? 'academic' 
              : 'personal'
          "
        >
          <PersonalForm_egre
            v-if="!showLaboralForm && !showAcademicForm && !showMotForm" 
            @formPersonal="formPersonal"
          />
          <AcademicForm_egre
            v-if="showAcademicForm && !showLaboralForm && !showMotForm"
            @formAcademic="formAcademic"
          />
          <Laboral_egre 
            v-if="showLaboralForm && !showMotForm"  
            @formLab="formLab" 
          />
          <Moti_egre v-if="showMotForm"  @formMot="formMot" />
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
