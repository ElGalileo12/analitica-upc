import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_4 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_4/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_4 = ref({
    title: {
        text: 'Estudiantes que trabajan',
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
            avoidLabelOverlap: 'false',  // 'false' como string
            left: '-30%',
            top: '25',
            label: {
                show: 'false',  // 'false' como string
                formatter: '({d}%)'
            },
            emphasis: {
                label: {
                    show: 'false',  // 'false' como string
                    fontSize: 10,
                    fontWeight: 'bold',
                }
            },
            labelLine: {
                show: 'false',  // 'false' como string
            },
            data: [
                { itemStyle: { color: "rgb(101, 197, 189)" }, value: 1, name: 'Mujeres' },
                { itemStyle: { color: "rgb(147,112,219)" }, value: 1, name: 'Hombres' },
                { itemStyle: { color: "rgb(255, 251, 13, 1)" }, value: 1, name: 'Otros' },
            ]
        }
    ]

})
