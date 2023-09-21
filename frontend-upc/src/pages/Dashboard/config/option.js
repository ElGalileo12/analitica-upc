import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };

export const config = ref({
    

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
            { itemStyle: {color: "rgb(101, 197, 189)"},value: 1,name: 'Mujeres' },
            { itemStyle: {color: "rgb(147,112,219)"},value: 1, name: 'Hombres' },
            { itemStyle: {color: "rgba(255, 251, 13, 1)"},value: 1,name: 'Otro Genero' }
            
        ]
        }]
    
})

