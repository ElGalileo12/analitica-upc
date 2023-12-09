import { ref } from "vue";
import jsonData from "./tabla.json";
// Filtrar y contar los valores
const criticoData = jsonData.filter(item => item.ID_RENDIMIENTO === 1);
const bajoData = jsonData.filter(item => item.ID_RENDIMIENTO === 2);
const normalData = jsonData.filter(item => item.ID_RENDIMIENTO === 3);

const cantidadCritico = criticoData.length;
const cantidadBajo = bajoData.length;
const cantidadNormal = normalData.length;

export const config3 = ref({
  color: ["#16a34a","#facc15","#9333ea","#0284c7"],
  title: {
    text: "Rendimiento de los estudiantes",
    right: "25%",
    top: "5%",
  },
  legend: {
    right: "-20%",
    top: "0%",
    orient: "center",
  },
  tooltip: {
    trigger: "item",
    formatter: "{b}: {c} ",
  },
  xAxis: {
    type: "category",
    data: ["R. Critico", "R. Bajo", "R. Bueno"],
  },
  yAxis: {
    type: "value",
  },

  series: [
    {
      data: [{ value: cantidadCritico }, { value: cantidadBajo },{value: cantidadNormal }],
      type: "bar",
      top: "0%",
      showBackground: "true",
      label: {
        show: 'true',
        position: 'top',
        fontSize: 16
    },
      backgroundStyle: {
        color: "rgba(180, 180, 180, 0.2)",
      },
    },
  ],
});
