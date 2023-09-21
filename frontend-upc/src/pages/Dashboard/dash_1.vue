<script setup>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart,BarChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components';
import VChart from 'vue-echarts';
import { config, getOptionChart } from './config/option.js'
import { config_2, getOptionChart_2 } from './config/option_2.js'
import { config_3, getOptionChart_3 } from './config/option_3.js'
import { config_4, getOptionChart_4 } from './config/option_4.js'
import { config_5, getOptionChart_5 } from './config/option_5.js'

use([
  CanvasRenderer,
  PieChart,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
]);

// Obtener los datos de getOptionChart
let chartData = null;
getOptionChart().then((data) => {
    chartData = data
  // Actualizar los valores en la opción del gráfico
 option.value.series[0].data = [
    { itemStyle: { color: "rgb(101, 197, 189)" }, value: chartData.a, name: 'Mujeres' },
    { itemStyle: { color: "rgb(147,112,219)" }, value: chartData.b, name: 'Hombres' },
    { itemStyle: { color: "rgba(255, 251, 13, 1)" }, value: chartData.c, name: 'Otro Genero' },
  ];

});
// Obtener los datos de getOptionChart_2
let chartData_2 = null;
getOptionChart_2().then((data) => {
    chartData_2 = data
  // Actualizar los valores en la opción del gráfico
 option_2.value.series[0].data = [
            { itemStyle: {color: "rgb(101, 197, 189)"},value: chartData_2.a},
            { itemStyle: {color: "rgb(147,112,219)"},value:   chartData_2.b},
  ];

});
// Obtener los datos de getOptionChart_3
let chartData_3 = null;
getOptionChart_3().then((data) => {
    chartData_3 = data
  // Actualizar los valores en la opción del gráfico
 option_3.value.series[0].data = [
            { itemStyle: {color: "rgb(101, 197, 189)"},value: chartData_3.a,  name: 'Mujeres'},
            { itemStyle: {color: "rgb(147,112,219)"},value: chartData_3.b , name: 'Hombres'},
  ];

});
// Obtener los datos de getOptionChart_4
let chartData_4 = null;
getOptionChart_4().then((data) => {
    chartData_4 = data
  // Actualizar los valores en la opción del gráfico
 option_4.value.series[0].data = [
                { itemStyle: { color: "rgb(101, 197, 189)" }, value: chartData_4.a, name: 'Mujeres' },
                { itemStyle: { color: "rgb(147,112,219)" }, value: chartData_4.b, name: 'Hombres' },
                { itemStyle: { color: "rgb(255, 251, 13, 1)" }, value: chartData_4.c, name: 'Otros' },
  ];

});
// Obtener los datos de getOptionChart_5
let chartData_5 = null;
getOptionChart_5().then((data) => {
    chartData_5 = data
  // Actualizar los valores en la opción del gráfico
 option_5.value.series[0].data = [
                { value: chartData_5.a1 },
                { value: chartData_5.b1 },
                { value: chartData_5.c1 },
                { value: chartData_5.d1 }
            ];
option_5.value.series[1].data = [           

                { value: chartData_5.a2 },
                { value: chartData_5.b2 },
                { value: chartData_5.c2 },
                { value: chartData_5.d2 }
            ];
option_5.value.series[2].data = [              
                {},
                {},
                { value: chartData_5.c3 },
                {}
            ]

});

// Configuracion para las graficas
//Grafica 1
const option = config
//Grafica 3
const option_2 = config_2
//Grafica 3
const option_3 = config_3
//Grafica 4
const option_4 = config_4
//Grafica 5
const option_5 = config_5
//
</script>
<template>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    </head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-3 my-4" >
                <div id="rounded-square" class="rounded-square">
                    <p id="text-1" class="text-1 text-center"> </p>
                    <p id="text-2" class="text-2 text-center">Estudiantes encuestados</p>
                </div>
            </div>
            <div class="col-md-6 my-4" >
                <div id="square2" class="square2">
                    <v-chart class="chart_2" :option="option_2"/>
                </div>
            </div>
            <div class="col-md-3 my-4" >
                <div id="rounded-square" class="rounded-square">
                    <v-chart class="chart" :option="option_3"/>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-3 my-4" >
                <div id="rounded-square" class="rounded-square">
                    <v-chart class="chart" :option="option"/>
                </div>
            </div>
            <div class="col-md-6 my-4 mx-auto">
                <div id="square2" class="square2">
                    <v-chart class="chart" :option="option_5"/>
                </div>
            </div>
            <div class="col-md-3 my-4" m>
                <div id="rounded-square" class="rounded-square">
                    <v-chart class="chart" :option="option_4"/>
                </div>
            </div>
        </div>
    </div>
</body>
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
body{
background: #9370db;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #7c44ec, #9370db);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #7c44ec, #9370db); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

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
    ;left: 50px;
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

.text-1 +.text-2 {
    margin-top: -25px;
}
  </style>