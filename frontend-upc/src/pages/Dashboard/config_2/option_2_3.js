import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2_3 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_2_3/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_2_3 = ref({
    color: ["#16a34a","#facc15","#9333ea"],
    title: {
        text: 'Situacion laboral',
        left: 'center',
        top: '5%'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)'
    },
    legend: {
        right: '-1%',
        top: '30%',
        orient: 'vertical'
    },
    series: [
        {
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: 'false',
            left: '-14%',
            top: '25',
            itemStyle: {
                borderRadius: 5,
                borderColor: '#fff',
                borderWidth: 2
              },
            label: {
                show: 'false',
                formatter: '({d}%)',
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
                {  value: 1, name: 'Estudiante' },
                {  value: 1, name: 'Empleado' },
                {  value: 1, name: 'Independiente' },
            ]
        }
    ]

})
