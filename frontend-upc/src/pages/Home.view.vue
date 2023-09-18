<script setup>
import { defineComponent } from "vue";
import PersonalForm from "../components/forms/personal.form.vue";
import Separador from "../components/things/separador.things.vue";

defineComponent({
  components: {
    PersonalForm,
    Separador,
  },
});
</script>

<template>
  <div class="m-8">
    <PersonalForm></PersonalForm>
    <Separador></Separador>
  </div>
</template>

<style></style>