import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2_5 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_2_5/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_2_5 = ref({
    color: ["#16a34a","#facc15","#9333ea","#0284c7"],
    title: {
        text: 'Facilidades tecnologicas',
        right: '16%',
        top: '5%'
    },
    grid: {
        right: '15%', // Ajusta el margen izquierdo para mover la gráfica hacia la izquierda
    },
    legend: {
        right: '2%',
        top: '30%',
        orient: 'vertical'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    yAxis: {
        show: true,
        type: 'value'
    },
    xAxis: {
        type: 'category',
        data: ['Tel.', 'Internet', 'Cel.', 'Datos'],
    },
    series: [
        {
            name: 'Si',
            type: 'bar',
            barWidth: '20%',
            bargap: '30%',
            label: {
                show: 'true',
                position: 'top',
                fontSize: 16
            },
            data: [
                { value: 1 },
                { value: 1 },
            ]
        },
        {
            name: 'No',
            type: 'bar',
            barWidth: '20%',
            bargap: '30%',
            label: {
                show: 'true',
                position: 'top',
                fontSize: 16
            },
            data: [
                { value: 1 },
                { value: 1 },
            ]
        },
    ]

})
