import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_5 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_5/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_5 = ref({
    color: ["rgb(147,112,219)", "rgb(101, 197, 189)", "rgb(255, 251, 13, 1)"],
    title: {
        text: 'Grado de motivaciion de los estudiantes',
        right: '10%',
        top: '5%'
    },
    legend: {
        right: '0%',
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
        splitLine: { show: 'false' },
        axisLabel: { show: 'false' },
        axisTick: { show: 'false' },
        axisLine: { show: 'false' }
    },
    xAxis: {
        data: ['Bajo', 'Medio', 'Alto', 'Exc'],
    },
    series: [
        {
            name: 'Hombres',
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
                { value: 1 },
                { value: 1 }
            ]
        },
        {
            name: 'Mujeres',
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
                { value: 1 },
                { value: 1 }
            ]
        },
        {
            name: 'Otros',
            type: 'bar',
            barWidth: '20%',
            bargap: '30%',
            label: {
                show: 'true',
                position: 'top',
                fontSize: 16
            },
            data: [
                {},
                {},
                { value: 1 },
                {}
            ]
        }
    ]

})
