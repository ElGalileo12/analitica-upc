import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_3 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_3/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_3 = ref({
    title: {
        text: 'Estudiantes con hijos',
        left: 'center',
        top: '0%'
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
            avoidLabelOverlap: 'false',
            left: '-30%',
            top: '25',
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
                { itemStyle: { color: "rgb(101, 197, 189)" }, value: 1, name: 'Mujeres' },
                { itemStyle: { color: "rgb(147,112,219)" }, value: 1, name: 'Hombres' },
            ]
        }
    ]

})
