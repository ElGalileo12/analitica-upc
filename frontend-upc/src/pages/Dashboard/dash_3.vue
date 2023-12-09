<script setup>
import jsonData from "./config_3/tabla.json";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart, BarChart } from "echarts/charts";
import {config3} from "./config_3/option_3.js";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
} from "echarts/components";
import VChart from "vue-echarts";
use([
  CanvasRenderer,
  PieChart,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
]);
//console.log(jsonData);
// Mapear los valores de ID_RENDIMIENTO a los textos específicos
const mapeoRendimiento = {
		1: "Rendimiento Crítico",
		2: "Rendimiento Bajo",
		3: "Rendimiento Bueno",
	};
// Cambiar los valores de ID_RENDIMIENTO
const newData = jsonData.map(item => ({
    ...item,
    ID_RENDIMIENTO: mapeoRendimiento[item.ID_RENDIMIENTO] || item.ID_RENDIMIENTO
}));
// Configuracion para las graficas
//Grafica 1
const option = config3;
</script>

<template>
  <section>
    <div class="p-4">
      <!-- Primera Fila-->
      <div class="flex justify-around">
        <div class="square2">
          <v-chart class="chart_2" :option="option" />
        </div>
        <div>
          <h1 class="mt-5 text-center text-lg font-medium text-green-600 uppercase">Tabla de Datos</h1>
          <div class="mt-5 max-h-96 overflow-y-scroll">
            <table class="m-auto min-w-80 divide-y divide-gray-200">
              <thead>
                <tr>
                  <th
                    class="sticky top-0 bg-green-600 px-6 py-3 text-center text-base font-medium text-gray-50 uppercase tracking-wider"
                  >
                    Nombre
                  </th>
                  <th
                    class="sticky top-0 bg-green-600 px-6 py-3 text-center text-base font-medium text-gray-50 uppercase tracking-wider"
                  >
                    Resultado
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="dato in newData" :key="dato.id">
                  <td class="px-6 py-4 text-center whitespace-nowrap">
                    {{ dato.ID_NOMBRE }}
                  </td>
                  <td class="px-6 py-4 text-center whitespace-nowrap">
                    {{ dato.ID_RENDIMIENTO }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
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

.square2 {
  width: 600px;
  height: 500px;
  background-color: #ffffff;
  border-radius: 50px;
}

td {
  border: 1px solid #dddddd;
  padding: 8px;
}
</style>
