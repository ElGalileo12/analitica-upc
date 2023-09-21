<template>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grafico</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">


</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-3 my-4" >
                <div id="rounded-square" class="rounded-square">
                    <p id="text-1" class="text-1 text-center"> {{total_estudiantes}}</p>
                    <p id="text-2" class="text-2 text-center">Estudiantes encuestados</p>
                </div>
            </div>
            <div class="col-md-6 my-4" >
                <div id="square2" class="square2">
                    <v-chart class="chart" :option="option"/>
                </div>
            </div>
            <div class="col-md-3 my-4" >
                <div id="rounded-square" class="rounded-square">
                    <v-chart class="chart" :option="option"/>
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
                    <v-chart class="chart" :option="option"/>
                </div>
            </div>
            <div class="col-md-3 my-4" m>
                <div id="rounded-square" class="rounded-square">
                    <v-chart class="chart" :option="option"/>
                </div>
            </div>
        </div>
    </div>
</body>
</template>
  
  <script setup>
  import { axiosApi } from "@/plugins/axios";
  import { use } from 'echarts/core';
  import { CanvasRenderer } from 'echarts/renderers';
  import { PieChart } from 'echarts/charts';
  import {
    TitleComponent,
    TooltipComponent,
    LegendComponent,
  } from 'echarts/components';
  import VChart, { THEME_KEY } from 'vue-echarts';
  import { ref, provide } from 'vue';
  
  use([
    CanvasRenderer,
    PieChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
  ]);
  
  
  const getOptionChart = async () => {
  try {
    let { data } = await axiosApi.get(`/api/get_chart/`);   
    return  data;
} catch (ex) {
    console.error(ex);
  }
};
// Obtener los datos de getOptionChart
let chartData = null;
getOptionChart().then((data) => {
  chartData = data;
// Actualizar los valores en la opción del gráfico
  option.value.series[0].data = [
    { itemStyle: { color: "rgb(101, 197, 189)" }, value: chartData.a, name: 'Mujeres' },
    { itemStyle: { color: "rgb(147,112,219)" }, value: chartData.b, name: 'Hombres' },
    { itemStyle: { color: "rgba(255, 251, 13, 1)" }, value: chartData.c, name: 'Otro Genero' },
  ];
});
  const option = ref({
    title: {
              text: 'Cantidad de estudiantes \n segun su genero',
              left: 'center'
           },
          tooltip: {
              trigger: 'item',
              formatter: '{b}: {c} ({d}%)'
          },
          legend: {
              right: '0%',
              top: '30%',
              orient: 'vertical'
          },
          series: [
          {
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              left: '-30%',
              top: '40',
              label: {
                  show: 'false',
                  formatter: '({d}%)'
              },
          emphasis: {
                  label: {
                  show: 'false',
                  fontSize: 10,
                  fontWeight: 'bold',
                  
                  }
              },
              labelLine: {
                  show: 'false'
              },
              data: [
                  { itemStyle: {color: "rgb(101, 197, 189)"},value: 0,name: 'Mujeres' },
                  { itemStyle: {color: "rgb(147,112,219)"},value: 0, name: 'Hombres' },
                  { itemStyle: {color: "rgba(255, 251, 13, 1)"},value: 0,name: 'Otro Genero' }
                  
              ]
              }
          ]
          })
  </script>
  
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