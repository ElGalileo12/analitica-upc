<script setup>
import { ref, onMounted, toRaw } from "vue";
import { useConsulta } from "@/composable/useConsulta";
import { changeId } from "../Consulta/validation/funtions";
import { useRoute } from "vue-router";
import PersonalForm from "../../components/forms/personal.form.vue";

const route = useRoute();

const { deleteByApi, consultaByApi, rqConsult } = useConsulta();
var consultValidation = ref({});

onMounted(async () => {
  if (route.query.id != undefined) {
    await consultaByApi(route.query.id);
    consultValidation.value = changeId(toRaw(rqConsult.value));
  }
});
</script>

<template>
  <PersonalForm :contendPersonarl="consultValidation" />
</template>
