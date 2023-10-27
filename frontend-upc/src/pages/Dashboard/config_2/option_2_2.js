import { ref, provide } from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2_2 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_2_2/`);
      //let { data_2_2 } = await axiosApi.get(`/api/get_chart_2_2/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_2_2 = ref({
    
    title: {
        text: 'Rango de ingreso familiar',
        right: '25%',
        top : '5%'
     },
     legend: {
        show: true, // Habilita la leyenda
        orient: 'horizontal',
        top: 'auto'
    },
    tooltip: {
        trigger: 'axis',
        formatter: '{b}: {c} '
    },
   xAxis: {
        type: 'category',
        data: ['0 a 1.3M', '1.3M a 2.5M', '2.5M a 4M', 'Mas de 4M'],
        
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: [
            { value: 1},
            { value: 1},
            { value: 1},
            { value: 1}],
        type: 'bar',
        top : '0%',
        showBackground: 'true',
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
            show: 'true',
            position: 'top',
            fontSize: 16
        },
        }
]
    
})