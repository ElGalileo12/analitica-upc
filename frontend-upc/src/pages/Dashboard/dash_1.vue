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
import { config, getOptionChart } from "./config/option.js";
import { config_2, getOptionChart_2 } from "./config/option_2.js";
import { config_3, getOptionChart_3 } from "./config/option_3.js";
import { config_4, getOptionChart_4 } from "./config/option_4.js";
import { config_5, getOptionChart_5 } from "./config/option_5.js";
import { config_6, getOptionChart_6 } from "./config/option_6.js";
import { config_7, getOptionChart_7 } from "./config/option_7.js";
import { ref, onMounted  } from "vue";
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
        total.value= data.t;
};
onMounted(() => {
      fetchTotal(); // Llama a la función cuando el componente se monta
    });

// Obtener los datos de getOptionChart
let chartData = null;
getOptionChart().then((data) => {
  chartData = data;
  // Actualizar los valores en la opción del gráfico
  option.value.series[0].data = [
    {
      itemStyle: { color: "rgb(101, 197, 189)" },
      value: chartData.a,
      name: "Mujeres",
    },
    {
      itemStyle: { color: "rgb(147,112,219)" },
      value: chartData.b,
      name: "Hombres",
    },
    {
      itemStyle: { color: "rgba(255, 251, 13, 1)" },
      value: chartData.c,
      name: "Otro Genero",
    },
  ];
});

// Obtener los datos de getOptionChart_2
let chartData_2 = null;
getOptionChart_2().then((data) => {
  chartData_2 = data;
  // Actualizar los valores en la opción del gráfico
  option_2.value.series[0].data = [
    { itemStyle: { color: "rgb(101, 197, 189)" }, value: chartData_2.a },
    { itemStyle: { color: "rgb(147,112,219)" }, value: chartData_2.b },
  ];
});
// Obtener los datos de getOptionChart_3
let chartData_3 = null;
getOptionChart_3().then((data) => {
  chartData_3 = data;
  // Actualizar los valores en la opción del gráfico
  option_3.value.series[0].data = [
    {
      itemStyle: { color: "rgb(101, 197, 189)" },
      value: chartData_3.a,
      name: "Mujeres",
    },
    {
      itemStyle: { color: "rgb(147,112,219)" },
      value: chartData_3.b,
      name: "Hombres",
    },
  ];
});
// Obtener los datos de getOptionChart_4
let chartData_4 = null;
getOptionChart_4().then((data) => {
  chartData_4 = data;
  // Actualizar los valores en la opción del gráfico
  option_4.value.series[0].data = [
    {
      itemStyle: { color: "rgb(101, 197, 189)" },
      value: chartData_4.a,
      name: "Mujeres",
    },
    {
      itemStyle: { color: "rgb(147,112,219)" },
      value: chartData_4.b,
      name: "Hombres",
    },
    {
      itemStyle: { color: "rgb(255, 251, 13, 1)" },
      value: chartData_4.c,
      name: "Otros",
    },
  ];
});
// Obtener los datos de getOptionChart_5
let chartData_5 = null;
getOptionChart_5().then((data) => {
  chartData_5 = data;
  // Actualizar los valores en la opción del gráfico
  option_5.value.series[0].data = [
    { value: chartData_5.a1 },
    { value: chartData_5.b1 },
    { value: chartData_5.c1 },
    { value: chartData_5.d1 },
  ];
  option_5.value.series[1].data = [
    { value: chartData_5.a2 },
    { value: chartData_5.b2 },
    { value: chartData_5.c2 },
    { value: chartData_5.d2 },
  ];
  option_5.value.series[2].data = [{}, {}, { value: chartData_5.c3 }, {}];
});
// Obtener los datos de getOptionChart_6
let chartData_6 = null;
getOptionChart_6().then((data) => {
  chartData_6 = data;
     // Actualizar los valores en la opción del gráfico
  option_6.value.series[0].data = [
    { value: chartData_6.ym },
    { value: chartData_6.nm },
  ];
  option_6.value.series[1].data = [
    { value: chartData_6.yf },
    { value: chartData_6.nf },
  ];
  option_6.value.series[2].data = [  
    { value: chartData_6.yo },
    { value: chartData_6.no },
  ];
});
// Obtener los datos de getOptionChart_7
let chartData_7 = null;
getOptionChart_7().then((data) => {
  chartData_7 = data;
     // Actualizar los valores en la opción del gráfico
  option_7.value.series[0].data = [
    { value: chartData_7.ym },
    { value: chartData_7.nm },
  ];
  option_7.value.series[1].data = [
    { value: chartData_7.yf },
    { value: chartData_7.nf },
  ];
  option_7.value.series[2].data = [  
    { value: chartData_7.yo },
    { value: chartData_7.no },
  ];
});

// Configuracion para las graficas
//Grafica 1
const option = config;
//Grafica 3
const option_2 = config_2;
//Grafica 3
const option_3 = config_3;
//Grafica 4
const option_4 = config_4;
//Grafica 5
const option_5 = config_5;
//Grafica 6
const option_6 = config_6;
//Grafica 7
const option_7 = config_7;
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
          <p class="text-7xl text-purple-700 text-center mt-8">{{total}}</p>
        </div>
        <div class="square2">
          <v-chart class="chart_2" :option="option_7" />
        </div>
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option_3" />
        </div>
      </div>
      <!-- Segunda Fila-->
      <div class="flex justify-around mt-4">
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option" />
        </div>
        <div class="square2">
          <v-chart class="chart" :option="option_6" />
        </div>
        <div class="rounded-square bg-white">
          <v-chart class="chart" :option="option_4" />
        </div>
      </div>
      <!-- Tercera Fila-->
      <div class="flex justify-around mt-4">
        <div class="square2 bg-white">
          <v-chart class="chart" :option="option_2" />
        </div>
        <div class="square2">
          <v-chart class="chart" :option="option_5" />
        </div>
      </div>
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
  width: 310px;
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