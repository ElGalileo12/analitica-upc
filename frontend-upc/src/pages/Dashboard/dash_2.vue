<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart, BarChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
} from "echarts/components";
import VChart from "vue-echarts";
import { getOptionChart } from "./config/option.js";
import { config_2_1, getOptionChart_2_1 } from "./config_2/option_2_1.js";
import { config_2_2, getOptionChart_2_2 } from "./config_2/option_2_2.js";
import { config_2_3, getOptionChart_2_3 } from "./config_2/option_2_3.js";
import { config_2_4, getOptionChart_2_4 } from "./config_2/option_2_4.js";
import { config_2_5, getOptionChart_2_5 } from "./config_2/option_2_5.js";
import { ref, onMounted } from "vue";
use([
  CanvasRenderer,
  PieChart,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
]);
// Obtener los datos de total
let total = ref();
const fetchTotal = async () => {
  const data = await getOptionChart();
  total.value = data.t;
};
onMounted(() => {
  fetchTotal(); // Llama a la función cuando el componente se monta
});
// Obtener los datos de getOptionChart_2_1
let chartData_2_1 = null;
getOptionChart_2_1().then((data) => {
  chartData_2_1 = data;
  // Actualizar los valores en la opción del gráfico
  option_2_1.value.series[0].data = [
    { itemStyle: { color: "#16a34a" }, value: chartData_2_1.a },
    { itemStyle: { color: "#facc15" }, value: chartData_2_1.b },
    { itemStyle: { color: "#9333ea" }, value: chartData_2_1.c },
    { itemStyle: { color: "#0284c7" }, value: chartData_2_1.d },
    { itemStyle: { color: "#16a34a" }, value: chartData_2_1.e },
  ];
});

// Obtener los datos de getOptionChart_2
let chartData_2_2 = null;
getOptionChart_2_2().then((data) => {
  chartData_2_2 = data;
  // Actualizar los valores en la opción del gráfico
  option_2_2.value.series[0].data = [
    { itemStyle: { color: "#16a34a" }, value: chartData_2_2.a },
    { itemStyle: { color: "#facc15" }, value: chartData_2_2.b },
    { itemStyle: { color: "#9333ea" }, value: chartData_2_2.c },
    { itemStyle: { color: "#0284c7" }, value: chartData_2_2.d },
  ];
});
// Obtener los datos de getOptionChart_3
let chartData_2_3 = null;
getOptionChart_2_3().then((data) => {
  chartData_2_3 = data;
  // Actualizar los valores en la opción del gráfico
  option_2_3.value.series[0].data = [
    {
      value: chartData_2_3.a,
      name: "Estudiante",
    },
    {
      value: chartData_2_3.b,
      name: "Empleado",
    },
    {
      value: chartData_2_3.c,
      name: "Independiente",
    },
  ];
});
// Obtener los datos de getOptionChart_4
let chartData_2_4 = null;
getOptionChart_2_4().then((data) => {
  chartData_2_4 = data;
  // Actualizar los valores en la opción del gráfico
  option_2_4.value.series[0].data = [
    {
      value: chartData_2_4.a,
      name: "Familiar",
    },
    {
      value: chartData_2_4.b,
      name: "Propia",
    },
    {
      value: chartData_2_4.c,
      name: "Arrendada",
    },
    {
      value: chartData_2_4.d,
      name: "Otra",
    },
  ];
});
// Obtener los datos de getOptionChart_5
let chartData_2_5 = null;
getOptionChart_2_5().then((data) => {
  chartData_2_5 = data;
  // Actualizar los valores en la opción del gráfico
  option_2_5.value.series[0].data = [
    { value: chartData_2_5.yp },
    { value: chartData_2_5.yi },
    { value: chartData_2_5.yc },
    { value: chartData_2_5.ypd },
  ];
  option_2_5.value.series[1].data = [
    { value: chartData_2_5.np },
    { value: chartData_2_5.ni },
    { value: chartData_2_5.nc },
    { value: chartData_2_5.npd },
  ];
});

// Configuracion para las graficas
//Grafica 1
const option_2_1 = config_2_1;
//Grafica 3
const option_2_2 = config_2_2;
//Grafica 3
const option_2_3 = config_2_3;
//Grafica 4
const option_2_4 = config_2_4;
//Grafica 5
const option_2_5 = config_2_5;
//
</script>
<template>
  <section>
    <div class="p-4">
      <!-- Primera Fila-->
      <div class="flex justify-around">
        <div class="rounded-square bg-white p-4 flex flex-col items-center">
          <p class="text-center text-xl font-bold text-black mt-10">
            Estudiantes encuestados
          </p>
          <p class="text-7xl text-green-600 text-center mt-8">{{ total }}</p>
        </div>
        <div class="square2">
          <v-chart class="chart_2" :option="option_2_1" />
        </div>
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option_2_3" />
        </div>
      </div>
      <!-- Segunda Fila-->
      <div class="flex justify-around mt-4">
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option_2_4" />
        </div>
        <div class="square2">
          <v-chart class="chart" :option="option_2_2" />
        </div>
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option_2_5" />
        </div>
      </div>
      <!-- Tercera Fila-->
    </div>
  </section>
</template>

<style scoped>
.chart {
  top: 25px;
  width: 100%;
  min-height: 250px;
}

.chart2 {
  top: 0%;
  min-width: 300px;
  height: 300px;
  left: 00px;
}
section {
  background-color: rgb(231, 231, 231);
  /*background: url(../../assets/cool-background-g2.svg) center no-repeat;*/
  background-attachment: fixed;
  background-size: cover;
}

.rounded-square {
  width: 360px;
  height: 280px;
  background-color: #ffffff;
  border-radius: 50px;
  position: relative;
  overflow: hidden;
}
.square2 {
  width: 500px;
  height: 280px;
  background-color: #ffffff;
  border-radius: 50px;
  position: relative;
  overflow: hidden;
}
.text-1 {
  font-size: 75px; /* Cambiar el tamaño de la fuente */
  font-family: Arial, Helvetica, sans-serif; /* Cambiar la fuente */
  font: bold;
  margin: 0;
  margin-top: 60px;
}
.text-2 {
  color: #999;
  font-family: Arial, Helvetica, sans-serif; /* Cambiar la fuente */
}

.text-1 + .text-2 {
  margin-top: -25px;
}
</style>
