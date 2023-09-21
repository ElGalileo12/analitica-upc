import { ref, provide } from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_2/`);
      //let { data_2 } = await axiosApi.get(`/api/get_chart_2/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_2 = ref({
    title: {
        text: 'Estudiantes con mas de 6 años',
        right: '25%',
        top : '5%'
     },
    tooltip: {
        trigger: 'item',
        formatter: '{b}: {c}'
    },
   xAxis: {
        type: 'category',
        data: ['Mujeres', 'Hombres']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: [
            { itemStyle: {color: "rgb(101, 197, 189)"},value: 1},
            { itemStyle: {color: "rgb(147,112,219)"},value:   1},],
        type: 'bar',
        top : '0%',
        showBackground: 'true',
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        }
        }
]
    
})