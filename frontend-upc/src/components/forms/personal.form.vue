<script setup>
import { ref } from "vue";

const dataInscri = ref({
  "Tipo de documento": "",
  Documento: "",
  Nombre: "",
  Edad: "",
  Telefono: "",
});
</script>

<template>
  <section>
    <div class="mt-10 sm:mt-0">
      <div class="md:grid md:grid-cols-3 md:gap-6">
        <div class="md:col-span-1">
          <div class="px-4 sm:px-0 mt-10">
            <h3 class="text-lg teme leading-6 text-gray-900">
              Información personal
            </h3>
            <p class="mt-1 text-sm text-gray-600">Complete todos los datos.</p>
          </div>
        </div>
        <div class="mt-5 md:col-span-2 md:mt-0">
          <form>
            <div class="overflow-hidden shadow sm:rounded-md">
              <div class="bg-gray-50 px-4 py-5 sm:p-6">
                <div class="grid gap-4 mb-4 grid-cols-3">
                  <div v-for="(value, innerKey) in dataInscri" :key="innerKey">
                    <label
                      for="Nombres"
                      class="block text-sm font-medium text-gray-700"
                    >
                      {{ innerKey }}</label
                    >
                    <input
                      type="text"
                      name="Nombres"
                      autocomplete="given-name"
                      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-sky-500 focus:ring-sky-500 sm:text-sm"
                    />
                  </div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
