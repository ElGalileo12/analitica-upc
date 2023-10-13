<script setup>
const datasCards = {
  1: {
    title: "Excelencia Educativa",
    Description: "Aspiramos a la continua mejora de la calidad educativa.",
  },
  2: {
    title: "Accesibilidad y Usabilidad",
    Description:
      "Nuestra interfaz se distingue por su usabilidad y accesibilidad.",
  },
  3: {
    title: "Análisis de Datos Avanzados",
    Description: "Utilizamos técnicas estadísticas y algoritmos sofisticados.",
  },
  4: {
    title: "Enfoque Basado en Datos",
    Description: "Tomamos decisiones informadas mediante análisis detallados.",
  },
  5: {
    title: "Enfoque Multidimensional",
    Description: "Analizamos factores diversos que afectan la deserción.",
  },
  6: {
    title: "Retención Estudiantil",
    Description:
      "Fomenta el incremento de la retención y el rendimiento académico de los estudiantes.",
  },
};
</script>

<template>
  <section class="grid gap-4 grid-cols-3 mt-10 px-10">
    <div
      class="teme block max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100"
      v-for="data in datasCards"
      :key="data"
    >
      <h2
        class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-center"
      >
        {{ data.title }}
      </h2>
      <p class="font-normal text-gray-700 dark:text-gray-400">
        {{ data.Description }}
      </p>
    </div>
  </section>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap");

.teme {
  font-family: "Roboto", sans-serif;
}

.temeTwo {
  font-family: "Roboto", sans-serif;
  font-weight: 400;
}
</style>