<script setup>
import { ref, onMounted, toRaw } from "vue";
import { useEgresadoConsulta } from "@/composable/useEgresados";
import { changeId } from "../Consulta/validation/funtions egre";
import { changedos } from "../Edition/validation/funtions_egre";
import { useRoute } from "vue-router";
import AcademicForm_egre from "../../components/forms_egre/academic_egre.form.vue";
import PersonalForm_egre from "../../components/forms_egre/personal_egre.form.vue";
import Laboral_egre from "../../components/forms_egre/Laboral_egre.form.vue";
import Moti_egre from "../../components/forms_egre/Moti_egre.form.vue";
import { changeDatas } from "../Inscripcion/validation/funtions_egre";

const route = useRoute();

const { EgreditionByApi, EgreconsultaByApi, rqConsult } = useEgresadoConsulta();

var concatObject = ref({});
var consultValidation = ref({});
var consultValidationAcad = ref({});
var datasPerson = ref({});
var dastasLabo = ref({});
var datasAcad = ref({});
var datasMot = ref({});

var showLaboralForm = ref(false);
var showAcademicForm = ref(false);
var showMotForm = ref(false);

async function formPersonaledit(datas) {
  datasPerson.value = datas.value;
  showAcademicForm.value = true;
}

async function formAcademicedit(datas) {
  datasAcad.value = datas.value;
  showLaboralForm.value = true;
}

async function formLabedit(datas) {
  dastasLabo.value = datas.value;
  showMotForm.value = true;
}

async function formMotedit(datas) {
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
  
  await EgreditionByApi(toRaw(resultado.value));
  console.log(await EgreditionByApi(toRaw(resultado.value)));
}

onMounted(async () => {
  if (route.query.id != undefined) {
    await EgreconsultaByApi(route.query.id);
    
    consultValidation.value = changeId(toRaw(rqConsult.value));
    console.log(consultValidationAcad.value);
  }
});
</script>

<template>
  <section>
    <div class="m-8">
          <PersonalForm_egre
            v-if="!showLaboralForm && !showAcademicForm && !showMotForm"
            :contendPersonarl="consultValidation" 
            @formEditPersonal="formPersonaledit"
          />
          <AcademicForm_egre
            v-if="showAcademicForm && !showLaboralForm && !showMotForm"
            :contendAcademic="consultValidation"
            @formEditAcademic="formAcademicedit"
          />
          <Laboral_egre 
            v-if="showLaboralForm && !showMotForm"  
            :contendLab="consultValidation"
            @formEditLab="formLabedit" 
          />
          <Moti_egre v-if="showMotForm"  
          :contendMot="consultValidation"
          @formEditMot="formMotedit" />
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
