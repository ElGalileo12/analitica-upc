import { ref} from 'vue';
import { axiosApi } from "@/plugins/axios";
export const getOptionChart_2_4 = async () => {
    try {
      let { data } = await axiosApi.get(`/api/get_chart_2_4/`);
      return data;
    } catch (ex) {
      console.error(ex);
    }
  };
export const config_2_4 = ref({
    color: ["#16a34a","#facc15","#9333ea","#0284c7"],
    title: {
        text: 'Tipo de vivienda',
        left: 'center',
        top: '5%'
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
            itemStyle: {
                borderRadius: 5,
                borderColor: '#fff',
                borderWidth: 2
              },
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
                { value: 1, name: 'Familiar' },
                { value: 1, name: 'Propia' },
                { value: 1, name: 'Arrendada' },
                { value: 1, name: 'Otra' },
            ]
        }
    ]

})
